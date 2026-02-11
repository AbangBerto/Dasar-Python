import os
import webbrowser
import datetime
import wikipedia
import pywhatkit 

wikipedia.set_lang("Id")

def eksekusi_perintah(perintah):
    perintah = perintah.lower()

  
    if "jam berapa" in perintah or "waktu" in perintah:
        waktu = datetime.datetime.now().strftime("%H:%M")
        return f"Sekarang jam {waktu}" # Kembalikan teks untuk diucapkan

    elif "tanggal berapa" in perintah or "hari apa" in perintah:
        tanggal = datetime.datetime.now().strftime("%A, %d %B %Y")
        return f"Sekarang adalah {tanggal}"

  
    elif "buka youtube" in perintah:
        webbrowser.open("https://www.youtube.com")
        return "Siap, membuka YouTube."
        
    elif "buka google" in perintah:
        webbrowser.open("https://www.google.com")
        return "Membuka Google."
    
    elif "putar" in perintah or "mainkan" in perintah:
        lagu = perintah.replace("putar", "").replace("mainkan", "")
        pywhatkit.playonyt(lagu)
        return f"Siap, memutar {lagu}."

    elif "buka notepad" in perintah:
        os.system("notepad") 
        return "Notepad sudah dibuka."
        
    elif "buka kalkulator" in perintah:
        os.system("calc")
        return "Kalkulator sistem dibuka."
    
    elif "cari" in perintah or "siapa" in perintah or "apa itu" in perintah:
        
        topik = perintah.replace("cari", "").replace("siapa", "").replace("apa itu", "")
        
        try:
            hasil = wikipedia.summary(topik, sentences=2)
            return hasil
        except:
            return "Maaf bos, saya tidak menemukan informasi itu."

    else:
        return False