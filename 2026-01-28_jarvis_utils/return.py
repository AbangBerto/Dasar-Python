def hitung_luas(panjang, lebar):
    hasil = panjang * lebar
    return hasil

luas_meja = hitung_luas(10, 5)
luas_tanah = hitung_luas(7, 10)

total = luas_meja + luas_tanah
print(f"Hasil dari perhitungan luas adalah {total}")

