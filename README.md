# Sentra Technology — sentratechnology.com

Website company profile PT. Sentra Visi Teknologi. Situs statis (HTML/CSS/JS) dalam 5 bahasa: ID (root), `/en`, `/zh`, `/ko`, `/ms`.

## Struktur

- `site/` — seluruh isi website, disajikan apa adanya oleh Vercel.
- `vercel.json` — tanpa build. Mengatur URL bersih (`/about` → `site/about.html`, `/about.html` → 308 ke `/about`), cache aset, dan halaman 404 per bahasa.
- `site/assets/js/ocean.js` + `site/assets/css/ocean.css` — laut ASCII: di hero beranda (hiu + ikan, logo Sentra sebagai koin ASCII yang berputar) dan di footer semua halaman (ikan saja). Kualitas menyesuaikan perangkat: 30 fps, turun ke 20 fps / 2 hiu di perangkat lemah, dan berhenti jadi gambar diam kalau masih terlalu berat.
- `site/assets/js/ocean/` — engine laut ASCII dari [ascii-sharks](https://github.com/stackedlol/ascii-sharks) (MIT, lihat `LICENSE.txt` di folder itu), dikonversi ke JS biasa dengan latar navy Sentra.

## Jalankan lokal

Situs memakai URL tanpa `.html`, jadi pakai server yang meniru aturan di `vercel.json`, misalnya:

```bash
npx vercel dev
```

## Deploy

Push ke `main` otomatis di-deploy ke production oleh integrasi Git Vercel (project `sentratech/compro-sentra`). Branch lain jadi deploy preview.
