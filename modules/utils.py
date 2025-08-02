import os
import json

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nTekan Enter untuk melanjutkan...")

def load_json(path, default):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return default
    except json.JSONDecodeError:
        return default

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def input_tidak_kosong(prompt):
    while True:
        data = input(prompt).strip()
        if data:
            return data
        print("\n⚠ Input tidak boleh kosong!")

def input_angka(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("\n⚠ Masukkan angka yang benar!")

def input_pilihan(prompt, pilihan_valid):
    while True:
        try:
            angka = int(input(prompt))
            if angka in pilihan_valid:
                return angka
            else:
                print(f"\n⚠ Pilihan tidak valid! \nPilihan harus salah satu dari {pilihan_valid}!\n")
        except ValueError:
            print("\n⚠ Masukkan angka yang benar!")
