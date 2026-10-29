# Sentra Technology — sentratechnology.com

Website company profile PT. Sentra Visi Teknologi. Situs statis (HTML/CSS/JS) dalam 5 bahasa: ID (root), `/en`, `/zh`, `/ko`, `/ms`.

## Struktur

- `site/` — seluruh isi website, disajikan apa adanya oleh Vercel.
- `vercel.json` — tanpa build. Mengatur URL bersih (`/about` → `site/about.html`, `/about.html` → 308 ke `/about`), cache aset, dan halaman 404 per bahasa.
- `site/assets/js/ocean.js` (+ `ocean-worker.js`, `ocean/scene.js`) dan `site/assets/css/ocean.css` — laut ASCII bergaya ascii-sharks (hiu berwarna, ikan `-` `><` `<=>` `<>`): hero beranda versi light mode (air biru terang, ikan warna-warni, logo Sentra sebagai koin ASCII putih yang berputar) dan footer semua halaman versi gelap (latar hitam, tanpa koin). Digambar di Web Worker lewat OffscreenCanvas supaya thread utama tetap bebas. HP memakai preset lebih ringan (hiu lebih sedikit, fps lebih rendah), dan kualitas turun otomatis sampai gambar diam kalau perangkat kewalahan. Saat mengubah file di `assets/js/ocean*`, naikkan versi `?v=` di semua import dan di HTML, karena `/assets/*` di-cache setahun.
- `site/assets/js/ocean/` — engine laut ASCII dari [ascii-sharks](https://github.com/stackedlol/ascii-sharks) (MIT, lihat `LICENSE.txt` di folder itu), dikonversi ke JS biasa, ditambah tema (warna hiu, glyph ikan) dan dukungan Web Worker.

## Jalankan lokal

Situs memakai URL tanpa `.html`, jadi pakai server yang meniru aturan di `vercel.json`, misalnya:

```bash
npx vercel dev
```

## Deploy

Push ke `main` otomatis di-deploy ke production oleh integrasi Git Vercel (project `sentratech/compro-sentra`). Branch lain jadi deploy preview.
