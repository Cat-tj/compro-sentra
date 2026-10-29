# Sentra Technology — sentratechnology.com

Website company profile PT. Sentra Visi Teknologi. Situs statis (HTML/CSS/JS) dalam 5 bahasa: ID (root), `/en`, `/zh`, `/ko`, `/ms`.

## Struktur

- `site/` — seluruh isi website, disajikan apa adanya oleh Vercel.
- `vercel.json` — tanpa build. Mengatur URL bersih (`/about` → `site/about.html`, `/about.html` → 308 ke `/about`), cache aset, dan halaman 404 per bahasa.
- `site/assets/js/field.js` + `site/assets/css/ocean.css` — medan ASCII: gumpalan glyph yang pelan-pelan berubah bentuk, digambar di GPU dengan satu fragment shader WebGL (simplex noise, MIT). Hero beranda versi light mode (glyph biru di atas biru terang) dan footer semua halaman versi gelap (gradient biru tua ke navy yang menyambung CTA). CPU hampir tidak terpakai; 30 fps, berhenti saat di luar layar, dan satu frame diam tanpa WebGL atau saat "kurangi gerakan" aktif.
- `site/assets/js/reach.js` + `site/assets/css/reach.css` + `site/assets/img/reach/` — peta jangkauan interaktif di section "Pusat teknologi dari Samarinda": Hardware (Kalimantan Timur) dan Software (seluruh dunia). Data peta dari Natural Earth dan batas provinsi BAKOSURTANAL.
- Saat mengubah file di `/assets`, naikkan versi `?v=` di HTML (dan di import antar-modul), karena `/assets/*` di-cache setahun.

## Jalankan lokal

Situs memakai URL tanpa `.html`, jadi pakai server yang meniru aturan di `vercel.json`, misalnya:

```bash
npx vercel dev
```

## Deploy

Push ke `main` otomatis di-deploy ke production oleh integrasi Git Vercel (project `sentratech/compro-sentra`). Branch lain jadi deploy preview.
