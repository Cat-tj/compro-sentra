# Sentra Technology — sentratechnology.com

Website company profile PT. Sentra Visi Teknologi. Situs statis (HTML/CSS/JS) dalam 5 bahasa: ID (root), `/en`, `/zh`, `/ko`, `/ms`.

## Struktur

- `site/` — seluruh isi website, disajikan apa adanya oleh Vercel.
- `vercel.json` — tanpa build. Mengatur URL bersih (`/about` → `site/about.html`, `/about.html` → 308 ke `/about`), cache aset, dan halaman 404 per bahasa.
- `site/assets/css/aurora.css` — background "Soft Aurora" di hero beranda (light mode, biru terang) dan footer semua halaman (navy): cahaya warna-warni lembut yang melayang pelan. Murni CSS (gradient radial + animasi transform), tanpa JavaScript, canvas, atau filter blur, jadi ringan di HP murah; berhenti otomatis kalau pengunjung memilih "kurangi gerakan". Saat mengubah file di `/assets`, naikkan versi `?v=` di HTML, karena `/assets/*` di-cache setahun.

## Jalankan lokal

Situs memakai URL tanpa `.html`, jadi pakai server yang meniru aturan di `vercel.json`, misalnya:

```bash
npx vercel dev
```

## Deploy

Push ke `main` otomatis di-deploy ke production oleh integrasi Git Vercel (project `sentratech/compro-sentra`). Branch lain jadi deploy preview.
