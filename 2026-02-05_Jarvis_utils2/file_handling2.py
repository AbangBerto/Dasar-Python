daftar_hadir = []

def baca_data_absensi():
    try:
        # Buka file mode baca ('r')
        with open("absensi.txt", "r") as file:
            semua_baris = file.readlines()
            for baris in semua_baris:
                # Masukkan ke list, hilangkan enter (\n) dengan strip()
                daftar_hadir.append(baris.strip())
    except FileNotFoundError:
        pass # Abaikan jika file belum ada

def tampilan_menu():
    print("\n=== APLIKASI ABSENSI ===")
    print("1. Catat Kehadiran")
    print("2. Lihat Siapa Yang Hadir")
    print("3. Hapus Kehadiran (Permanen)") 
    print("4. Keluar")

def catat_kehadiran():
    nama_siswa = input("Nama Siswa: ")
    daftar_hadir.append(nama_siswa) # Simpan di RAM
        
    # Simpan di File (Append/Tambah Bawah)
    with open("absensi.txt", "a") as file:
        file.write(nama_siswa + "\n")
    print(f"Sukses! {nama_siswa} hadir.")

def siswa_hadir():
    print("Siswa yang hadir:", daftar_hadir)

def hapus_kehadiran():
    nama_hapus = input("Nama Siswa yang dihapus: ")
    
    if nama_hapus in daftar_hadir:
        # 1. Hapus dari List (RAM)
        daftar_hadir.remove(nama_hapus)
        
        # 2. Hapus & Tulis Ulang File (Write Mode)
        with open("absensi.txt", "w") as file:
            for siswa in daftar_hadir:
                file.write(siswa + "\n")
        print(f"{nama_hapus} berhasil dihapus selamanya.")
    else: 
        print("Siswa tidak ditemukan.")

# --- PROGRAM UTAMA ---

# Load data lama saat program jalan pertama kali
baca_data_absensi() 

while True:
    tampilan_menu()
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        catat_kehadiran()

    elif pilihan == "2":
        siswa_hadir()

    elif pilihan == "3":
        hapus_kehadiran()

    elif pilihan == "4":
        print("Anda Keluar. Data aman tersimpan.")
        break

    else:
        print("Pilihan salah, masukkan 1-4.")