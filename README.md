# Laporan Keberlanjutan Bank di BEI

Daftar tautan resmi laporan keberlanjutan (*sustainability report*) emiten bank
yang tercatat di Bursa Efek Indonesia, tahun buku 2020–2025, beserta skrip
untuk mengunduhnya sekaligus.

Repo ini **tidak menyimpan PDF-nya**. Yang disimpan hanya alamat berkas di situs
resmi bank, supaya hak cipta tetap pada penerbitnya dan repo tetap ringan.

## Isi

| Berkas | Isi |
|---|---|
| `data/bank.csv` | 48 emiten subindustri Bank (klasifikasi IDX-IC), dengan situs resmi dan tanggal pencatatan |
| `data/laporan.csv` | Satu baris per laporan: kode, tahun buku, bahasa, URL, sumber, status verifikasi, catatan |
| `scripts/unduh.py` | Pengunduh, hanya pustaka standar Python 3.8+ |

Kolom `terverifikasi = ya` berarti berkasnya sudah diunduh dan sampulnya dicek
cocok dengan bank dan tahun bukunya.

## Cara pakai

```bash
git clone <url-repo-ini>
cd laporan-keberlanjutan-bank-idx
python3 scripts/unduh.py                    # semua laporan
python3 scripts/unduh.py --kode BBCA BBRI   # bank tertentu
python3 scripts/unduh.py --tahun 2023       # tahun buku tertentu
```

Berkas tersimpan di `unduhan/<KODE>/<KODE>_<TAHUN>.pdf` (laporan berbahasa
Inggris diberi akhiran `_EN`). `unduhan/manifest.csv` mencatat ukuran dan
SHA-256 tiap berkas.

## Cakupan saat ini

Baru empat bank terbesar yang lengkap dan terverifikasi: BBCA, BBRI, BMRI, BBNI
(2020–2025). Bank lain menyusul. Status per bank bisa dilihat dari
`data/laporan.csv`.

## Catatan sumber

- Arsip terlengkap ada di situs hubungan investor masing-masing bank.
  Pengumuman laporan keberlanjutan di IDX baru tersedia mulai tahun buku 2023.
- Sebagian bank kecil tidak menerbitkan laporan keberlanjutan terpisah;
  isinya menjadi satu bab di laporan tahunan (*integrated report*). Baris
  seperti itu ditandai `jenis = laporan_tahunan_terintegrasi`.
- Situs bank bisa memindahkan berkasnya. Kalau tautan mati, buka *issue* atau
  kirim *pull request* berisi tautan pengganti.

## Menambah atau memperbaiki tautan

Tambahkan baris di `data/laporan.csv` dengan kolom yang sama. Isi
`terverifikasi = ya` hanya kalau berkasnya sudah kamu buka dan cocok dengan bank
serta tahun bukunya.

---

**English:** Links to official sustainability reports of banks listed on the
Indonesia Stock Exchange (fiscal years 2020–2025), plus a stdlib-only Python
downloader. PDFs are not redistributed; only links to the issuers' own sites.

Kode skrip berlisensi MIT.
