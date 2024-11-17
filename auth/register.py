import pwinput
import csv

# Membaca akun dari file CSV
def akun_baru():
    try:
        with open("akuns.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        return [["admin", "1234", "admin"]]  # Data default jika file belum ada

# Menyimpan akun ke file CSV
def simpan_akun():
    with open("akuns.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(akuns)

# Fungsi untuk registrasi akun
def register():
    print("\n==== Registrasi Akun User ====")
    username = input("Masukkan username baru: ")
    cek_akun = akun_baru()  # Mengambil list akun dari file
    akuna = False

    if not username:
        print("username tidak boleh kosong")
        return
    
    for akun in cek_akun:
        if akun[0] == username:
            akuna = True
            break
    if akuna:
        print("Username telah dipakai, silakan coba lagi")
    else:
        password = pwinput.pwinput("Masukkan password baru: ")
        if not password:
            print("password tidak boleh kosong")
            return
        
        akuns.append([username, password, "user"])
        simpan_akun()  # Menyimpan akun yang baru didaftarkan ke file CSV
        print(f"Akun Anda berhasil terdaftar dengan ID: {username}")

# Contoh penggunaan
akuns = akun_baru()  # Membaca akun yang sudah ada dari file saat program dijalankan


if __name__ == '__main__':
    register()
