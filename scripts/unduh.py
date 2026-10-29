#!/usr/bin/env python3
"""Unduh laporan keberlanjutan yang terdaftar di data/laporan.csv.

Contoh:
    python3 scripts/unduh.py                 # semua
    python3 scripts/unduh.py --kode BBCA     # satu bank
    python3 scripts/unduh.py --tahun 2022 2023

Hanya pustaka standar Python 3.8+. Berkas disimpan di unduhan/<KODE>/.
"""
import argparse
import csv
import hashlib
import sys
import time
import urllib.request
from pathlib import Path

AKAR = Path(__file__).resolve().parent.parent
UA = "esg-bank/1.0 (+https://github.com/setyawanbayu355-sketch/esg-bank)"


def nama_berkas(r):
    akhir = "" if r["bahasa"] == "id" else "_" + r["bahasa"].upper()
    return f'{r["kode"]}_{r["tahun_buku"]}{akhir}.pdf'


def unduh(url, tujuan, coba=3):
    for i in range(coba):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=300) as resp:
                isi = resp.read()
            if not isi.startswith(b"%PDF"):
                raise ValueError("bukan PDF (mungkin halaman HTML/blokir)")
            tujuan.write_bytes(isi)
            return isi
        except Exception as e:  # noqa: BLE001
            if i == coba - 1:
                raise
            print(f"  ulang ({e})", file=sys.stderr)
            time.sleep(5 * (i + 1))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kode", nargs="*")
    ap.add_argument("--tahun", nargs="*")
    ap.add_argument("--keluar", default=str(AKAR / "unduhan"))
    ap.add_argument("--jeda", type=float, default=2.0, help="detik antar unduhan")
    a = ap.parse_args()

    baris = list(csv.DictReader(open(AKAR / "data" / "laporan.csv", encoding="utf-8")))
    if a.kode:
        baris = [r for r in baris if r["kode"] in {k.upper() for k in a.kode}]
    if a.tahun:
        baris = [r for r in baris if r["tahun_buku"] in set(a.tahun)]
    baris = [r for r in baris if r["url"]]

    keluar = Path(a.keluar)
    gagal = 0
    log = []
    for r in baris:
        tujuan = keluar / r["kode"] / nama_berkas(r)
        tujuan.parent.mkdir(parents=True, exist_ok=True)
        if tujuan.exists() and tujuan.read_bytes()[:4] == b"%PDF":
            isi = tujuan.read_bytes()
            status = "sudah ada"
        else:
            try:
                isi = unduh(r["url"], tujuan)
                status = "ok"
                time.sleep(a.jeda)
            except Exception as e:  # noqa: BLE001
                gagal += 1
                print(f"GAGAL {tujuan.name}: {e}", file=sys.stderr)
                continue
        sha = hashlib.sha256(isi).hexdigest()
        log.append([tujuan.name, len(isi), sha, r["url"]])
        print(f"{status:9} {tujuan.name} ({len(isi) // 1024:,} KB)")

    with open(keluar / "manifest.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["berkas", "ukuran_byte", "sha256", "url"])
        w.writerows(log)
    print(f"\nSelesai: {len(log)} berkas, {gagal} gagal. Daftar di {keluar / 'manifest.csv'}")
    sys.exit(1 if gagal else 0)


if __name__ == "__main__":
    main()
