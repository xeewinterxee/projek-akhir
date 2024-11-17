from tools import loading
import pwinput
import os
from admin_tools import crud_admin
from user_tools import crud_user
import main
from auth import register

akuns = register.akun_baru()

# start login
def login():
    try:
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
                        crud_admin.tambah_barang()
                    elif opsi == 2:
                        crud_admin.lihat_barang()
                    elif opsi == 3:
                        crud_admin.update_barang()
                    elif opsi == 4:
                        crud_admin.hapus_barang()
                    elif opsi == 5:
                        crud_admin.riwayat_barang()
                    elif opsi == 6:
                        print("Keluar dari menu admin")
                        loading.loading_efek()
                        os.system('cls || clear')
                        main.menu()
                        break
                
            elif akun[0] == username and akun[1] == password and akun[2] == "user":
                print("Berhasil login sebagai user")
                loading.loading_efek()
                os.system('cls || clear')
                while True:
                    print("\nMenu User\n1. Lihat Barang\n2. Peminjaman Barang\n3. Keluar ke menu utama")
                    opsi = int(input("Pilih opsi: "))
                    if opsi == 1:
                        crud_user.lihat_barang()      
                    elif opsi == 2:
                        crud_user.peminjaman_barang()
                    elif opsi == 3:
                        main.menu()
                        break
        print("username atau password anda salah,silahkan coba lagi")
    except ModuleNotFoundError:
        print("Modul tidak ketemu")

# end login

if __name__ == '__main__':
    login()