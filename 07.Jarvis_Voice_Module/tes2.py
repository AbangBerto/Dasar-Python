import speech_recognition as sr

print("Mendeteksi microphone utama...")

try:
    mic = sr.Microphone()   # pakai default mic Windows
    print(f"Microphone aktif: {mic}")

    r = sr.Recognizer()

    with mic as source:
        print("Mengkalibrasi noise, diamkan selama 2-3 detik...")
        r.adjust_for_ambient_noise(source, duration=2)

        print("Silakan bicara...")
        audio = r.listen(source, timeout=5)

    print("Rekaman berhasil. Menguji noise atau gangguan...")
    # Hanya cek apakah audio dapat diakses
    print("Level energi audio:", r.energy_threshold)

except Exception as e:
    print("ERROR:", e)
