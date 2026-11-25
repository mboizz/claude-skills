---
name: cari-joran-reel-tiktok
description: Gunakan saat user mencari, membandingkan, atau memantau joran (rod) dan/atau reel pancing di TikTok — merk, type/seri, spesifikasi, harga, review, video terpopuler, kreator mancing, combo joran+reel, atau tren #joranpancing #reelpancing.
---

# Cari Joran & Reel Pancing di TikTok

Skill untuk riset **joran** dan **reel** pancing dari konten TikTok publik: merk, type/seri,
spesifikasi, harga, video review/unboxing/strike test/drag test, dan kreator mancing yang sering
membahasnya. Semua jawaban dalam Bahasa Indonesia.

## 1. Pahami permintaan

Tangkap dari pesan user (jangan tanya ulang kalau sudah jelas):
- **Kategori**: joran, reel, atau keduanya / combo (joran + reel yang cocok dipasangkan).
  Kalau tidak disebut, ikuti kata yang dipakai user ("reel", "gulungan", "katrol" = reel).
- **Merk / seri** (mis. joran Daido Hurricane, Kenzi Sky Hawk; reel Shimano Sedona,
  Daiwa Revros, Abu Garcia Black Max). Kalau user hanya menyebut jenis, pakai
  `references/merk-joran-reel.md`.
- **Jenis joran**: spinning, casting/baitcasting, UL, jigging, surf/pantai, tegek, fly.
- **Jenis reel**: spinning, baitcasting (BC), overhead/conventional, power handle (PH),
  lever drag, slow jigging, surf/longcast, fly.
- **Ukuran & kebutuhan**: panjang/power joran; ukuran reel (1000–10000 untuk spinning,
  100–300 untuk BC), drag, gear ratio.
- **Budget**, **teknik/lokasi** (kolam, sungai, laut, pantai, boat), **target ikan**.
- **Tujuan**: perbandingan, video terpopuler, cari kreator, pantau tren, atau rekomendasi combo.

## 2. Kumpulkan data — pilih jalur yang tersedia, urut dari yang terbaik

### Jalur A — ScrapeCreators API (paling lengkap, butuh API key)
Kalau env `SCRAPECREATORS_API_KEY` ada dan shell bisa mengakses `api.scrapecreators.com`:

```bash
python3 scripts/tiktok_search.py keyword "review joran daido" --region ID --limit 20
python3 scripts/tiktok_search.py keyword "review reel shimano sedona" --region ID --limit 20
python3 scripts/tiktok_search.py hashtag reelpancing --limit 30
python3 scripts/tiktok_search.py users "review reel pancing" --limit 10
python3 scripts/tiktok_search.py profile namakreator
```
Opsi: `--sort relevance|most-liked|date-posted`, `--date this-week|this-month|last-3-months|last-6-months|all-time`,
`--json out.json` untuk simpan mentah, `--csv out.csv` untuk tabel.
Setiap panggilan memakai kredit API — jalankan 1 query per merk/seri, jangan berulang.

### Jalur B — Firecrawl (kalau connector Firecrawl terhubung)
- `firecrawl_search`: `site:tiktok.com <joran|reel> <merk> <seri> review`.
- `firecrawl_scrape` untuk `https://www.tiktok.com/tag/<hashtag>` atau `https://www.tiktok.com/@<user>`
  bila perlu angka views/likes. Halaman TikTok berat JavaScript; bila hasil kosong, pakai jalur C.

### Jalur C — WebSearch (selalu tersedia)
Jalankan beberapa query berbeda sekaligus, misalnya:
- `site:tiktok.com joran <merk> <seri>` / `site:tiktok.com reel <merk> <seri>`
- `tiktok review reel <merk> <seri> drag test`
- `tiktok reel spinning <ukuran> murah <budget>`
- `tiktok combo joran reel <jenis> <budget>`
Angka views/likes dari jalur ini sering tidak ada — tulis "—", jangan menebak.

Untuk perbandingan, cari **tiap merk/seri secara terpisah**, dan joran serta reel dengan query terpisah.

## 3. Saring dan nilai

- Simpan hanya video yang relevan dengan kategori yang diminta (joran, reel, atau combo).
  Buang konten senar/umpan/kail saja kecuali diminta.
- Tandai **konten jualan/afiliasi** (keranjang kuning, "link di bio", toko resmi) vs **review independen**.
- Catat klaim spesifikasi dan harga yang disebut. Harga dari video = "harga disebut kreator
  per <tanggal video>", bukan harga pasti.
- Untuk reel, catat juga keluhan yang sering muncul: drag tersendat, spool goyang, bunyi/kasar,
  karat (air asin), backlash (BC), handle oblak.
- Skor sederhana per video: engagement = (likes + komentar + share) / views. Tampilkan bila views ada.
- Waspadai barang tiruan/KW: sebut bila komentar atau kreator menyinggungnya.

## 4. Lengkapi spesifikasi & harga

Caption TikTok jarang memuat spesifikasi lengkap. Untuk tiap produk yang muncul:
1. Ambil dulu apa yang disebut di caption/video/komentar.
2. Lengkapi kolom yang kosong dari **sumber resmi** (situs/katalog merk, label pada produk)
   lewat WebSearch/Firecrawl: `<merk> <seri> spesifikasi`, `<merk> <seri> specs gear ratio max drag`.
3. Harga: catat **harga disebut kreator** dan, bila perlu, **kisaran harga marketplace**
   (Tokopedia/Shopee/toko resmi) dari pencarian web, dengan tanggal pengecekan.
4. Satu seri sering punya beberapa varian (joran: panjang/power; reel: ukuran 1000/2500/4000,
   gear ratio HG/XG, handle kiri/kanan). Tulis satu baris per varian yang dibahas.
5. Tandai asal tiap angka: (V) dari video, (R) dari sumber resmi, (M) dari marketplace.
   Kolom yang tidak ditemukan diisi "—".

## 5. Format jawaban

1. **Ringkasan 2–4 kalimat**: produk mana yang paling banyak dibahas & sentimennya.
2. **Tabel produk joran** (bila joran diminta; satu baris per seri/varian):
   `| # | Merk | Seri/Type | Jenis | Panjang | Power/Action | Line (lb/PE) | Lure/Casting wt | Bahan | Ruas/Ring | Harga disebut | Kisaran harga pasar | Video acuan |`
3. **Tabel produk reel** (bila reel diminta; satu baris per seri/ukuran):
   `| # | Merk | Seri/Type | Jenis | Ukuran | Gear ratio | Max drag (kg) | Bearing | Kapasitas senar (PE/mono) | Tarikan per putaran (cm) | Berat (g) | Bahan body/spool | Harga disebut | Kisaran harga pasar | Video acuan |`
   Untuk BC tambahkan di kolom Jenis: sistem rem (magnet/sentrifugal/DC) dan handle kiri/kanan.
4. **Saran combo** (bila user minta combo, atau joran dan reel dicari bersamaan): pasangan
   joran–reel yang cocok berdasarkan jenis (spinning↔spinning, BC↔casting), ukuran reel vs line
   rating joran, dan total kisaran harga. Jelaskan alasannya singkat.
5. **Tabel video teratas** (maks 10):
   `| # | Kategori | Merk/Seri | Kreator | Views | Likes | Tgl | Jenis konten | Poin utama | Link |`
6. **Kelebihan/kekurangan per seri** menurut kreator & komentar, plus cocok untuk teknik/lokasi apa.
7. **Kreator rekomendasi** untuk diikuti (bila relevan).
8. **Catatan**: sumber data (jalur A/B/C), tanggal pencarian, keterbatasan. Harga berubah — cek ulang sebelum beli.

Bila user minta dashboard/pantauan berkala, buat HTML single-file (IBM Plex Sans/Mono,
Chart.js di-inline, tema terang cream #EDE2C8 / spruce #18412D / aksen tomato #EE4129)
dengan tab Joran / Reel / Combo: tabel produk (filter jenis, sortir harga), tabel video,
dan grafik views per merk.

## 6. Aturan

- Hanya data publik. Jangan login ke akun TikTok user, jangan mengunduh video.
- Jangan mengarang angka, harga, atau spesifikasi. Kosong lebih baik daripada salah.
- Kutipan caption maksimal satu kalimat pendek; sisanya parafrase.
- Selalu cantumkan link video asli agar user bisa cek sendiri.
