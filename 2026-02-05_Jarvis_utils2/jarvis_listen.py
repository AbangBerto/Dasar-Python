import speech_recognition as sr

def dengarkan():
    # 1. Panggil alat pendengarnya
    telinga = sr.Recognizer()
    
    # 2. Buka Microphone
    with sr.Microphone() as sumber_suara:
        print("Mendengarkan... (Silakan bicara)")
        
        # Kalibrasi noise (agar suara kipas laptop tidak dianggap suara manusia)
        telinga.adjust_for_ambient_noise(sumber_suara)
        
        # Rekam suara sampai diam
        audio = telinga.listen(sumber_suara)
        
    try:
        print("Mencerna suara...")
        # 3. Kirim rekaman ke Google untuk diterjemahkan
        # language='id-ID' adalah kode Bahasa Indonesia
        teks = telinga.recognize_google(audio, language='id-ID')
        
        print(f"Bos bilang: {teks}")
        return teks
        
    except sr.UnknownValueError:
        print("Maaf, suara tidak jelas/putus-putus.")
        return ""
    except sr.RequestError:
        print("Maaf, koneksi internet mati.")
        return ""

# --- TES LANGSUNG ---
if __name__ == "__main__":
    dengarkan()