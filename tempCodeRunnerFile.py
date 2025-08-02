percobaan = 3
    while percobaan > 0:
        utils.clear_screen()
        print("=== LOGIN ADMIN ===")
        username = utils.input_tidak_kosong("Username: ")
        password = utils.input_tidak_kosong("Password: ")

        if username in akun_manager.akun and akun_manager.akun[username] == password:
            print(f"✅ Login berhasil! Selamat datang, {username}.")
            utils.pause()
            break
        else:
            percobaan -= 1
            print(f"❌ Username atau password salah. Sisa percobaan: {percobaan}")
            utils.pause()

    if percobaan == 0:
        print("🚪 Terlalu banyak percobaan gagal. Program keluar.")
        return
