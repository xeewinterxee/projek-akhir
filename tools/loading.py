import time
import sys

def loading_efek():
    for i in range(3):  # Melakukan iterasi sebanyak 3 kali
        sys.stdout.write("Loading" + "." * (i + 1))  # Tampilkan "Loading", titiknya bertambah
        sys.stdout.flush()  # Memastikan bahwa output langsung ditampilkan
        time.sleep(0.5)  # Delay selama 0.5 detik
        sys.stdout.write("\r")  # Menghapus teks sebelumnya (menggantinya dengan baris baru)
    
    print("Kembali ke menu utama!")  # Setelah selesai, tampilkan "Done!"

if __name__ == "__main__":
    loading_efek()
