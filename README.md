# claude-skills (mboizz)

Kumpulan skill Claude milik Heru Supriyanto.

| Skill | Fungsi |
|---|---|
| [cari-joran-tiktok](cari-joran-tiktok/) | Riset merk/seri joran pancing dari konten TikTok publik: video teratas, review, harga disebut kreator, kreator mancing, tren hashtag. |

## Pemasangan

**Claude.ai / aplikasi Claude:** Settings → Capabilities → Skills → upload folder skill (zip).

**Claude Code:**
```bash
git clone https://github.com/mboizz/claude-skills.git
cp -r claude-skills/cari-joran-tiktok ~/.claude/skills/
```

## Opsional: ScrapeCreators API
Untuk angka views/likes yang lengkap, daftar di https://scrapecreators.com lalu:
```bash
export SCRAPECREATORS_API_KEY="kunci_anda"
python3 cari-joran-tiktok/scripts/tiktok_search.py keyword "review joran daido" --region ID
```
Tanpa API key, skill tetap jalan memakai WebSearch / Firecrawl (angka engagement bisa tidak lengkap).
