# Sentra Technology — sentratechnology.com

Website company profile PT. Sentra Visi Teknologi. Situs statis (HTML/CSS/JS) dalam 5 bahasa: ID (root), `/en`, `/zh`, `/ko`, `/ms`.

## Struktur

- `site/` — seluruh isi website, disajikan apa adanya oleh Vercel.
- `vercel.json` — tanpa build. Mengatur URL bersih (`/about` → `site/about.html`, `/about.html` → 308 ke `/about`), cache aset, dan halaman 404 per bahasa.
- `site/assets/js/hero-ocean.js` + `site/assets/css/hero-ocean.css` — animasi hero beranda: laut ASCII dan logo Sentra sebagai koin ASCII yang berputar.
- `site/assets/js/ocean/` — engine laut ASCII dari [ascii-sharks](https://github.com/stackedlol/ascii-sharks) (MIT, lihat `LICENSE.txt` di folder itu), dikonversi ke JS biasa dengan latar navy Sentra.

## Jalankan lokal

Situs memakai URL tanpa `.html`, jadi pakai server yang meniru aturan di `vercel.json`, misalnya:

```bash
npx vercel dev
```

## Deploy

Push ke `main` otomatis di-deploy ke production oleh integrasi Git Vercel (project `sentratech/compro-sentra`). Branch lain jadi deploy preview.
