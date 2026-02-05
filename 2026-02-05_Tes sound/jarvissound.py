from gtts import gTTS  #import gtts dari goole translate 
from playsound import playsound #import playsound untuk memutar suara


pesan = "Reza adalah anak yang mempunyai banyak gantungan kunci" # variabel pesan text yang akan dipakai
bahasa = "id" # kode bahasa yang akan digunakan id (indonesia)

suara_goole =gTTS (text=pesan, lang = bahasa, slow = False) # code ini dipakai untuk text pesan tadi menjadi suara dengan bhasa indonesia dan kecepatan standar 
nama_file = "i33.mp3" # meyimpan suara dengan format mp3
suara_goole.save(nama_file)

print("putar lagu")
playsound(nama_file) # memutar suara