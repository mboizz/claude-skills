#!/usr/bin/env python3
"""Cari video/kreator TikTok publik lewat ScrapeCreators API.

Butuh env SCRAPECREATORS_API_KEY. Hanya pustaka standar Python.

Contoh:
  python3 tiktok_search.py keyword "review joran daido" --region ID --limit 20
  python3 tiktok_search.py hashtag joranpancing --limit 30 --csv hasil.csv
  python3 tiktok_search.py users "review joran"
  python3 tiktok_search.py profile namakreator
"""
import argparse
import csv
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

BASE = "https://api.scrapecreators.com"
ENDPOINTS = {
    "keyword": ("/v1/tiktok/search/keyword", "query"),
    "top": ("/v1/tiktok/search/top", "query"),
    "hashtag": ("/v1/tiktok/search/hashtag", "hashtag"),
    "users": ("/v1/tiktok/search/users", "query"),
    "profile": ("/v1/tiktok/profile", "handle"),
}
DATE_MAP = {
    "yesterday": "yesterday", "this-week": "this-week", "this-month": "this-month",
    "last-3-months": "last-3-months", "last-6-months": "last-6-months", "all-time": "all-time",
}


def call(path, params, key):
    url = BASE + path + "?" + urllib.parse.urlencode({k: v for k, v in params.items() if v})
    req = urllib.request.Request(url, headers={"x-api-key": key, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")[:300]
        sys.exit(f"HTTP {e.code} dari ScrapeCreators: {body}")
    except urllib.error.URLError as e:
        sys.exit(f"Gagal terhubung ke ScrapeCreators ({e.reason}). Jaringan diblokir? Pakai jalur Firecrawl/WebSearch.")


def find_videos(obj):
    """Cari objek video (punya aweme_id/statistics) di mana pun dalam respons."""
    out = []

    def walk(o):
        if isinstance(o, dict):
            if "aweme_info" in o and isinstance(o["aweme_info"], dict):
                out.append(o["aweme_info"])
                return
            if ("aweme_id" in o or "id" in o) and ("statistics" in o or "stats" in o) and ("desc" in o or "author" in o):
                out.append(o)
                return
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(obj)
    seen, uniq = set(), []
    for v in out:
        vid = str(v.get("aweme_id") or v.get("id"))
        if vid not in seen:
            seen.add(vid)
            uniq.append(v)
    return uniq


def find_users(obj):
    out = []

    def walk(o):
        if isinstance(o, dict):
            if "user_info" in o and isinstance(o["user_info"], dict):
                out.append(o["user_info"])
                return
            if "unique_id" in o and ("follower_count" in o or "nickname" in o) and "aweme_id" not in o:
                out.append(o)
                return
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(obj)
    return out


def g(d, *keys, default=None):
    for k in keys:
        if isinstance(d, dict) and d.get(k) is not None:
            return d[k]
    return default


def video_row(v):
    st = g(v, "statistics", "stats", default={}) or {}
    au = g(v, "author", default={}) or {}
    handle = g(au, "unique_id", "uniqueId", default="?")
    vid = str(g(v, "aweme_id", "id", default=""))
    ts = g(v, "create_time", "createTime")
    tgl = dt.datetime.fromtimestamp(int(ts)).strftime("%Y-%m-%d") if ts else ""
    views = int(g(st, "play_count", "playCount", default=0) or 0)
    likes = int(g(st, "digg_count", "diggCount", default=0) or 0)
    kom = int(g(st, "comment_count", "commentCount", default=0) or 0)
    share = int(g(st, "share_count", "shareCount", default=0) or 0)
    er = round((likes + kom + share) / views * 100, 2) if views else None
    return {
        "tanggal": tgl, "views": views, "likes": likes, "komentar": kom, "share": share,
        "engagement_pct": er, "kreator": "@" + handle,
        "caption": (g(v, "desc", default="") or "").replace("\n", " ")[:160],
        "url": g(v, "share_url", default=None) or f"https://www.tiktok.com/@{handle}/video/{vid}",
    }


def user_row(u):
    h = g(u, "unique_id", "uniqueId", default="?")
    return {
        "kreator": "@" + h, "nama": g(u, "nickname", default=""),
        "followers": int(g(u, "follower_count", "followerCount", default=0) or 0),
        "likes_total": int(g(u, "total_favorited", "heartCount", "heart", default=0) or 0),
        "bio": (g(u, "signature", default="") or "").replace("\n", " ")[:120],
        "url": f"https://www.tiktok.com/@{h}",
    }


def fmt(n):
    return f"{n:,}".replace(",", ".") if isinstance(n, int) else ("—" if n is None else str(n))


def main():
    p = argparse.ArgumentParser(description="Cari TikTok via ScrapeCreators")
    p.add_argument("mode", choices=ENDPOINTS)
    p.add_argument("term", help="kata kunci / hashtag (tanpa #) / handle (tanpa @)")
    p.add_argument("--region", default="ID")
    p.add_argument("--sort", choices=["relevance", "most-liked", "date-posted"])
    p.add_argument("--date", choices=list(DATE_MAP))
    p.add_argument("--limit", type=int, default=20)
    p.add_argument("--json", help="simpan respons mentah")
    p.add_argument("--csv", help="simpan tabel hasil")
    a = p.parse_args()

    key = os.environ.get("SCRAPECREATORS_API_KEY")
    if not key:
        sys.exit("SCRAPECREATORS_API_KEY belum di-set. Daftar di scrapecreators.com, atau pakai jalur Firecrawl/WebSearch.")

    path, pname = ENDPOINTS[a.mode]
    term = a.term.lstrip("#@")
    params = {pname: term}
    if a.mode in ("keyword", "top", "users"):
        params["region"] = a.region
    if a.mode in ("keyword", "top"):
        params["sort_by"] = a.sort
        params["date_posted"] = DATE_MAP.get(a.date) if a.date else None

    data = call(path, params, key)
    if a.json:
        with open(a.json, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    if a.mode in ("users", "profile"):
        rows = [user_row(u) for u in find_users(data)]
        if a.mode == "profile" and not rows and isinstance(data, dict):
            rows = [user_row({**(data.get("user") or {}), **(data.get("stats") or {})})]
        rows.sort(key=lambda r: r["followers"], reverse=True)
    else:
        rows = [video_row(v) for v in find_videos(data)]
        rows.sort(key=lambda r: r["views"], reverse=True)
    rows = rows[: a.limit]

    if not rows:
        print("Tidak ada hasil terbaca. Cek --json untuk struktur respons.")
        return
    if a.csv:
        with open(a.csv, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]))
            w.writeheader()
            w.writerows(rows)

    for i, r in enumerate(rows, 1):
        if "views" in r:
            print(f"{i:>2}. {r['tanggal']} | views {fmt(r['views'])} | likes {fmt(r['likes'])} | "
                  f"kom {fmt(r['komentar'])} | share {fmt(r['share'])} | ER {fmt(r['engagement_pct'])}% | "
                  f"{r['kreator']} | {r['caption']} | {r['url']}")
        else:
            print(f"{i:>2}. {r['kreator']} ({r['nama']}) | followers {fmt(r['followers'])} | "
                  f"likes {fmt(r['likes_total'])} | {r['bio']} | {r['url']}")


if __name__ == "__main__":
    main()
