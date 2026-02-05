import os 
import operasi_hitung
import suara
import jarvis_listen

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

    suara.bicara("Mau hitung apa> Sialahkan biacara")
    print("\nSilakan bicara (Katakan: 'Satu', 'Tambah', atau 'Keluar')...")

    perintah_suara = jarvis_listen.dengarkan().lower()

    pilihan = ""

    # Cek apa yang diucapkan user
    if "satu" in perintah_suara or "tambah" in perintah_suara or "1" in perintah_suara:
        pilihan = "1"
    elif "dua" in perintah_suara or "kurang" in perintah_suara or "2" in perintah_suara:
        pilihan = "2"
    elif "tiga" in perintah_suara or "kali" in perintah_suara or "3" in perintah_suara:
        pilihan = "3"
    elif "empat" in perintah_suara or "bagi" in perintah_suara or "4" in perintah_suara:
        pilihan = "4"
    elif "lima" in perintah_suara or "keluar" in perintah_suara or "stop" in perintah_suara:
        pilihan = "5"
    else:
        # Kalau suara tidak jelas, kita fallback (cadangan) ke ketik manual
        suara.bicara("Maaf, saya tidak paham. Tolong ketik saja.")
        pilihan = input("Suara tidak dikenali. Masukkan pilihan (1-5): ")
        
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
        kalimat = f"Hasil dari {a} ditambah {b} adalah {hasil}"
        suara.bicara(kalimat)

    elif pilihan == "2":
        hasil = operasi_hitung.kurang(a,b)
        print(f"hasil {hasil}")
        kalimat = f"Hasil dari {a} dikurang {b} adalah {hasil}"
        suara.bicara(kalimat)
       
    elif pilihan == "3":
        hasil = operasi_hitung.kali(a,b)
        print(f"hasil {hasil}")
        kalimat = f"Hasil dari {a} dikali {b} adalah {hasil}"
        suara.bicara(kalimat)

    elif pilihan == "4":
        hasil = operasi_hitung.bagi(a,b)
        print(f"hasil {hasil}")
        kalimat = f"Hasil dari {a} dibagi {b} adalah {hasil}"
        suara.bicara(kalimat)

    else:
        print("Input tidak ditemukan mohon masukan 1-4")

    input("\nMau melanjutkan ENTER")

    