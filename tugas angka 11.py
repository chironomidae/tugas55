daftar_angka=(199,399,699,999)
print("daftar angka")
for angka in daftar_angka:
    print(angka)
nomor = int(input("masukkan tiga digit angka: "))
if nomor in daftar_angka:
    posisi = daftar_angka.index(nomor)
    print(f"nomor {nomor} ditemukan pada posisi {posisi + 1} dalam daftar")
else:
    print("nomor tidak ada dalam daftar")