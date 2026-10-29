# Sentra Technology — sentratechnology.com

Website company profile PT. Sentra Visi Teknologi. Situs statis (HTML/CSS/JS) dalam 5 bahasa: ID (root), `/en`, `/zh`, `/ko`, `/ms`.

## Struktur

- `site/` — seluruh isi website, disajikan apa adanya oleh Vercel.
- `vercel.json` — tanpa build. Mengatur URL bersih (`/about` → `site/about.html`, `/about.html` → 308 ke `/about`), cache aset, dan halaman 404 per bahasa.
- `site/assets/js/field.js` + `site/assets/css/ocean.css` — medan ASCII: gumpalan glyph yang pelan-pelan berubah bentuk, digambar di GPU dengan satu fragment shader WebGL (simplex noise, MIT). Hero beranda dan hero halaman Artikel versi light mode (glyph biru di atas biru terang) dan footer semua halaman versi gelap (gradient biru tua ke navy yang menyambung CTA). Seluruh area medan ditutup kaca tipis (blur 2,5px langsung di canvas + lapisan warna) supaya teks tidak tertimpa tapi gerakannya tetap terlihat. CPU hampir tidak terpakai; 30 fps, berhenti saat di luar layar, dan satu frame diam tanpa WebGL atau saat "kurangi gerakan" aktif.
- `site/assets/js/koi.js` — kolam koi ASCII di hero halaman Tentang (pengganti foto tim): tiga koi (kohaku, ogon, showa) berenang di lintasan elips yang landai. JS hanya menghitung 10 titik tulang punggung per koi; shader yang sama gayanya dengan field.js mengisi siluet (badan, sirip dada, ekor bercabang, mata, bayangan) dan riak air. 30 fps, berhenti di luar layar, satu frame diam saat "kurangi gerakan" aktif.
- `site/assets/img/art/` + `site/assets/og/art-*.jpg` — ilustrasi ASCII pengganti stock foto: medan glyph tipis di atas navy dengan satu ikon Lucide (ISC) per topik. Dibuat dengan `tools/ascii-art.py <ikon.svg> <tujuan> W H seed` (butuh Pillow dan `rsvg-convert`; ikon dari `https://unpkg.com/lucide-static@0.460.0/icons/<nama>.svg`). Jangan menambah stock foto baru; pakai screenshot proyek asli atau ilustrasi dari skrip ini.
- `site/assets/js/reach.js` + `site/assets/css/reach.css` + `site/assets/img/reach/` — peta jangkauan interaktif di section "Pusat teknologi dari Samarinda": Hardware (Kalimantan Timur) dan Software (seluruh dunia). Di desktop peta mengisi setengah kanan section sampai tepi layar; di HP selebar layar di bawah teks. Data peta dari Natural Earth dan batas provinsi BAKOSURTANAL.
- Saat mengubah file di `/assets`, naikkan versi `?v=` di HTML (dan di import antar-modul), karena `/assets/*` di-cache setahun.

## Jalankan lokal

Situs memakai URL tanpa `.html`, jadi pakai server yang meniru aturan di `vercel.json`, misalnya:

```bash
npx vercel dev
```

## Deploy

Push ke `main` otomatis di-deploy ke production oleh integrasi Git Vercel (project `sentratech/compro-sentra`). Branch lain jadi deploy preview.
