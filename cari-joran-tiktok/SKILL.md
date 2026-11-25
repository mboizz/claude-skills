---
name: cari-joran-tiktok
description: Gunakan saat user mencari, membandingkan, atau memantau merk/seri joran pancing (rod) di TikTok — review, harga yang disebut kreator, video terpopuler, kreator mancing, atau tren hashtag #joranpancing.
---

# Cari Joran Pancing di TikTok

Skill untuk riset merk dan seri joran pancing dari konten TikTok publik: video review,
unboxing, strike test, harga yang disebut kreator, dan kreator mancing yang sering membahasnya.
Semua jawaban dalam Bahasa Indonesia.

## 1. Pahami permintaan

Tangkap dari pesan user (jangan tanya ulang kalau sudah jelas):
- **Merk / seri** (mis. Daido Hurricane, Kenzi Sky Hawk, Shimano FX). Kalau user hanya
  menyebut jenis ("joran UL buat casting"), pakai daftar di `references/merk-joran.md`.
- **Jenis joran**: spinning, casting/baitcasting, UL/ultralight, jigging, surf/pantai,
  tegek, fly. **Panjang / power / action / bahan** (carbon, fiber, solid).
- **Budget** dan **teknik/lokasi** (kolam, sungai, laut, pantai, boat).
- **Tujuan**: perbandingan, video terpopuler, cari kreator, atau pantau tren.

## 2. Kumpulkan data — pilih jalur yang tersedia, urut dari yang terbaik

### Jalur A — ScrapeCreators API (paling lengkap, butuh API key)
Kalau env `SCRAPECREATORS_API_KEY` ada dan shell bisa mengakses `api.scrapecreators.com`:

```bash
python3 scripts/tiktok_search.py keyword "review joran daido" --region ID --limit 20
python3 scripts/tiktok_search.py hashtag joranpancing --limit 30
python3 scripts/tiktok_search.py users "review joran" --limit 10
python3 scripts/tiktok_search.py profile mancingmania --limit 1
```
Opsi: `--sort relevance|most-liked|date-posted`, `--date this-week|this-month|last-3-months|last-6-months|all-time`,
`--json out.json` untuk simpan mentah, `--csv out.csv` untuk tabel.
Script mengeluarkan baris ringkas: tanggal, views, likes, komentar, share, @kreator, caption, URL.
Setiap panggilan memakai kredit API — jalankan 1 query per merk/seri, jangan berulang.

### Jalur B — Firecrawl (kalau connector Firecrawl terhubung)
- `firecrawl_search` dengan query `site:tiktok.com joran <merk> <seri> review`.
- `firecrawl_scrape` untuk `https://www.tiktok.com/tag/<hashtag>` atau `https://www.tiktok.com/@<user>`
  bila perlu angka views/likes. Halaman TikTok berat JavaScript; bila hasil kosong, pakai jalur C.

### Jalur C — WebSearch (selalu tersedia)
Jalankan beberapa query berbeda sekaligus, misalnya:
- `site:tiktok.com joran <merk> <seri>`
- `tiktok review joran <merk> <seri> strike`
- `tiktok joran <jenis> murah <budget>`
- `tiktok #joranpancing <merk>`
Angka views/likes dari jalur ini sering tidak ada — tulis "—", jangan menebak.

Untuk perbandingan beberapa merk, cari **tiap merk secara terpisah**.

## 3. Saring dan nilai

- Buang video yang bukan joran (reel/senar saja, konten umpan) kecuali diminta.
- Tandai **konten jualan/afiliasi** (keranjang kuning, "link di bio", toko resmi) vs **review independen**.
- Catat klaim spesifikasi yang disebut: panjang, PE/line rating, casting weight, action, ring, harga.
  Harga dari video = "harga disebut kreator per <tanggal video>", bukan harga pasti.
- Skor sederhana per video: engagement = (likes + komentar + share) / views. Tampilkan bila views ada.
- Waspadai merk tiruan/KW: sebut bila komentar atau kreator menyinggungnya.

## 4. Lengkapi spesifikasi & harga

Caption TikTok jarang memuat spesifikasi lengkap. Untuk tiap joran yang muncul:
1. Ambil dulu apa yang disebut di caption/video/komentar.
2. Lengkapi kolom yang kosong dari **sumber resmi** (situs/katalog merk, label di blank joran)
   lewat WebSearch/Firecrawl: `<merk> <seri> spesifikasi`, `<merk> <seri> line weight lure weight`.
3. Harga: catat **harga disebut kreator** (dari video) dan, bila perlu, **kisaran harga marketplace**
   (Tokopedia/Shopee/toko resmi) dari pencarian web, dengan tanggal pengecekan.
4. Satu seri sering punya beberapa varian (panjang/power). Tulis satu baris per varian yang dibahas.
5. Tandai asal tiap angka: (V) dari video, (R) dari sumber resmi, (M) dari marketplace.
   Kolom yang tidak ditemukan diisi "—".

## 5. Format jawaban

1. **Ringkasan 2–4 kalimat**: merk/seri mana yang paling banyak dibahas & sentimennya.
2. **Tabel produk joran** (WAJIB, satu baris per seri/varian):
   `| # | Merk | Seri/Type | Jenis | Panjang | Power/Action | Line (lb/PE) | Lure/Casting wt | Bahan | Ruas/Ring | Harga disebut | Kisaran harga pasar | Video acuan |`
   Jenis = spinning/casting/UL/jigging/surf/tegek. Urutkan sesuai permintaan user (harga, popularitas, atau kecocokan).
3. **Tabel video teratas** (maks 10):
   `| # | Merk/Seri | Kreator | Views | Likes | Tgl | Jenis konten | Poin utama | Link |`
4. **Kelebihan/kekurangan per seri** menurut kreator & komentar (bila ada), plus cocok untuk teknik/lokasi apa.
5. **Kreator rekomendasi** untuk diikuti (bila relevan).
6. **Catatan**: sumber data (jalur A/B/C), tanggal pencarian, keterbatasan. Harga berubah — selalu cek ulang sebelum beli.

Bila user minta dashboard/pantauan berkala, buat HTML single-file (IBM Plex Sans/Mono,
Chart.js di-inline, tema terang cream #EDE2C8 / spruce #18412D / aksen tomato #EE4129)
berisi tabel produk (filter jenis, sortir harga), tabel video, dan grafik views per merk.

## 6. Aturan

- Hanya data publik. Jangan login ke akun TikTok user, jangan mengunduh video.
- Jangan mengarang angka, harga, atau spesifikasi. Kosong lebih baik daripada salah.
- Kutipan caption maksimal satu kalimat pendek; sisanya parafrase.
- Selalu cantumkan link video asli agar user bisa cek sendiri.
