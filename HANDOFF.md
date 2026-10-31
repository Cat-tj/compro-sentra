# Serah terima: cara melanjutkan pekerjaan situs dan SEO Sentra

Untuk agent atau orang yang melanjutkan. Baca juga `CLAUDE.md` (aturan teknis dan keputusan desain) dan `docs/seo/` (peta pasar dan daftar artikel). Terakhir diperbarui 31 Okt 2026.

## Akses yang dibutuhkan
- GitHub: repo kerja `Cat-tj/compro-sentra` (branch `static-site-remodel`), repo resmi `Sentra-Technology/compro-sentra`. Token fine-grained, satu repo, Contents dan Pull requests read-write.
- Vercel: project `sentratech/compro-sentra`, team `sentratech`. Token dibatasi ke team itu.
- Tidak perlu: DNS, registrar, kata sandi akun utama. Jangan simpan token di repo atau chat.
- Alat lokal: python3 + Pillow, vercel CLI, curl, xmllint. (Opsional: `swift` untuk hapus latar foto di macOS.)

## Alur kerja (selalu urut)
1. Ubah file di `site/` (5 bahasa: root=id, `en/`, `zh/`, `ko/`, `ms/`).
2. Jika mengubah CSS/JS: naikkan `?v=` di semua HTML yang memuatnya. Jika mengganti gambar: beri nama file baru (`-v2`), jangan timpa (aset di-cache 1 tahun, dan respons 404 pun bisa tersangkut cache).
3. Commit, push ke `fork` (`git push fork HEAD:static-site-remodel`).
4. Deploy preview dari ekspor bersih: `git archive HEAD | tar -x -C <dir-kosong-berisi-.vercel>` lalu `vercel deploy --yes --scope sentratech`.
5. Verifikasi preview (butuh share link Vercel untuk preview yang diproteksi): semua halaman berubah 200, JSON-LD valid (`json.loads` tiap blok), tautan internal ada, gambar 200, sitemap valid (`xmllint`), file kunci IndexNow 200.
6. Promote (instruksi tetap pemilik sejak 30 Okt: langsung promote setelah verifikasi lolos, tanpa bertanya): `vercel promote <url-preview> --yes --timeout 3m --scope sentratech`. Cek ulang di www.sentratechnology.com dengan curl.
7. IndexNow: `python3 tools/indexnow.py --since YYYY-MM-DD` (atau daftar URL). Kunci `site/d01773ca34bcf938cfbdbeff95ad2284.txt` tidak boleh dihapus atau diganti nama.
8. Laporkan ke pemilik apa yang live dan apa yang belum diverifikasi secara visual.

## Menambah konten
- Artikel (5 bahasa): tulis `tools/articles/<slug>.py` (lihat `starlink-untuk-tambang.py`), jalankan `python3 tools/new-article.py tools/articles/<slug>.py` lalu `python3 tools/blog-seo.py`. Byline selalu Raphael Wicaksono. Tanggal = tanggal terbit asli.
- Halaman layanan: `tools/pages/<slug>.json` lalu `python3 tools/new-service-page.py tools/pages/<slug>.json`; tambahkan juga ke setiap `services.html`, `sitemap.xml`, `llms.txt`.
- Gambar sampul ASCII: `python3 tools/ascii-art.py <icon.svg> <dst.webp|jpg> W H seed` (ikon Lucide dari unpkg lucide-static). OG image 1200x630 jpg.
- Aturan penulisan lengkap ada di akhir `docs/seo/daftar-artikel.md` (panjang 1.200-2.000 kata, FAQ 3-5 pertanyaan di akhir, H2 berbentuk pertanyaan, min. 2 tautan layanan dan 1 artikel lain, harga berupa rentang dengan tanggal acuan).

## Status per 31 Okt 2026
- Beranda: FAQ "Apa itu Sentra Technology?", WebSite `alternateName`, judul ID "Sentra Technology Samarinda | CCTV AI, IoT & Software".
- Artikel terbit: lihat kolom Status di `docs/seo/daftar-artikel.md` (6 dari Daftar Artikel + artikel awal lain).
- Halaman Tentang: bagian tim tiga grup (Leadership, Infra, Software) dengan foto asli 12 dari 13 (Ilham masih avatar inisial), bio masih draf dari jabatan.
- Hero Tentang dan footer masih memakai WebGL (`field.js`, `koi.js`). Pemilik mengeluh laptopnya berat; kandidat dibuat statis.

## Utang yang diketahui (kerjakan lebih dulu)
- Empat artikel yang ditulis 31 Okt (SPBE, WebGIS, CCTV tambang, Satu Data) lebih pendek dari aturan (sekitar 600-700 kata) dan belum punya FAQ 3-5 pertanyaan. Tambahkan FAQ dan perpanjang.
- Artikel terjemahan zh, ko, ms ditulis tanpa penutur asli: minta review.
- Nomor aturan di artikel SPBE (Perpres 95/2018, Perpres 132/2022, Permen PANRB 59/2020) dan Satu Data (Perpres 39/2019, UU 27/2022) ditulis dari pengetahuan umum, belum dicek ke sumber resmi.
- Verifikasi Google Search Console belum ada (tambahkan meta `google-site-verification` di 5 beranda bila pemilik memberi kodenya) dan sitemap belum dikirim.
- Organization JSON-LD belum punya `sameAs` (butuh URL profil sosial pemilik).

## Yang jangan dilakukan
- Jangan menulis klaim kapabilitas Sentra yang tidak ada di situs atau dokumen (merek, spesifikasi, status mitra, sertifikasi, harga). Tanyakan pemilik.
- Jangan membuat halaman kembar per kota; isi harus unik.
- Jangan mengubah DNS, pengaturan keamanan, atau menghapus konten tanpa persetujuan pemilik.
- Jangan menambah animasi berat: pemilik menguji di laptop dan HP lemah.
