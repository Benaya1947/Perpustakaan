from modules.akun import AkunManager
from modules.buku import BukuManager
from modules.member import MemberManager
from modules.peminjaman import PeminjamanManager
from modules import utils

# Buat semua manager
akun_manager = AkunManager()
buku_manager = BukuManager()
member_manager = MemberManager()
peminjaman_manager = PeminjamanManager(buku_manager, member_manager)

# === MENU AKUN ===
def menu_akun():
    while True:
        utils.clear_screen()
        print("=== MENU AKUN ===")
        print("1. Register Akun")
        print("2. Login")
        print("3. Lihat Semua Akun")
        print("4. Edit Password")
        print("5. Hapus Akun")
        print("0. Kembali")

        pilihan = utils.input_pilihan("Pilih menu: ", [0, 1, 2, 3, 4, 5])

        if pilihan == 1:
            akun_manager.register()
        elif pilihan == 2:
            akun_manager.login()
        elif pilihan == 3:
            akun_manager.lihat_semua()
        elif pilihan == 4:
            akun_manager.edit_password()
        elif pilihan == 5:
            akun_manager.hapus_akun()
        elif pilihan == 0:
            break
        else:
            print("\n⚠ Pilihan tidak valid!")
            utils.pause()

# === MENU BUKU ===
def menu_buku():
    while True:
        utils.clear_screen()
        print("=== MENU BUKU ===")
        print("1. Lihat Semua Buku")
        print("2. Tambah Buku")
        print("3. Edit Buku")
        print("4. Hapus Buku")
        print("0. Kembali")

        pilihan = utils.input_pilihan("Pilih menu: ", [0, 1, 2, 3, 4])

        if pilihan == 1:
            buku_manager.lihat_semua()
        elif pilihan == 2:
            buku_manager.tambah()
        elif pilihan == 3:
            buku_manager.edit()
        elif pilihan == 4:
            buku_manager.hapus()
        elif pilihan == 0:
            break
        else:
            print("\n⚠ Pilihan tidak valid!")
            utils.pause()

# === MENU MEMBER ===
def menu_member():
    while True:
        utils.clear_screen()
        print("=== MENU MEMBER ===")
        print("1. Lihat Semua Member")
        print("2. Tambah Member")
        print("3. Edit Member")
        print("4. Hapus Member")
        print("0. Kembali")

        pilihan = utils.input_pilihan("Pilih menu: ", [0, 1, 2, 3, 4])

        if pilihan == 1:
            member_manager.lihat_semua()
        elif pilihan == 2:
            member_manager.tambah()
        elif pilihan == 3:
            member_manager.edit()
        elif pilihan == 4:
            member_manager.hapus()
        elif pilihan == 0:
            break
        else:
            print("\n⚠ Pilihan tidak valid!")
            utils.pause()

# === MENU PEMINJAMAN ===
def menu_peminjaman():
    while True:
        utils.clear_screen()
        print("=== MENU PEMINJAMAN ===")
        print("1. Pinjam Buku")
        print("2. Kembalikan Buku")
        print("3. Lihat Peminjaman Aktif")
        print("4. Lihat Riwayat Peminjaman")
        print("0. Kembali")

        pilihan = utils.input_pilihan("Pilih menu: ", [0, 1, 2, 3, 4])

        if pilihan == 1:
            peminjaman_manager.pinjam_buku()
        elif pilihan == 2:
            peminjaman_manager.kembalikan_buku()
        elif pilihan == 3:
            peminjaman_manager.lihat_semua()
        elif pilihan == 4:
            peminjaman_manager.lihat_riwayat()
        elif pilihan == 0:
            break


# === MAIN PROGRAM ===
def main():
    # LOGIN WAJIB SEBELUM MASUK
    # percobaan = 3
    # while percobaan > 0:
    #     utils.clear_screen()
    #     print("=== LOGIN ADMIN ===")
    #     username = utils.input_tidak_kosong("Username: ")
    #     password = utils.input_tidak_kosong("Password: ")

    #     if username in akun_manager.akun and akun_manager.akun[username] == password:
    #         print(f"✅ Login berhasil! Selamat datang, {username}.")
    #         utils.pause()
    #         break
    #     else:
    #         percobaan -= 1
    #         print(f"❌ Username atau password salah. Sisa percobaan: {percobaan}")
    #         utils.pause()

    # if percobaan == 0:
    #     print("🚪 Terlalu banyak percobaan gagal. Program keluar.")
    #     return

    # MENU UTAMA
    while True:
        utils.clear_screen()
        print("=== SISTEM PERPUSTAKAAN MODULAR ===")
        print("1. Menu Akun")
        print("2. Menu Buku")
        print("3. Menu Member")
        print("4. Menu Peminjaman")
        print("5. Keluar")

        pilihan = utils.input_pilihan("Pilih menu: ", [0, 1, 2, 3, 4, 5])


        if pilihan == 1:
            menu_akun()
        elif pilihan == 2:
            menu_buku()
        elif pilihan == 3:
            menu_member()
        elif pilihan == 4:
            menu_peminjaman()
        elif pilihan == 5:
            print("Terima kasih sudah menggunakan program ini!")
            break
        else:
            print("\n⚠ Pilihan tidak valid!")
            utils.pause()

if __name__ == "__main__":
    main()