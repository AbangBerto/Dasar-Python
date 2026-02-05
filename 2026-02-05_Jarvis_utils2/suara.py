from gtts import gTTS
from playsound import playsound
import os 
import random


def bicara(teks):
    try :
        nama_file = f"suara_{random.randint(1, 1000)}.mp3"
        tts = gTTS(text=teks, lang='id')
        tts.save(nama_file)
        
        playsound(nama_file)
    
        os.remove(nama_file)

    except Exception as e:
        print("Jarvis Error (Cek Internet):", e)

if __name__ == "__main__":
    bicara("Tes modul suara Google siap digunakan.")
    



