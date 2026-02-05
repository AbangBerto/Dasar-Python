import speech_recognition as sr
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    # Kita cari yang ada tulisan 'Realtek' tapi JENISNYA INPUT (Microphone)
    print(f"Nomor {index} : {name}")