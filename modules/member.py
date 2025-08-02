import os
from modules import utils

DATA_PATH = os.path.join("data", "member.json")

class MemberManager:
    def __init__(self):
        # Load data member dari file JSON
        self.data = utils.load_json(DATA_PATH, [])

    def simpan(self):
        """Simpan data member ke file JSON."""
        utils.save_json(DATA_PATH, self.data)

    def lihat_semua(self):
        """Menampilkan semua anggota perpustakaan."""
        utils.clear_screen()
        print("=== DAFTAR ANGGOTA PERPUSTAKAAN ===")
        if not self.data:
            print("(Belum ada data anggota)")
        else:
            for i, anggota in enumerate(self.data, start=1):
                print(f"{i}. ID: {anggota['id']}")
                print(f"   Nama: {anggota['nama']}")
                print(f"   Nomor HP: {anggota['hp']}")
                print(f"   Alamat: {anggota['alamat']}")
                print("-" * 30)
        utils.pause()

    def tambah(self):
        """Menambah member baru (tidak boleh ID duplikat)."""
        utils.clear_screen()
        print("=== TAMBAH MEMBER ===")
        member_id = utils.input_tidak_kosong("ID Member: ").strip().lower()

        # Cek apakah ID sudah ada
        for m in self.data:
            if m.get("id", "").strip().lower() == member_id:
                print("⚠ Member dengan ID ini sudah terdaftar!")
                utils.pause()
                return

        nama = utils.input_tidak_kosong("Nama: ")
        hp = utils.input_tidak_kosong("Nomor HP: ")
        alamat = utils.input_tidak_kosong("Alamat: ")

        self.data.append({
            "id": member_id,  # simpan sudah dalam format lower
            "nama": nama,
            "hp": hp,
            "alamat": alamat
        })
        self.simpan()
        print("✅ Member berhasil ditambahkan!")
        utils.pause()


    def edit(self):
        """Mengedit data anggota."""
        utils.clear_screen()
        print("=== EDIT ANGGOTA PERPUSTAKAAN ===")
        self.lihat_semua()

        if not self.data:
            return

        index = utils.input_angka("Masukkan nomor anggota yang ingin diedit: ") - 1
        if 0 <= index < len(self.data):
            id_anggota = utils.input_tidak_kosong("ID Anggota baru: ")
            nama = utils.input_tidak_kosong("Nama baru: ")
            hp = utils.input_tidak_kosong("Nomor HP baru: ")
            alamat = utils.input_tidak_kosong("Alamat baru: ")

            self.data[index] = {
                "id": id_anggota,
                "nama": nama,
                "hp": hp,
                "alamat": alamat
            }
            self.simpan()
            print("✅ Data anggota berhasil diubah!")
        else:
            print("⚠ Nomor anggota tidak valid.")
        utils.pause()

    def hapus(self):
        """Menghapus data anggota."""
        utils.clear_screen()
        print("=== HAPUS ANGGOTA PERPUSTAKAAN ===")
        self.lihat_semua()

        if not self.data:
            return

        index = utils.input_angka("Masukkan nomor anggota yang ingin dihapus: ") - 1
        if 0 <= index < len(self.data):
            konfirmasi = input(f"Yakin ingin menghapus anggota '{self.data[index]['nama']}'? (y/n): ").lower()
            if konfirmasi == "y":
                del self.data[index]
                self.simpan()
                print("✅ Anggota berhasil dihapus.")
            else:
                print("❌ Dibatalkan.")
        else:
            print("⚠ Nomor anggota tidak valid.")
        utils.pause()
