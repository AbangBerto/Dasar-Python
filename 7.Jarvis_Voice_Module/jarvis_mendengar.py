import speech_recognition as sr
import pywhatkit
from gtts import gTTS
import playsound
import time
import os

MIC_INDEX = 1
recognizer = sr.Recognizer()

# Pengaturan sensitivitas suara
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8


# -----------------------------
# SUARA JARVIS (TTS)
# -----------------------------
def jarvis_speak(text):
    print("Jarvis:", text)

    filename = "jarvis_voice.mp3"

    # Hapus file lama jika masih ada
    if os.path.exists(filename):
        try:
            os.remove(filename)
        except:
            pass

    tts = gTTS(text=text, lang="id")
    tts.save(filename)
    playsound.playsound(filename)

    # Bersihkan file suara
    try:
        os.remove(filename)
    except:
        pass


# -----------------------------
# FUNGSI MENDENGAR SUARA
# -----------------------------
def listen(timeout=5, phrase_limit=5):
    try:
        with sr.Microphone(device_index=MIC_INDEX, sample_rate=48000, chunk_size=2048) as source:
            print("Mendengarkan...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_limit)

        text = recognizer.recognize_google(audio, language="id-ID")
        print("Kamu berkata:", text)
        return text.lower()

    except sr.WaitTimeoutError:
        print("Tidak ada suara...")
    except sr.UnknownValueError:
        print("Suara tidak jelas...")
    except Exception as e:
        print("Error:", e)

    return ""


# -----------------------------
# PROSES PERINTAH
# -----------------------------
def process_command(cmd):

    # Perintah musik
    if "putar" in cmd or "lagu" in cmd or "play" in cmd:

        # Ambil judul lagu
        song = cmd.replace("putar", "").replace("lagu", "").replace("play", "").strip()

        if song == "":
            jarvis_speak("Apa judul lagunya?")
            return

        jarvis_speak(f"Memutar {song}")

        # Langsung putar VIDEO PERTAMA
        pywhatkit.playonyt(song)
        return

    # Perintah buka YouTube
    if "youtube" in cmd:
        jarvis_speak("Membuka YouTube.")
        pywhatkit.playonyt("youtube")
        return

    jarvis_speak("Perintah belum saya mengerti.")


# -----------------------------
# MODE WAKE WORD
# -----------------------------
def wait_for_jarvis():
    print("Menunggu wake word: hai jarvis...")
    while True:
        text = listen(timeout=4, phrase_limit=4)
        if "hai" in text:
            jarvis_speak("Ya, Ada apa bos berto")
            return


# -----------------------------
# LOOP UTAMA
# -----------------------------
while True:

    # 1. Tunggu dipanggil dulu
    wait_for_jarvis()

    # 2. Setelah dipanggil, dengarkan perintah
    command = listen()
    if command != "":
        process_command(command)

    time.sleep(0.3)
