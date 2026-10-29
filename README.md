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

Lihat bagian Cakupan untuk arti kolom `terverifikasi`.

## Cara pakai

```bash
git clone https://github.com/setyawanbayu355-sketch/esg-bank.git
cd esg-bank
python3 scripts/unduh.py                    # semua laporan
python3 scripts/unduh.py --kode BBCA BBRI   # bank tertentu
python3 scripts/unduh.py --tahun 2023       # tahun buku tertentu
```

Berkas tersimpan di `unduhan/<KODE>/<KODE>_<TAHUN>.pdf` (laporan berbahasa
Inggris diberi akhiran `_EN`). `unduhan/manifest.csv` mencatat ukuran dan
SHA-256 tiap berkas.

## Cakupan saat ini

Semua 48 bank punya tautan untuk setidaknya sebagian tahun; 220 dari 288 kombinasi bank-tahun sudah terisi.

- `SR`: tautan langsung ke PDF laporan keberlanjutan di situs resmi bank.
- `IDX`: lampiran pengajuan laporan tahunan di situs IDX. Laporan keberlanjutan
  termasuk salah satu lampirannya, tetapi IDX menamai lampiran `att1`, `att2`,
  dan seterusnya, jadi isi tiap lampiran perlu dicek. Mulai tahun buku 2024
  ada juga formulir ESG (E020) dari emiten.
- `—`: belum ada tautan. Untuk 2020–2021 arsip IDX memang tidak lengkap, dan
  beberapa bank baru tercatat di bursa setelah 2020.

| Kode | Bank | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| AGRO | Bank Raya Indonesia | — | — | IDX | IDX | — | IDX |
| AGRS | Bank IBK Indonesia | — | — | IDX | IDX | IDX | IDX |
| AMAR | Bank Amar Indonesia | — | — | IDX | IDX | — | IDX |
| ARTO | Bank Jago | — | — | IDX | IDX | IDX | IDX |
| BABP | Bank MNC Internasional | — | IDX | IDX | IDX | IDX | IDX |
| BACA | Bank Capital Indonesia | — | IDX | IDX | IDX | IDX | — |
| BANK | Bank Aladin Syariah | — | — | IDX | IDX | IDX | IDX |
| BBCA | Bank Central Asia | SR | SR | SR | SR | SR | SR |
| BBHI | Allo Bank Indonesia | — | — | IDX | IDX | — | IDX |
| BBKP | Bank KB Indonesia | — | IDX | IDX | IDX | IDX | IDX |
| BBMD | Bank Mestika Dharma | — | — | IDX | IDX | IDX | IDX |
| BBNI | Bank Negara Indonesia (Persero) | SR | SR | SR | SR | SR | SR |
| BBRI | Bank Rakyat Indonesia (Persero) | SR | SR | SR | SR | SR | SR |
| BBSI | Krom Bank Indonesia | — | IDX | IDX | IDX | IDX | IDX |
| BBTN | Bank Tabungan Negara (Persero) | SR | SR | SR | SR | SR | SR |
| BBYB | Bank Neo Commerce | IDX | IDX | IDX | IDX | IDX | IDX |
| BCIC | Bank JTrust Indonesia | — | IDX | IDX | IDX | IDX | — |
| BDMN | Bank Danamon Indonesia | IDX | — | IDX | IDX | — | IDX |
| BEKS | Bank Pembangunan Daerah Banten | — | IDX | IDX | IDX | IDX | IDX |
| BGTG | Bank Ganesha | — | — | IDX | IDX | IDX | IDX |
| BINA | Bank Ina Perdana | — | — | IDX | IDX | — | IDX |
| BJBR | Bank Pembangunan Daerah Jawa Barat dan Banten | IDX | — | SR | SR | — | IDX |
| BJTM | Bank Pembangunan Daerah Jawa Timur | — | — | IDX | IDX | IDX | IDX |
| BKSW | Bank QNB Indonesia | — | — | IDX | IDX | IDX | IDX |
| BMAS | Bank Kasikorn Indonesia | — | IDX | IDX | IDX | IDX | IDX |
| BMRI | Bank Mandiri (Persero) | SR | SR | SR | SR | SR | SR |
| BNBA | Bank Bumi Arta | — | — | IDX | IDX | IDX | IDX |
| BNGA | Bank CIMB Niaga | SR | SR | SR | SR | SR | SR |
| BNII | Bank Maybank Indonesia | SR | SR | SR | SR | SR | SR |
| BNLI | Bank Permata | — | — | IDX | IDX | — | IDX |
| BRIS | Bank Syariah Indonesia (Persero) | SR | SR | SR | SR | SR | SR |
| BSIM | Bank Sinarmas | — | — | IDX | IDX | IDX | IDX |
| BSWD | Bank of India Indonesia | — | IDX | IDX | IDX | IDX | IDX |
| BTPN | Bank SMBC Indonesia | SR | SR | SR | SR | SR | SR |
| BTPS | Bank BTPN Syariah | — | — | IDX | IDX | IDX | IDX |
| BVIC | Bank Victoria International | — | — | IDX | IDX | IDX | IDX |
| DNAR | Bank Oke Indonesia | — | IDX | IDX | IDX | IDX | IDX |
| INPC | Bank Artha Graha Internasional | — | IDX | IDX | IDX | IDX | IDX |
| MASB | Bank Multiarta Sentosa | — | — | IDX | IDX | IDX | IDX |
| MAYA | Bank Mayapada Internasional | — | IDX | IDX | IDX | IDX | IDX |
| MCOR | Bank China Construction Bank Indonesia | — | IDX | IDX | IDX | IDX | IDX |
| MEGA | Bank Mega | SR | SR | SR | SR | — | IDX |
| NISP | Bank OCBC NISP | SR | SR | SR | SR | SR | SR |
| NOBU | Bank Nationalnobu | — | IDX | IDX | IDX | IDX | IDX |
| PNBN | Bank Pan Indonesia | — | IDX | IDX | IDX | IDX | IDX |
| PNBS | Bank Panin Dubai Syariah | — | IDX | IDX | IDX | IDX | IDX |
| SDRA | Bank Woori Saudara Indonesia 1906 | IDX | — | IDX | IDX | — | IDX |
| SUPA | Super Bank Indonesia | — | — | — | — | — | IDX |

Kolom `terverifikasi` di `data/laporan.csv`:

- `ya`: berkas sudah diunduh dan sampulnya cocok dengan bank dan tahun buku.
- `belum`: tautan diambil dari halaman resmi, tetapi berkasnya belum dibuka.

Kolom `jenis`: `laporan_keberlanjutan`, `lampiran_laporan_tahunan_idx`, atau
`formulir_esg_idx`. Pakai `--jenis` di skrip untuk memilih.

Situs IDX kadang menolak unduhan otomatis. Tautan yang gagal dicatat di
`unduhan/gagal.csv` dan bisa dibuka langsung di browser.

## Cara mencari tautan bank lain

1. Buka situs bank (kolom `situs` di `data/bank.csv`), lalu menu
   Hubungan Investor → Laporan Keberlanjutan / *Sustainability Report*.
2. Banyak bank memakai penyedia situs investor yang sama; polanya
   `https://<domain-investor>/sustainability_reports.html`, dengan berkas di
   `/misc/SR/`. Contoh: BRI, BSI, CIMB Niaga.
3. Kalau tidak ada halaman khusus, laporan keberlanjutan biasanya menjadi bab
   di laporan tahunan. Isi `jenis = laporan_tahunan_terintegrasi`.
4. Mulai tahun buku 2023, bank juga mengunggahnya ke IDX lewat pengumuman
   "Penyampaian Laporan Keberlanjutan" di menu Keterbukaan Informasi. Situs
   IDX membatasi akses otomatis, jadi tautan IDX sebaiknya dibuka lewat
   browser, bukan skrip.

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
