import suara           # Mulut
import jarvis_listen   # Telinga
import kontrol_laptop  
import operasi_hitung 
import os
        

def bersihkan():
    os.system('cls' if os.name == 'nt' else 'clear')

def mulai_jarvis():
    bersihkan()
    print("=== JARVIS ULTIMATE SYSTEM ===")
    print("Silakan bicara...")
    
    suara.bicara("Sistem online. Saya siap melayani.")

    while True:
        print("\nMenunggu perintah...")
        perintah = jarvis_listen.dengarkan()
        
        if perintah == "":
            continue
            
        print(f"Perintah: {perintah}")

        
        if "keluar" in perintah or "matikan" in perintah or "stop" in perintah:
            suara.bicara("Baik bos. Sistem dimatikan.")
            break

        hasil_kontrol = kontrol_laptop.eksekusi_perintah(perintah)
        
        if hasil_kontrol != False:
            print(f"Jarvis: {hasil_kontrol}")
            suara.bicara(hasil_kontrol)
            continue 

        if "hitung" in perintah or "kalkulator" in perintah:
            suara.bicara("Mode kalkulator aktif. Mau tambah, kurang, kali, atau bagi?")
            
           
            sub_perintah = jarvis_listen.dengarkan()
            
            if "tambah" in sub_perintah:
                suara.bicara("Masukkan angka di keyboard.")
                try:
                    a = int(input("Angka 1: "))
                    b = int(input("Angka 2: "))
                    hasil = operasi_hitung.tambah(a, b)
                    suara.bicara(f"Hasilnya adalah {hasil}")
                except:
                    suara.bicara("Error input angka.")
            
            elif "kurang" in sub_perintah:
                
                suara.bicara("Fitur kurang siap.")
            
            else:
                suara.bicara("Saya tidak dengar mau hitung apa.")
            
            continue

        
        suara.bicara("Maaf bos, saya belum mengerti perintah itu.")

if __name__ == "__main__":
    mulai_jarvis()