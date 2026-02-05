# Menampilkan List dengan for 

# senjata = ["Repulsom", "Unibeam", "Rocket", "Laser"]
# for x in senjata :
#     print(x)


# List berpasangan 
# status_baterai = {
#     "Mark 1" : "0%",
#     "Mark 7" : "85%",
#     "Mark 50": "100%",
#     "Hulkbuster": "50%"
# }

# for suit, power in status_baterai.items():
#     print(f"{suit} sisa baterai {power}")


siswa = {
    "Michael" : 100,
    "Berto" : 90,
    "Ali" : 80,
    "Dola" : 60
}
for name, value in siswa.items():
    
    if value > 75:
        print (f"{name} di atas KKM dengan nilai {value}")

    else:
        print (f"{name} Nilai di bawah KKM dengan nilai {value}")
