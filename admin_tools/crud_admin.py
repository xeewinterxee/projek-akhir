import csv
from prettytable import PrettyTable
import os

gudang = os.path.join(os.path.dirname(__file__), '..', 'gudang.csv')
riwayat = os.path.join(os.path.dirname(__file__), '..', 'riwayat.csv')

def tambah_barang():
    try:
        nama_barang = input("Masukkan nama barang: ").capitalize()
        tipe_barang = input("Masukkan tipe barang: ")
        stok_barang = int(input("Masukkan stok barang: "))
        id_barang   = input("Masukkan id barang: ")

        if not nama_barang or not tipe_barang or not id_barang:
            raise ValueError("input valid tidak boleh kosong")

    except ValueError:
        print("input harus berupa angka")
    except KeyboardInterrupt:
        print("input dibatalkan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

    else:
        with open(gudang, mode="a", newline='', encoding="utf-8") as file:
                fieldnames = ["nama barang", "tipe barang", "stok barang","id"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                writer.writerow({
                    "nama barang": nama_barang, 
                    "tipe barang": tipe_barang, 
                    "stok barang": stok_barang,
                    "id"         : id_barang  
                })
                print(f"Data {nama_barang} berhasil ditambahkan dengan id:{id_barang}.")

def lihat_barang():
    try:
        with open(gudang, mode="r", newline='', encoding="utf-8") as file:
            csvreader = csv.DictReader(file)
            data = list(csvreader)

            if data:
                table = PrettyTable()
                table.field_names = data[0].keys()

                for row in data:
                    table.add_row(row.values())
                    print(table)
            else:
                print("\nData kosong.")
            
    except FileNotFoundError:
        print("File tidak ditemukan, buat data baru terlebih dahulu.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


def update_barang():
    id_barang = input("Masukkan id barang yang ingin diubah: ")
    barang = False
    with open(gudang, mode="r", newline='', encoding="utf-8") as file:
        read = csv.DictReader(file)
        for row in read:
            if row["ID"] == id_barang:
                barang = True
                print(f"Barang ditemukan: {row['nama_barang']}, {row['tipe_barang']}, {row['stok_barang']}")
                nama_baru = input("Masukkan nama baru: ").capitalize()
                tipe_baru = input("Masukkan tipe baru: ")
                stok_baru = input("Masukkan stok baru: ")
                row["nama barang"] = nama_baru
                row["tipe_barang"] = tipe_baru
                row["stok_barang"] = stok_baru
                print(f"Data barang dengan id:{id_barang} berhasil diperbarui.")
                break
    
        if barang:           
            # Menyimpan data yang telah diperbarui ke dalam CSV
            with open("gudang", mode="w", newline='', encoding="utf-8") as file:
                fieldnames = ["nama barang", "tipe barang", "stok barang","id"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(read)
                
            print(f"Data {id_barang} berhasil diperbarui.")
        else:
            print(f"Barang dengan id:{id_barang} tidak ditemukan.")

                
def hapus_barang():
    try:
        hapus_barang = input("Masukkan ID Barang: ").strip()
        if not hapus_barang:
            raise ValueError("ID barang tidak boleh kosong.")
        
        barang_dihapus = False 

        with open(gudang, 'r', newline='', encoding="utf-8") as file:
            read = csv.DictReader(file)
            data_barang = [row for row in read]

        with open(gudang, 'w', newline='', encoding="utf-8") as file:
            fieldnames = ["nama barang", "tipe barang", "stok barang", "id"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            for row in data_barang:
                if row["id"] != hapus_barang:
                    writer.writerow(row)
                else:
                    barang_dihapus = True

        if barang_dihapus:
            print(f"Barang dengan ID {hapus_barang} berhasil dihapus.")
        else:
            print(f"Barang dengan ID {hapus_barang} tidak ditemukan.")
    
    except ValueError as e:
        print(f"error: {e}")



def riwayat_barang():
    try:
        with open(riwayat,'r',newline='',encoding='utf-8') as file:
            baca = csv.DictReader(file)
            data = list(baca)

            if data:
                table = PrettyTable()
                table.field_names = data[0].keys()

                for row in data:
                    table.add_row(row.values())
                print(table)
            else:
                print("\nData kosong.")
            
    except FileNotFoundError:
        print("File tidak ditemukan, buat data baru terlebih dahulu.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == '__main__':
    tambah_barang()
    lihat_barang()
    update_barang()
    hapus_barang()
    riwayat_barang()