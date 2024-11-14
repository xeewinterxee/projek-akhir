import csv
import os
from tools import loading
import pwinput
from prettytable import PrettyTable

# file ekstra
csv_file = 'gudang.csv'

# Variabel global menggunakan list
akuns = [["admin","1234","admin"]]


# start register
def register():
    print("\n==== Registrasi Akun User ====")
    username = input("Masukkan username baru: ")
    akuna = False
    for akun in akuns:
        if akun[0] == username:
            akuna = True
            break
    if akuna:
        print("Username telah dipakai,silahkan coba lagi")
    else:
        password = pwinput.pwinput("Masukkan password baru: ")
        akuns.append([username,password,"user",])
        print(f"Akun Anda berhasil terdaftar dengan ID: {username}")
# end register

# start login
def login():
    print("\n==== Login ====")
    username = input("Masukkan username: ")
    password = pwinput.pwinput("Masukkan password: ")
    
    for akun in akuns:
        if akun[0] == username and akun[1] == password and akun[2] == "admin":
            print("Berhasil login sebagai admin")
            loading.loading_efek()
            os.system('cls || clear')
            while True:
                print("\nKhusus ADMIN\n1. Tambah Alat\n2. Lihat Alat\n3. Update Alat\n4. Hapus Alat\n5. Riwayat Peminjaman\n6. Keluar ke menu utama")
                opsi = int(input("Pilih opsi: "))
                if opsi == 1:
                    tambah_alat_admin()
                elif opsi == 2:
                    lihat_alat_admin()
                elif opsi == 3:
                    update_alat_admin()
                elif opsi == 4:
                    hapus_alat_admin()
                elif opsi == 5:
                    riwayat_peminjaman_admin()
                elif opsi == 6:
                    print("Keluar dari menu admin")
                    loading.loading_efek()
                    os.system('cls || clear')
                    menu()
                    break
        elif akun[0] == username and akun[1] == password and akun[2] == "user":
            print("Berhasil login sebagai user")
            loading.loading_efek()
            os.system('cls || clear')
            while True:
                print("\nMenu User\n1. Tambah Alat\n2. Lihat Alat\n3. Riwayat\n4. Keluar ke menu utama")
                opsi = int(input("Pilih opsi: "))
                if opsi == 1:
                   tambah_alat_user()
                elif opsi == 2:
                    lihat_alat_user()
                elif opsi == 3:
                    riwayat_peminjaman_user()
                elif opsi == 4:
                    menu()
                    break
    print("username atau password anda salah,silahkan coba lagi")

# end login




# start fitur



# fitur admin
def tambah_alat_admin():
    nama_barang = input("Masukkan nama barang: ")
    tipe_barang = input("Masukkan tipe barang: ")
    stok_barang = input("Masukkan stok barang: ")
    with open("gudang.csv", mode="a", newline="") as file:
            fieldnames = ["nomor", "nama_barang", "tipe_barang", "stok_barang"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writerow({
                "nama_barang": nama_barang, 
                "tipe_barang": tipe_barang, 
                "stok_barang": stok_barang
            })
            print(f"Data {nama_barang} berhasil ditambahkan.")

def lihat_alat_admin():
    try:
        with open("gudang.csv", mode="r", newline="") as file:
            csvreader = csv.DictReader(file)
            data = list(csvreader)
            if data:
                table = PrettyTable()
                table.field_names = data[0].keys()
            else:
                print("\nData kosong.")
            for row in data:
                table.add_row(row.values())
            print(table)
    except FileNotFoundError:
        print("File tidak ditemukan, buat data baru terlebih dahulu.")


def update_alat_admin():
    nama_barang = input("Masukkan nama barang yang ingin diubah: ")
    barang = False
    with open("gudang.csv", "r", newline="") as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            if row["nama_barang"] == nama_barang:
                barang = True
                print(f"Barang ditemukan: {row['nama_barang']}, {row['tipe_barang']}, {row['stok_barang']}")
                tipe_baru = input("Masukkan tipe baru: ")
                stok_baru = input("Masukkan stok baru: ")
                row["tipe_barang"] = tipe_baru
                row["stok_barang"] = stok_baru
            
            
                writer.writerows(row)
    
    if barang:
        # Menyimpan data yang telah diperbarui ke dalam CSV
        with open("gudang.csv", "w", newline="") as file:
            fieldnames = ["nomor", "nama_barang", "tipe_barang", "stok_barang"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows()
            
        print(f"Data {nama_barang} berhasil diperbarui.")
    else:
        print(f"Barang dengan nama {nama_barang} tidak ditemukan.")

                
def hapus_alat_admin():
    pass

def riwayat_peminjaman_admin():
    pass

# fitur user
def tambah_alat_user():
    pass

def lihat_alat_user():
    pass

def riwayat_peminjaman_user():
    pass

# end fitur



# start menu
def menu():
    while True:
        print("\nSelamat Datang di E-GUDANG ELEKTRONIK\n 1.register\n 2.Login\n 3.Exit ")
        try:
            opsi = int(input("\nPilih opsi: "))
            os.system('cls || clear')
            if opsi == 1:
                register()
                input("Tekan enter untuk kembali ke menu utama")
                loading.loading_efek()
                os.system('cls || clear')
            elif opsi == 2:
                login()
                loading.loading_efek()
                os.system('cls || clear')
            elif opsi == 3:
                print("Terima kasih telah mengunjungi E-GUDANG\nProgram akan keluar")
                loading.loading_efek()
                os.system('cls || clear')
                break
            else:
                print("Opsi tidak valid. Silakan pilih 1,2 dan 3")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
# end menu



if __name__ == "__main__":
    menu()
