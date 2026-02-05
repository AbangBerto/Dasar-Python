# # 1. BUAT ALATNYA DULU (Define Functions)

# def tambah(angka1, angka2):
#     # Tugas: Jumlahkan angka1 dan angka2, lalu RETURN hasilnya
#     hasil = ... # isi titik-titik
#     return hasil

# def kurang(angka1, angka2):
#     # Tugas: Kurangi angka1 dengan angka2, lalu RETURN hasilnya
#     hasil = ... # isi titik-titik
#     return hasil

# # 2. PROGRAM UTAMA (Main Loop)
# print("--- KALKULATOR JARVIS ---")
# a = int(input("Angka pertama: "))
# b = int(input("Angka kedua: "))

# print("Pilih operasi: [1] Tambah  [2] Kurang")
# pilihan = input("Pilihan: ")

# if pilihan == "1":
#     # Panggil fungsi tambah, simpan di variabel 'skor'
#     skor = tambah(a, b) 
#     print(f"Hasil penjumlahan: {skor}")

# elif pilihan == "2":
#     # Tugas: Panggil fungsi kurang, simpan di variabel 'skor', lalu print
#     ... # Lanjutkan sendiri

# else:
#     print("Salah pilih.")


# 1. BUAT ALATNYA DULU (Define Functions)

#Jawaban

def tambah(angka1, angka2):
    # Tugas: Jumlahkan angka1 dan angka2, lalu RETURN hasilnya
    hasil = angka1 + angka2
    return hasil

def kurang(angka1, angka2):
    # Tugas: Kurangi angka1 dengan angka2, lalu RETURN hasilnya
    hasil = angka1 - angka2
    return hasil

# 2. PROGRAM UTAMA (Main Loop)
print("--- KALKULATOR JARVIS ---")
a = int(input("Angka pertama: "))
b = int(input("Angka kedua: "))

print("Pilih operasi: [1] Tambah  [2] Kurang")
pilihan = input("Pilihan: ")

if pilihan == "1":
    # Panggil fungsi tambah, simpan di variabel 'skor'
    skor = tambah(a, b) 
    print(f"Hasil penjumlahan: {skor}")

elif pilihan == "2":
    skor =kurang(a, b)
    print(f"Hasil pengurangan : {skor}")


else:
    print("Salah pilih.")