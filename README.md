# claude-skills (mboizz)

Kumpulan skill Claude milik Heru Supriyanto.

| Skill | Fungsi |
|---|---|
| [cari-joran-reel-tiktok](cari-joran-reel-tiktok/) | Riset joran & reel pancing dari konten TikTok publik: merk, type, spesifikasi, harga, video teratas, saran combo, kreator mancing. |

## Pemasangan

**Claude.ai / aplikasi Claude:** Settings → Capabilities → Skills → upload folder skill (zip).

**Claude Code:**
```bash
git clone https://github.com/mboizz/claude-skills.git
cp -r claude-skills/cari-joran-reel-tiktok ~/.claude/skills/
```

## Opsional: ScrapeCreators API
Untuk angka views/likes yang lengkap, daftar di https://scrapecreators.com lalu:
```bash
export SCRAPECREATORS_API_KEY="kunci_anda"
python3 cari-joran-reel-tiktok/scripts/tiktok_search.py keyword "review reel shimano sedona" --region ID
```
Tanpa API key, skill tetap jalan memakai WebSearch / Firecrawl (angka engagement bisa tidak lengkap).
