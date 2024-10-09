# # # # daftar_buku = {
# # # # "Buku1" : "Harry Potter",
# # # # "Buku2" : "Twillight",
# # # # "Buku3" : "Twillight"
# # # # }
# # # # print(daftar_buku["Buku1"])
# # # # print(daftar_buku["Buku2"])
# # # # print(daftar_buku["Buku3"])
# # # # # print(daftar_buku["Buku3"])

# # # # Biodata = {
# # # #     "Nama" : "Aldy Ramadhan Syahputra",
# # # #     "NIM" : 2109106079,
# # # #     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
# # # #     "Mahasiswa_Aktif" :True,
# # # #     "Social Media" : {
# # # #         "Instagram" : "@aldyrmdhns_",
# # # #         "Discord" : "Izanami#6848",
# # # #         "Email" : "iniemail@gmail.com"
# # # #     }
# # # # }

# # # # print(Biodata["KRS"][0])
# # # # print(Biodata["Social Media"]["Email"])

# # # # Games = dict(Sekiro = "Action", Pokemon = "Adventure",
# # # # Valorant = {"nama" : {123 : "informatika"}} )
# # # # print(Games['Valorant']['nama'][123])

# # # # Games = {
# # # #     "Games1" : "PUBG Mobile",
# # # #     "Games2" : "Mobile Legends",
# # # #     "Games3" : {
# # # #         "nama" : "COC",
# # # #         "genre" : "strategy",
# # # #     }
# # # # }
# # # # print((Games.get('Game3')).get('genre'))

# # # # Nilai = {
# # # # "Matematika" : 80,
# # # # "B. Indonesia" : 90,
# # # # "B. Inggris" : 81,
# # # # "Kimia" : 78,
# # # # "Fisika" : 80
# # # # }
# # # # #tanpa menggunakan items
# # # # for i in Nilai:
# # # #     print(i)
# # # # print("")

# # # # #menggunakan items
# # # # for mapel, nilai in Nilai.items():
# # # #     print(f"Nilai {mapel} anda adalah {nilai}")

# # # Film = {
# # # "Avenger Endgame" : "Action",
# # # "Sherlock Holmes" : "Mystery",
# # # "The Conjuring" : "Horror"
# # # }
# # # #Sebelum Ditambah
# # # # print(Film)

# # # Film["Zombieland"] = "Comedy"
# # # Film.update({"Hours" : "Thriller", 
# # #              "Rush Hour" : "Comedy", 
# # #              "Oblivion" : "Science Fication"})

# # # #Setelah Ditambah
# # # # penggunaan del
# # # # del Film['Avenger Endgame']
# # # # print(Film)
# # # # simpan = Film.pop('Hours')
# # # # # Film.clear()
# # # # print(Film)
# # # # Film["Hours"] = simpan
# # # # print(Film)

# # # movies = Film.copy()
# # # print(movies)
# # # print("Jumlah Data = ", len(Film))

# # # key = "apel", "jeruk", "mangga"
# # # value = 1
# # # buah = dict.fromkeys(key, value)
# # # print(buah)

# # Nilai = {
# # "Matematika" : 80,
# # "B. Indonesia" : 90,
# # "B. Inggris" : 81
# # }
# # #sebelum Setdefault
# # print(Nilai)
# # print("")
# # #menggunakan setdefault
# # print("Nilai : ", Nilai.setdefault("Kimia", 70))
# # print("")
# # #setelah menggunakan setdefault
# # print(Nilai)

# Musik = {
# "The Chainsmoker" : ["All we Know", "TheParis"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
# print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for x, y in value.items():
#         print (x, " : ", y)
# print("")

