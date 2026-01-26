from gtts import gTTS
import playsound
import os


def bicara(teks):
    print(f"Jarvis: {teks}") 
    
    tts = gTTS(text=teks, lang='id', slow=False)
    
  
    nama_file = "suara_jarvis.mp3"
    tts.save(nama_file)
    
   
    playsound.playsound(nama_file)
    
 
    os.remove(nama_file)


print("--- JARVIS VERSI GOOGLE ---")

bicara("Hai BOS!")
bicara("Saya siap melayani")
bicara("Apa yang anda butuhkan?")