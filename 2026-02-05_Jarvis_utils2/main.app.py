import os 
import operasi_hitung

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    bersihkan_layar()
    print("=== Jarvis Modular Calculator Tekan Angka Oprasi Hitung ====")
    print("1. Tambah + ")
    print("2. Kurang - ")
    print("3. Kali x ")
    print("4. bagi / ")
    print("5. Keluar ")
        
    pilihan = input("Masukan pilihan anda :")
    if pilihan == "5":
        print("Anda berhasil keluar")
        break


    try:
        a = int(input("Angka 1 : "))
        b = int(input("Angka 2 : "))

    except ValueError:
        print("Harus angka bos")
        input("Tekan Enter untuk lanjut...")
        continue

    if pilihan == "1" :
        hasil = operasi_hitung.tambah(a,b)
        print(f"hasil {hasil}")

    elif pilihan == "2":
        hasil = operasi_hitung.kurang(a,b)
        print(f"hasil {hasil}")

    elif pilihan == "3":
        hasil = operasi_hitung.kali(a,b)
        print(f"hasil {hasil}")

    elif pilihan == "4":
        hasil = operasi_hitung.bagi(a,b)
        print(f"hasil {hasil}")

    else:
        print("Input tidak ditemukan mohon masukan 1-4")

    input("\nMau melanjutkan ENTER")

    