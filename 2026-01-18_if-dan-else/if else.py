nama_ai = input ("Nama AI : ")
versi = float (input ("versi : "))
kecepatan = float (input("kecepatan : "))

print("Versi : " , versi)
print("Kecepatan : " , kecepatan)

versi_baru = versi + 1.0 
print("sedang menginstall pembaruan.....")
print("Versi AI anda sekarang menjadi : ", versi_baru)

print("-" * 20) #jangan bingung ini apa ini hanya spasi biar rapi 

if kecepatan > 100 :
    print("Bahaya! terlalu cepat hati-hati bisa overhead")

elif kecepatan < 80 : 
    print("Peringatan : Sistem berjalan lambat")
   
else  : 
    print("Sistem berjalan Optimal")