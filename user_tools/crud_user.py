import csv
import os
from datetime import datetime,  timedelta
from prettytable import PrettyTable

gudang = os.path.join(os.path.dirname(__file__), '..', 'gudang.csv')


def lihat_barang():
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

# def peminjaman_barang():
#     lihat_barang()
#     id_barang = input("Masukkan ID Barang: ")
#     barang = False
#     with open(gudang, mode="r", newline='', encoding="utf-8") as file:
#         read = csv.DictReader(file)
#         for row in read:
#             if row["ID"] == id_barang:
#                 barang = True
#                 nama_user = input("Masukkan nama baru: ").capitalize()
#                 stok_user = input("Masukkan stok baru: ")
#                 jumlah_hari = int(input("Masukkan jumlah hari peminjaman: "))
#                 tanggal_peminjaman = datetime.now()
#                 print("Tanggal peminjaman:", tanggal_peminjaman.strftime("%Y-%m-%d"))
#                 tanggal_pengembalian = tanggal_peminjaman + timedelta(days=jumlah_hari)
#                 print("Tanggal pengembalian:", tanggal_pengembalian.strftime("%Y-%m-%d"))

#                 row["nama"] = nama_user
#                 row["id barang"] = id_barang
#                 row["stok_user"] = stok_user
#                 row["waktu awal minjam"] = tanggal_peminjaman
#                 row["waktu akhir minjam"] = tanggal_pengembalian
#                 print(f"Data barang dengan id:{id_barang} berhasil dipinjam.")
#                 break
            
#         if barang:   
#             with open('riwayat.csv','a',newline='') as file:
#                 fieldname = ["nama","id barang","stok","waktu awal minjam","waktu akhir peminjaman"]
#                 writer = csv.DictWriter(file,fieldnames=fieldname)
#                 writer.writerow(row)
#             print(f"Data {id_barang} berhasil diperbarui.")
#         else:
#             print(f"Barang dengan id:{id_barang} tidak ditemukan.")

import csv
from datetime import datetime, timedelta

def peminjaman_barang():
    lihat_barang()  # Pastikan fungsi ini didefinisikan
    id_barang = input("Masukkan ID Barang: ")
    barang_ditemukan = False
    riwayat_row = None
    
    # Membaca data dari file gudang
    with open('gudang.csv', mode="r", newline='', encoding="utf-8") as file:
        read = csv.DictReader(file)
        rows = list(read)
        
        for row in rows:
            if row["ID"] == id_barang:
                barang_ditemukan = True
                nama_user = input("Masukkan nama baru: ").capitalize()
                try:   
                    stok_user = int(input("Berapa stok yang ingin dipinjam(maks 10): "))
                    if 0 < stok_user <= 10 :
                        jumlah_hari = int(input("Masukkan jumlah hari peminjaman: "))
                        tanggal_peminjaman = datetime.now()
                        print("Tanggal peminjaman:", tanggal_peminjaman.strftime("%Y-%m-%d"))
                        tanggal_pengembalian = tanggal_peminjaman + timedelta(days=jumlah_hari)
                        print("Tanggal pengembalian:", tanggal_pengembalian.strftime("%Y-%m-%d"))
                        
                        # Menambahkan data peminjaman ke dalam row baru untuk riwayat
                        riwayat_row = {
                            "nama": nama_user,
                            "id barang": id_barang,
                            "stok": stok_user,
                            "waktu awal minjam": tanggal_peminjaman.strftime("%Y-%m-%d"),
                            "waktu akhir peminjaman": tanggal_pengembalian.strftime("%Y-%m-%d")
                        }
                        
                        print(f"Data barang dengan ID: {id_barang} berhasil dipinjam.")
                        break
                    if barang_ditemukan:
                        # Menambahkan data ke riwayat.csv
                        with open('riwayat.csv', 'a', newline='', encoding="utf-8") as file:
                            fieldnames = ["nama", "id barang", "stok", "waktu awal minjam", "waktu akhir peminjaman"]
                            writer = csv.DictWriter(file, fieldnames=fieldnames)
                            writer.writerow(riwayat_row)
                        
                            print(f"Data {id_barang} berhasil diperbarui.")
                    else:
                        print(f"Barang dengan ID: {id_barang} tidak ditemukan.")

                except ValueError:
                    print("input tidak valid, harus berupa angka")
                except ValueError:
                    print("Peminjaman barang tidak boleh melebihi 7 stok")
                
import csv
from datetime import datetime, timedelta

def peminjaman_barang():
    lihat_barang()  # Pastikan fungsi ini didefinisikan
    id_barang = input("Masukkan ID Barang: ")
    barang_ditemukan = False
    riwayat_row = None

    # Membaca data dari file gudang
    with open('gudang.csv', mode="r", newline='', encoding="utf-8") as file:
        read = csv.DictReader(file)
        rows = list(read)

        for row in rows:
            if row["ID"] == id_barang:
                barang_ditemukan = True
                nama_user = input("Masukkan nama baru: ").capitalize()

                try:
                    stok_user = int(input("Berapa stok yang ingin dipinjam (maks 10): "))
                    if 0 < stok_user <= 10:
                        jumlah_hari = int(input("Masukkan jumlah hari peminjaman: "))
                        tanggal_peminjaman = datetime.now()
                        print("Tanggal peminjaman:", tanggal_peminjaman.strftime("%Y-%m-%d"))
                        tanggal_pengembalian = tanggal_peminjaman + timedelta(days=jumlah_hari)
                        print("Tanggal pengembalian:", tanggal_pengembalian.strftime("%Y-%m-%d"))

                        # Menambahkan data peminjaman ke dalam row baru untuk riwayat
                        riwayat_row = {
                            "nama": nama_user,
                            "id barang": id_barang,
                            "stok": stok_user,
                            "waktu awal minjam": tanggal_peminjaman.strftime("%Y-%m-%d"),
                            "waktu akhir peminjaman": tanggal_pengembalian.strftime("%Y-%m-%d")
                        }

                        # Menambahkan data ke riwayat.csv jika barang ditemukan
                        with open('riwayat.csv', 'a', newline='', encoding="utf-8") as file_riwayat:
                            fieldnames = ["nama", "id barang", "stok", "waktu awal minjam", "waktu akhir peminjaman"]
                            writer = csv.DictWriter(file_riwayat, fieldnames=fieldnames)
                            writer.writerow(riwayat_row)

                        print(f"Data barang dengan ID: {id_barang} berhasil dipinjam.")
                        break

                    else:
                        print("Peminjaman barang tidak boleh melebihi 10 stok")

                except ValueError:
                    print("Input tidak valid, harus berupa angka")
                    
    if not barang_ditemukan:
        print(f"Barang dengan ID: {id_barang} tidak ditemukan.")

if __name__ == "__main__":
    lihat_barang()
    peminjaman_barang()