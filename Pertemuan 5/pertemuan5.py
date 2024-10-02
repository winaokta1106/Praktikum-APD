# nama = ["shandy", 160, True, 3.96[123,"ALVITO",False,3.66]]
# (nama [4][-2])

# nama = ["shandy",106,True,
#         ["yuyun",145],3.96,
#         ]
# matkul = ["APD",
#           "APL",
#           "WEB",
#           "JARKOM",
#           "BASDAT",
#           "STRUKDAT",
#           "PTI",
#           "KALKULUS",
#           "PROBAS"
# ]
# print(matkul[-1])

# makanan = ["Bakso","sate","soto"]
# print("Sebelum: ")
# print(makanan[1:])
# makanan.append("nasi goreng")
# print("Sesudah: ")
# del makanan[2:2]
# print(makanan)
# makanan.insert(2,"nasi goreng")
# makanan[0] = ["AYAM", "BEBEK"]
# print(makanan)

# minuman 6. 3(dihapus) 6(air putih) 1(jus tomat)

# minuman = ["susu", "jus mangga", "jus sirsak", 
#            "Es teler", "es teh", "es buah"]
# print("sebelum")
# print(minuman)
# del minuman[2]
# print("sesudah")
# print(minuman)
# minuman[4] = "air putih"
# print(minuman)
# minuman.insert(0,"jus tomat")
# print(minuman)

makanan = ["ayam","ikan",["bakso","soto","sate","ikan","bebek"],
           ["teh","kopi","air"]]

for i in makanan :
    if isinstance(i, list) :
       for j in i :
           print(j)
    else:
        print(i)
    # for i in makanan :
    #     for j in i :
    #         print(j)