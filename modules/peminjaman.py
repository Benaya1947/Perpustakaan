import os
from modules import utils
from datetime import datetime, timedelta

DATA_PATH = os.path.join("data", "peminjaman.json")
RIWAYAT_PATH = os.path.join("data", "riwayat_pengembalian.json")

DENDA_PER_HARI = 2000  # denda per hari keterlambatan


class PeminjamanManager:
    def __init__(self, buku_manager, member_manager):
        self.data = utils.load_json(DATA_PATH, [])       # pinjaman aktif
        self.riwayat = utils.load_json(RIWAYAT_PATH, []) # riwayat pengembalian
        self.buku_manager = buku_manager
        self.member_manager = member_manager

    def simpan(self):
        utils.save_json(DATA_PATH, self.data)
        utils.save_json(RIWAYAT_PATH, self.riwayat)

    def tampilkan_pinjaman_aktif(self):
        """Menampilkan daftar peminjaman tanpa pause."""
        print("=== DAFTAR PEMINJAMAN AKTIF ===")
        if not self.data:
            print("(Belum ada peminjaman aktif)")
        else:
            hari_ini = datetime.now().date()
            for i, pinjam in enumerate(self.data, start=1):
                tgl_kembali = datetime.strptime(pinjam["tgl_kembali"], "%Y-%m-%d").date()
                if hari_ini > tgl_kembali:
                    terlambat = (hari_ini - tgl_kembali).days
                    denda = terlambat * DENDA_PER_HARI
                    status = f"Terlambat {terlambat} hari (Denda: Rp {denda:,})"
                else:
                    status = "On Time"
                print(f"{i}. Anggota: {pinjam['nama_anggota']}")
                print(f"   Buku: {pinjam['judul_buku']}")
                print(f"   Tgl Pinjam: {pinjam['tgl_pinjam']}")
                print(f"   Tgl Kembali: {pinjam['tgl_kembali']}")
                print(f"   Status: {status}")
                print("-" * 30)

    def lihat_semua(self):
        utils.clear_screen()
        self.tampilkan_pinjaman_aktif()
        utils.pause()

    def lihat_riwayat(self):
        utils.clear_screen()
        print("=== RIWAYAT PENGEMBALIAN ===")
        if not self.riwayat:
            print("(Belum ada riwayat)")
        else:
            for i, r in enumerate(self.riwayat, start=1):
                print(f"{i}. Anggota: {r['nama_anggota']}")
                print(f"   Buku: {r['judul_buku']}")
                print(f"   Tgl Pinjam: {r['tgl_pinjam']}")
                print(f"   Tgl Kembali (Rencana): {r['tgl_kembali_rencana']}")
                print(f"   Tgl Dikembalikan: {r['tgl_dikembalikan']}")
                print(f"   Terlambat: {r['terlambat_hari']} hari")
                print(f"   Denda: Rp {r['denda']:,}")
                print("-" * 30)
        utils.pause()

    def pinjam_buku(self):
        utils.clear_screen()
        print("=== PINJAM BUKU ===")

        # Pilih anggota
        self.member_manager.lihat_semua()
        if not self.member_manager.data:
            return
        idx_member = utils.input_angka("Pilih nomor anggota: ") - 1
        if not (0 <= idx_member < len(self.member_manager.data)):
            print("⚠ Nomor anggota tidak valid.")
            utils.pause()
            return
        anggota = self.member_manager.data[idx_member]

        # Pilih buku
        self.buku_manager.lihat_semua()
        if not self.buku_manager.data:
            return
        idx_buku = utils.input_angka("Pilih nomor buku: ") - 1
        if not (0 <= idx_buku < len(self.buku_manager.data)):
            print("⚠ Nomor buku tidak valid.")
            utils.pause()
            return
        buku = self.buku_manager.data[idx_buku]

        # Cek stok buku
        if buku["stok"] <= 0:
            print("❌ Buku tidak tersedia.")
            utils.pause()
            return

        # Tanggal pinjam & kembali
        tgl_pinjam = datetime.now().date()
        tgl_kembali = tgl_pinjam + timedelta(days=7)  # default 7 hari

        # Simpan data pinjaman
        self.data.append({
            "nama_anggota": anggota["nama"],
            "judul_buku": buku["judul"],
            "tgl_pinjam": str(tgl_pinjam),
            "tgl_kembali": str(tgl_kembali)
        })

        # Kurangi stok buku
        buku["stok"] -= 1
        self.buku_manager.simpan()
        self.simpan()

        print(f"✅ Buku '{buku['judul']}' berhasil dipinjam oleh {anggota['nama']}.")
        utils.pause()

    def kembalikan_buku(self):
        utils.clear_screen()
        print("=== PENGEMBALIAN BUKU ===")

        if not self.data:
            print("(Tidak ada pinjaman aktif)")
            utils.pause()
            return

        self.tampilkan_pinjaman_aktif()

        idx = utils.input_angka("Pilih nomor peminjaman yang ingin dikembalikan: ") - 1
        if not (0 <= idx < len(self.data)):
            print("⚠ Nomor tidak valid.")
            utils.pause()
            return

        pinjam = self.data[idx]
        tgl_kembali = datetime.strptime(pinjam["tgl_kembali"], "%Y-%m-%d").date()
        hari_ini = datetime.now().date()
        terlambat = max(0, (hari_ini - tgl_kembali).days)
        total_denda = terlambat * DENDA_PER_HARI

        if terlambat > 0:
            print(f"⚠ Terlambat {terlambat} hari. Total denda: Rp{total_denda:,}")
            sisa = total_denda
            while sisa > 0:
                try:
                    bayar = int(input(f"Masukkan nominal pembayaran (Sisa: Rp{sisa:,}): "))
                except ValueError:
                    print("⚠ Masukkan angka yang benar!")
                    continue
                if bayar <= 0:
                    print("⚠ Nominal harus lebih dari 0.")
                    continue
                sisa -= bayar
                if sisa > 0:
                    print(f"💰 Uang kurang Rp{sisa:,}. Silakan tambahkan.")
                elif sisa < 0:
                    print(f"✅ Pembayaran berhasil. Kembalian Anda: Rp{-sisa:,}")
                else:
                    print("✅ Pembayaran pas. Terima kasih.")
        else:
            print("✅ Tidak ada denda. Pengembalian tepat waktu.")

        # Tambah stok buku kembali
        for buku in self.buku_manager.data:
            if buku["judul"] == pinjam["judul_buku"]:
                buku["stok"] += 1
                break

        # Simpan ke riwayat
        self.riwayat.append({
            "nama_anggota": pinjam["nama_anggota"],
            "judul_buku": pinjam["judul_buku"],
            "tgl_pinjam": pinjam["tgl_pinjam"],
            "tgl_kembali_rencana": pinjam["tgl_kembali"],
            "tgl_dikembalikan": str(hari_ini),
            "terlambat_hari": terlambat,
            "denda": total_denda
        })

        # Hapus dari daftar pinjaman aktif
        del self.data[idx]
        self.buku_manager.simpan()
        self.simpan()

        print("✅ Buku berhasil dikembalikan dan dicatat di riwayat.")
        utils.pause()
