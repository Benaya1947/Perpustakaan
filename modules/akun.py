# modules/akun.py
import os
from modules import utils

DATA_PATH = os.path.join("data", "akun.json")

class AkunManager:
    def __init__(self):
        # Load data akun dari file JSON (pakai dict)
        self.akun = utils.load_json(DATA_PATH, {})

    def simpan(self):
        """Simpan data akun ke file JSON."""
        utils.save_json(DATA_PATH, self.akun)

    def register(self):
        """Daftarkan akun baru."""
        utils.clear_screen()
        print("=== REGISTER AKUN BARU ===")
        username = utils.input_tidak_kosong("Username: ")

        if username in self.akun:
            print("⚠ Username sudah terdaftar!")
            utils.pause()
            return

        password = utils.input_tidak_kosong("Password: ")
        self.akun[username] = password
        self.simpan()
        print("✅ Akun berhasil dibuat!")
        utils.pause()

    def login(self):
        """Login akun dengan 3x percobaan."""
        percobaan = 3
        while percobaan > 0:
            utils.clear_screen()
            print("=== LOGIN ===")
            username = utils.input_tidak_kosong("Username: ")
            password = utils.input_tidak_kosong("Password: ")

            if username in self.akun and self.akun[username] == password:
                print(f"✅ Login berhasil! Selamat datang, {username}.")
                utils.pause()
                return True
            else:
                percobaan -= 1
                print(f"❌ Username atau password salah. Sisa percobaan: {percobaan}")
                utils.pause()

        print("🚪 Terlalu banyak percobaan gagal.")
        return False

    def lihat_semua(self):
        """Lihat semua akun terdaftar (username saja)."""
        utils.clear_screen()
        print("=== DAFTAR AKUN ===")
        if not self.akun:
            print("(Belum ada akun terdaftar)")
        else:
            for user in self.akun:
                print(f"- {user}")
        utils.pause()

    def edit_password(self):
        """Edit password akun."""
        utils.clear_screen()
        print("=== EDIT PASSWORD AKUN ===")
        username = utils.input_tidak_kosong("Username: ")

        if username not in self.akun:
            print("⚠ Username tidak ditemukan!")
            utils.pause()
            return

        password_lama = utils.input_tidak_kosong("Password lama: ")
        if self.akun[username] != password_lama:
            print("❌ Password lama salah.")
            utils.pause()
            return

        password_baru = utils.input_tidak_kosong("Password baru: ")
        self.akun[username] = password_baru
        self.simpan()
        print("✅ Password berhasil diubah!")
        utils.pause()

    def hapus_akun(self):
        """Hapus akun."""
        utils.clear_screen()
        print("=== HAPUS AKUN ===")
        username = utils.input_tidak_kosong("Username: ")

        if username not in self.akun:
            print("⚠ Username tidak ditemukan!")
            utils.pause()
            return

        konfirmasi = input(f"Yakin hapus akun '{username}'? (y/n): ").lower()
        if konfirmasi == "y":
            del self.akun[username]
            self.simpan()
            print("✅ Akun berhasil dihapus.")
        else:
            print("❌ Dibatalkan.")
        utils.pause()
