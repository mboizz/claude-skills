---
name: cari-joran-reel-tiktok
description: Gunakan saat user mencari, membandingkan, atau memantau joran (rod) dan/atau reel pancing di TikTok, YouTube, Facebook, atau Shopee — merk, type/seri, spesifikasi, harga baru/bekas, review, video terpopuler, kreator mancing, combo joran+reel, atau tren #joranpancing #reelpancing.
---

# Cari Joran & Reel Pancing (TikTok, YouTube, Facebook, Shopee)

Skill untuk riset **joran** dan **reel** pancing dari konten publik di empat platform:
- **TikTok**: video promosi/review pendek, kreator, dan tren.
- **YouTube**: review panjang. Biasanya paling lengkap untuk spesifikasi, kelebihan, dan kekurangan.
- **Facebook**: grup komunitas, halaman toko, dan **harga barang bekas**.
- **Shopee** (shopee.co.id): **harga baru**, varian, dan nama toko.

Semua jawaban dalam Bahasa Indonesia.

## 1. Pahami permintaan

Tangkap dari pesan user (jangan tanya ulang kalau sudah jelas):
- **Platform**: kalau user menyebut platform tertentu ("di TikTok", "di Shopee"), utamakan platform itu. Kalau tidak menyebut, cari di keempat platform.
- **Kategori**: joran, reel, atau keduanya / combo. "Gulungan" atau "katrol" = reel.
- **Merk / seri**. Kalau user hanya menyebut jenis, mulai dari merk populer:
  - Joran: Daido, Kenzi, Exori, Pioneer, Maguro, Relix Nusantara, Kaizo, Shimano, Daiwa, Major Craft, Abu Garcia, Kastking, Penn, Ugly Stik.
  - Reel: Shimano (Sienna, FX, Sedona, Nasci, Miravel, Vanford, Stradic, SLX, Curado), Daiwa (Revros, Crossfire, LT, Fuego, BG, Tatula), Abu Garcia (Black Max, Pro Max, Revo), Penn (Battle, Spinfisher, Slammer), Ryobi, Daido, Kenzi, Exori, Pioneer, Maguro, Seahawk, Kastking, Haibo, Deukio.
- **Satu nama bisa dipakai beberapa seri** (contoh: Relix "Samson" = joran slow jigging, joran galatama GS 602, reel Samson SW, dan senar PE Samson X12). Pisahkan per seri dan sebutkan di ringkasan.
- **Jenis joran**: spinning, casting/baitcasting, UL, jigging, surf/pantai, tegek, fly.
- **Jenis reel**: spinning, baitcasting (BC), overhead/conventional, power handle (PH), lever drag, slow jigging, surf/longcast, fly.
- **Ukuran & kebutuhan**: panjang/power joran; ukuran reel (spinning 500–1000 UL/kolam, 2000–3000 serbaguna, 4000–5000 laut ringan/pantai, 6000+ jigging/ikan besar; BC 100–150 ringan–sedang, 200–300 laut), drag, gear ratio.
- **Budget**, **teknik/lokasi** (kolam, sungai, laut, pantai, boat), **target ikan**.
- **Tujuan**: perbandingan, video terpopuler, cari kreator, pantau tren, harga termurah/bekas, atau rekomendasi combo.

## 2. Kumpulkan data per platform

Kirim pencarian antar-platform **sekaligus dalam satu giliran** (paralel). Untuk perbandingan, cari tiap merk/seri secara terpisah, dan joran serta reel dengan query terpisah.

Alat yang dipakai, urut dari yang terbaik:
1. **ScrapeCreators API** (khusus TikTok): hanya kalau ada env `SCRAPECREATORS_API_KEY` dan shell bisa mengakses `api.scrapecreators.com`.
2. **Firecrawl** (`firecrawl_search` / `firecrawl_scrape`): kalau connector terhubung.
3. **WebSearch**: selalu tersedia. Pakai pola query yang sama dengan Firecrawl. Angka views/likes dari jalur ini sering tidak ada; tulis "—", jangan menebak.

### TikTok
- **ScrapeCreators**: `GET https://api.scrapecreators.com/v1/tiktok/search/keyword?query=...&region=ID` (header `x-api-key`), atau `/v1/tiktok/search/hashtag?hashtag=...`, `/v1/tiktok/search/users?query=...`, `/v1/tiktok/profile?handle=...`. Script siap pakai: `scripts/tiktok_search.py`. Satu query per merk/seri, jangan berulang (memakai kredit).
- **Firecrawl search**: `site:tiktok.com <joran|reel> <merk> <seri>`, plus variasi kata (`review`, `one piece`, `PE 1-3`, `drag test`, `#joran<seri>`). Satu query biasanya memberi 10–25 hasil berisi judul dan cuplikan.
- Query umum lain: `tiktok reel spinning <ukuran> murah <budget>`, `tiktok combo joran reel <jenis> <budget>`.
- **Views/likes per video**: `firecrawl_scrape` URL video dengan `formats: ["query"]`. Biayanya **±34 kredit per video** (lewat provider influencers-club), jadi jangan scrape semua. Ambil untuk 3–5 video teratas saja, atau tanyakan dulu ke user kalau ingin lebih banyak. Halaman foto (`/photo/`) tidak bisa di-scrape.
- Hashtag: #joranpancing #reviewjoran #reelpancing #reviewreel #reelspinning #reelbc #combopancing #mancingmania #ultralight #jigging #mancinglaut #fishingindonesia.

### YouTube
- **Cari**: `site:youtube.com <merk> <seri> review` / `joran <merk> <seri>` / `reel <merk> <seri> drag test`.
- **Detail**: `firecrawl_scrape` URL `youtube.com/watch?v=...` dengan `formats: ["query"]` (±5 kredit). Hasilnya berisi nama channel, tanggal unggah, views, likes, deskripsi, dan isi transkrip. Minta spesifikasi per varian beserta kelebihan/kekurangan yang disebut reviewer.
- Prioritaskan scrape **review independen** (channel reviewer) dan video dari **pembuat/kolaborator** produk. Spesifikasi dari YouTube dipakai untuk **meluruskan** angka TikTok yang bertentangan.

### Facebook
- **Cari**: `site:facebook.com <merk> <seri> joran`, dan `site:facebook.com <merk> <seri> second OR bekas OR jual` untuk harga bekas.
- Halaman Facebook **tidak bisa di-scrape** (Firecrawl menolak). Pakai cuplikan dari hasil pencarian saja, dan tulis di catatan bahwa isinya hanya dari cuplikan.
- Yang dicari: halaman resmi merk/kolaborator, postingan toko (sering memuat spesifikasi), grup komunitas pengguna, dan **postingan jual barang bekas** (harga, kondisi, lokasi).

### Shopee (shopee.co.id)
- **Cari**: `site:shopee.co.id <joran|reel> <merk> <seri>`, plus varian (`PE 1-3`, `SP`, `OH`, `GS 602`, ukuran reel). Cuplikan hasil pencarian biasanya memuat **judul listing, harga atau rentang harga, dan kadang nama toko**.
- Halaman Shopee (pencarian maupun produk) **diblokir verifikasi traffic** kalau di-scrape. Jangan ulangi scrape; pakai cuplikan hasil pencarian saja.
- Kalau user ingin data terjual/rating/stok dan browser Claude in Chrome tersedia, tawarkan untuk membuka Shopee lewat browser itu. Jangan login atau checkout atas nama user.
- **Pembanding harga** (opsional): halaman pencarian `tokopedia.com/find/<kata-kunci>` bisa di-scrape (±5 kredit) dan memberi daftar judul + harga yang panjang. Blibli dan Lazada bisa dipakai lewat cuplikan pencarian.

## 3. Saring dan nilai

- Simpan hanya konten yang relevan dengan kategori yang diminta (joran, reel, atau combo). Buang konten senar/umpan/kail saja kecuali diminta.
- Tandai jenis sumber: **resmi** (merk/kolaborator), **review independen**, **toko/afiliasi** (keranjang kuning, "link di bio", "cek di toko"), **komunitas**, **jual bekas**.
- Catat klaim spesifikasi dan harga. Harga dari video = "harga disebut kreator per <tanggal>", bukan harga pasti.
- **Cocokkan angka antar-platform.** Kalau ada yang bertentangan (panjang, berat, line rating, jig weight), tampilkan keduanya, beri tanda ⚠️, dan sebutkan sumber mana yang paling kuat (urutannya: resmi/label > review YouTube > toko > TikTok).
- **Harga Shopee**: catat harga terendah–tertinggi per varian. Tandai listing yang jauh di bawah pasaran (≥40% lebih murah) dengan ⚠️, karena bisa barang KW, ujung joran saja (top section), atau salah input.
- Untuk reel, catat juga keluhan yang sering muncul: drag tersendat, spool goyang, bunyi/kasar, karat (air asin), backlash (BC), handle oblak.
- Skor sederhana per video: engagement = (likes + komentar + share) / views. Tampilkan bila views ada.
- Waspadai barang tiruan/KW: sebut bila komentar, kreator, atau penjual menyinggungnya.

## 4. Lengkapi spesifikasi & harga

Untuk tiap produk yang muncul:
1. Ambil apa yang disebut di video, caption, komentar, postingan, dan judul listing.
2. Lengkapi kolom kosong dari **review YouTube** dan **sumber resmi** (situs/katalog merk, label pada produk): `<merk> <seri> spesifikasi`, `<merk> <seri> specs gear ratio max drag`.
3. Harga: **harga disebut kreator**, **harga baru Shopee** (rentang), pembanding Tokopedia/Blibli/Lazada bila perlu, dan **harga bekas Facebook** bila ada. Selalu cantumkan tanggal pengecekan.
4. Satu seri sering punya beberapa varian (joran: panjang/power/PE, SP/OH; reel: ukuran 1000/2500/4000, gear ratio HG/XG, handle kiri/kanan). Tulis satu baris per varian.
5. Tandai asal tiap angka: **(T)** TikTok, **(Y)** YouTube, **(F)** Facebook, **(S)** Shopee, **(M)** marketplace lain, **(R)** sumber resmi. Kolom yang tidak ditemukan diisi "—".

## 5. Format jawaban

1. **Ringkasan 2–4 kalimat**: seri apa saja yang ditemukan, mana yang paling banyak dibahas, sentimennya, dan kisaran harga.
2. **Tabel produk joran** (bila joran diminta; satu baris per seri/varian):
   `| # | Merk | Seri/Type | Jenis | Panjang | Power/Action | Line (lb/PE) | Lure/Jig wt | Berat | Bahan | Ruas/Ring/Reel seat | Harga baru (Shopee) | Harga bekas | Sumber |`
3. **Tabel produk reel** (bila reel diminta; satu baris per seri/ukuran):
   `| # | Merk | Seri/Type | Jenis | Ukuran | Gear ratio | Max drag (kg) | Bearing | Kapasitas senar (PE/mono) | Tarikan per putaran (cm) | Berat (g) | Bahan body/spool | Harga baru (Shopee) | Harga bekas | Sumber |`
   Untuk BC tambahkan di kolom Jenis: sistem rem (magnet/sentrifugal/DC) dan handle kiri/kanan.
4. **Listing Shopee** (maks 10, urut harga termurah): `| # | Judul/varian | Harga | Toko | Link |`. Beri ⚠️ untuk harga mencurigakan.
5. **Saran combo** (bila user minta combo, atau joran dan reel dicari bersamaan): pasangan joran–reel yang cocok berdasarkan jenis (spinning↔spinning, BC↔casting), ukuran reel vs line rating joran, dan total kisaran harga. Jelaskan alasannya singkat.
6. **Konten teratas per platform**, digabung dalam satu tabel (maks 10 TikTok + 5 YouTube + 5 Facebook, kecuali user minta jumlah lain):
   `| # | Platform | Kreator/Channel/Grup | Seri | Jenis sumber | Views | Likes | Tgl | Poin utama | Link |`
7. **Kelebihan/kekurangan per seri**: utamakan yang disebut review independen, lalu komentar dan komunitas. Sebutkan juga cocok untuk teknik/lokasi apa.
8. **Angka yang bertentangan** (⚠️) dan sumber mana yang paling bisa dipercaya.
9. **Kreator/channel rekomendasi** untuk diikuti (bila relevan).
10. **Catatan**: alat yang dipakai, tanggal pencarian, keterbatasan (Facebook dan Shopee hanya dari cuplikan, views TikTok hanya untuk video yang di-scrape). Harga berubah, jadi cek ulang sebelum beli.

Bila user minta dashboard/pantauan berkala, buat HTML single-file (IBM Plex Sans/Mono, Chart.js di-inline, tema terang cream #EDE2C8 / spruce #18412D / aksen tomato #EE4129) dengan tab Joran / Reel / Combo / Harga: tabel produk (filter jenis, sortir harga), tabel listing Shopee, tabel konten per platform, dan grafik views per merk.

## 6. Aturan

- Hanya data publik. Jangan login ke akun TikTok/Facebook/Shopee user, jangan mengunduh video, jangan checkout.
- Jangan mengarang angka, harga, atau spesifikasi. Kosong lebih baik daripada salah.
- Kutipan caption, postingan, dan listing maksimal satu kalimat pendek; sisanya parafrase.
- Hemat kredit Firecrawl: pencarian ±2–6 kredit, scrape YouTube/marketplace ±5, scrape video TikTok ±34. Jangan scrape halaman yang sudah diketahui tidak bisa (Facebook, Shopee, foto TikTok).
- Selalu cantumkan link asli (video, postingan, listing) agar user bisa cek sendiri.
