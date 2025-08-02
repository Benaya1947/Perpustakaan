import os
from modules import utils

DATA_PATH = os.path.join("data", "buku.json")

class BukuManager:
    def __init__(self):
        # Load data buku dari file JSON
        self.data = utils.load_json(DATA_PATH, [])

        # Pastikan semua buku punya stok
        for b in self.data:
            if "stok" not in b:
                b["stok"] = 1  # default stok 1 buku


    def simpan(self):
        """Simpan data buku ke file JSON."""
        utils.save_json(DATA_PATH, self.data)

    def lihat_semua(self):
        utils.clear_screen()
        print("=== DAFTAR BUKU PERPUSTAKAAN ===")
        if not self.data:
            print("(Belum ada data buku)")
        else:
            for i, buku in enumerate(self.data, start=1):
                print(f"{i}. Judul : {buku['judul']}")
                print(f"   Penulis : {buku['penulis']}")
                print(f"   Tahun : {buku['tahun']}")
                print(f"   Stok : {buku.get('stok', 0)}")  # ← tambahin ini
                print("-" * 30)
        utils.pause()


    def tambah(self):
        """Menambah buku baru (tidak boleh duplikat)."""
        utils.clear_screen()
        print("=== TAMBAH BUKU ===")
        judul = utils.input_tidak_kosong("Judul buku: ")

        # Cek duplikat berdasarkan judul
        for buku in self.data:
            if buku["judul"].lower() == judul.lower():
                print("⚠ Buku ini sudah ada di daftar!")
                utils.pause()
                return

        penulis = utils.input_tidak_kosong("Penulis: ")
        tahun = utils.input_angka("Tahun terbit: ")

        self.data.append({
            "judul": judul,
            "penulis": penulis,
            "tahun": tahun
        })
        self.simpan()
        print("✅ Buku berhasil ditambahkan!")
        utils.pause()


    def edit(self):
        """Mengedit data buku."""
        utils.clear_screen()
        print("=== EDIT DATA BUKU ===")
        self.lihat_semua()
        if not self.data:
            return

        index = utils.input_angka("Masukkan nomor buku yang ingin diedit: ") - 1
        if 0 <= index < len(self.data):
            judul = utils.input_tidak_kosong("Judul baru: ")
            penulis = utils.input_tidak_kosong("Penulis baru: ")
            tahun = utils.input_angka("Tahun baru: ")

            self.data[index] = {
                "judul": judul,
                "penulis": penulis,
                "tahun": tahun
            }
            self.simpan()
            print("✅ Data buku berhasil diubah!")
        else:
            print("⚠ Nomor buku tidak valid.")
        utils.pause()

    def hapus(self):
        """Menghapus buku."""
        utils.clear_screen()
        print("=== HAPUS DATA BUKU ===")
        self.lihat_semua()
        if not self.data:
            return

        index = utils.input_angka("Masukkan nomor buku yang ingin dihapus: ") - 1
        if 0 <= index < len(self.data):
            konfirmasi = input(f"Yakin ingin menghapus buku '{self.data[index]['judul']}'? (y/n): ").lower()
            if konfirmasi == "y":
                del self.data[index]
                self.simpan()
                print("✅ Buku berhasil dihapus.")
            else:
                print("❌ Dibatalkan.")
        else:
            print("⚠ Nomor buku tidak valid.")
        utils.pause()
