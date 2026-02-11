import wikipedia

wikipedia.set_lang("id")

def cari_info(topik):
    print("Sedang mencari informasi yang sedang anda cari")
    try :
        hasil = wikipedia.summary(topik, sentences=2)
        return hasil 
    except wikipedia.exceptions.DisambiguationError:
        return "Topik terlalu umum silahkan coba yang lain"

    except wikipedia.exceptions.PageError:
        return "Maaf, tidak ada artikel tentang itu"
    
info = cari_info("Soekarno")
print(info)
    

