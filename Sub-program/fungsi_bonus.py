from Module import *

matriks_user = MatriksData("save\\baru\\user.csv", "user", 3, 102)
matriks_candi = MatriksData("save\\baru\\candi.csv", "candi", 5, 100)
matriks_bahan = MatriksData("save\\baru\\bahan_bangunan.csv", "bahan_bangunan", 3, 3)
tuple_matriks_data = ([matriks_user, matriks_candi, matriks_bahan], 3)
    

def isTerurutLeksi(kata1:str, kata2:str) -> bool:
    terurut = True

    if len(kata1) > len(kata2):
        ref_len = len(kata2)
    else:
        ref_len = len(kata1)

    for i_huruf in range(ref_len):
        if kata1[i_huruf] != kata2[i_huruf]:
            if kata1[i_huruf] > kata2[i_huruf]:
                terurut = False
            break

        if i_huruf == ref_len - 1:
            if ref_len == len(kata2):
                terurut = False            

    return terurut


def dataJinPembangun(matriks_user:MatriksData, matriks_candi:MatriksData, kategori:str) -> Matriks:
    neff_user = panjangMatriks(matriks_user.matriks, matriks_user.nmaks)
    neff_candi = panjangMatriks(matriks_candi.matriks, matriks_candi.nmaks)
    nmaks_pembangun = jumlahJin(matriks_user)[2]
    matriks_data_pembangun = [[None, 0] for i in range(nmaks_pembangun)]

    for user in range(neff_user):
        pembangun = matriks_user.matriks[user][0]
        i_kosong = panjangMatriks(matriks_data_pembangun, nmaks_pembangun)

        if matriks_user.matriks[user][2] == "jin_pembangun":
            matriks_data_pembangun[i_kosong][0] = pembangun

    if kategori == "total_pasir":
        i_ref = 2
    elif kategori == "total_batu":
        i_ref = 3
    elif kategori == "total_air":
        i_ref = 4

    for candi in range(neff_candi):
        pembangun = matriks_candi.matriks[candi][1]
        i_pembuat = getIndeks(matriks_data_pembangun, pembangun, nmaks_pembangun)

        if i_pembuat is not None:
            if kategori == "total_candi":
                matriks_data_pembangun[i_pembuat][1] += 1
            elif kategori == "total_bahan":
                total_bahan = 0
                for i in range(3):
                    total_bahan += int(matriks_candi.matriks[candi][i+2])
                matriks_data_pembangun[i_pembuat][1] += total_bahan
            else:
                matriks_data_pembangun[i_pembuat][1] += int(matriks_candi.matriks[candi][i_ref])

    return matriks_data_pembangun


def dataHargaCandi(matriks_candi:MatriksData) -> Matriks:
    neff_candi = panjangMatriks(matriks_candi.matriks, matriks_candi.nmaks)
    matriks_data_harga = [[None, None] for i in range(neff_candi)]

    for candi in range(neff_candi):
        id_candi = matriks_candi.matriks[candi][0]
        pasir = int(matriks_candi.matriks[candi][2])
        batu = int(matriks_candi.matriks[candi][3])
        air = int(matriks_candi.matriks[candi][4])
        harga = pasir*10000 + batu*15000 + air*7500

        matriks_data_harga[candi] = [id_candi, harga]

    return matriks_data_harga


def dataLeaderboard(matriks_user:MatriksData, matriks_candi:MatriksData, matriks_leaderboard:Matriks, tipe:str) -> Matriks:
    if tipe == "jin":
        neff = jumlahJin(matriks_user)[2]
    elif tipe == "candi":
        neff = panjangMatriks(matriks_candi.matriks, matriks_candi.nmaks)

    for i in range(1, neff):
        indeks = i 

        while indeks > 0 and matriks_leaderboard[indeks][1] >= matriks_leaderboard[indeks-1][1]:

            if matriks_leaderboard[indeks][1] != matriks_leaderboard[indeks-1][1]:
                temp = matriks_leaderboard[indeks]
                matriks_leaderboard[indeks] = matriks_leaderboard[indeks-1]
                matriks_leaderboard[indeks-1] = temp

            else:
                if not(isTerurutLeksi(matriks_leaderboard[indeks-1][0], matriks_leaderboard[indeks][0])):
                    temp = matriks_leaderboard[indeks]
                    matriks_leaderboard[indeks] = matriks_leaderboard[indeks-1]
                    matriks_leaderboard[indeks-1] = temp

            indeks -= 1

    return matriks_leaderboard


def printLeaderboard(matriks_user:MatriksData, matriks_candi:MatriksData) -> None:

    tipe = input("Leaderboard tipe apakah yang Anda diinginkan? (jin/candi) ")

    while not(tipe == "jin" or tipe == "candi"):
        print("Tipe yang tersedia hanyalah \"jin\" atau \"candi\". Tolong ulangi kembali.")
        tipe = input("Leaderboard tipe apakah yang diinginkan? (jin/candi) ")
    
    if tipe == "candi":
        neff = panjangMatriks(matriks_candi.matriks, matriks_candi.nmaks)
        data_candi = dataHargaCandi(matriks_candi)
        matriks_leaderboard = dataLeaderboard(matriks_user, matriks_candi, data_candi, tipe)

        if neff != 0:
            print("Berikut merupakan leaderboard candi saat ini:")
            for data in range(neff):
                print(f"{data+1}. \"{matriks_leaderboard[data][0]}\": {matriks_leaderboard[data][1]}")
        else:
            print("Oh maaf, data yang tersedia kosong!")

    else:
        neff = jumlahJin(matriks_user)[2]
        kategori = input("""Berikut merupakan beberapa kategori leaderboard jin pembangun:
(1): total candi yang dibuat.
(2): total bahan yang digunakan.
(3): total pasir yang digunakan.
(4): total batu yang digunakan.
(5): total air yang digunakan.
Pada kategori apakah Anda ingin melihat leaderboard jin pembangun? (1--5) """)
        while not(kategori == "1" or kategori == "2" or kategori == "3" or kategori == "4"  or kategori == "5"):
            print("Kategori yang tersedia hanya ada 5. Tolong ulangi kembali.")
            kategori = input("Pada kategori apakah Anda ingin melihat leaderboard jin pembangun? (1--5) ")

        if kategori == "1":
            kategori = "total_candi"
        elif kategori == "2":
            kategori = "total_bahan"
        elif kategori == "3":
            kategori = "total_pasir"
        elif kategori == "4":
            kategori = "total_batu"
        elif kategori == "5":
            kategori = "total_air"

        data_jin = dataJinPembangun(matriks_user, matriks_candi, kategori)
        matriks_leaderboard = dataLeaderboard(matriks_user, matriks_candi, data_jin, tipe)

        if neff != 0:
            print(f"Berikut merupakan leaderboard jin pada kategori {kategori}:")
            for data in range(neff):
                print(f"{data+1}. \"{matriks_leaderboard[data][0]}\": {matriks_leaderboard[data][1]}")
        else:
            print("Oh maaf, data yang tersedia kosong!")

