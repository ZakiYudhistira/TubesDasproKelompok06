import Module

matriks_user = Module.MatriksData("save\\backup\\user.csv", "user", 3, 102)
matriks_candi = Module.MatriksData("save\\backup\\candi.csv", "candi", 5, 100)
matriks_bahan = Module.MatriksData("save\\backup\\bahan_bangunan.csv", "bahan_bangunan", 3, 3)
tuple_matriks_data = ([matriks_user, matriks_candi, matriks_bahan], 3)

def dataLeaderboard(matriks_data:Module.MatriksData, tipe:str):
    nmaks = 100
    if tipe == "jin":
        matriks_leaderboard = Module.dataJinPembangun(matriks_data)
    elif tipe == "candi":
        matriks_leaderboard = Module.dataHargaCandi(matriks_data)

    neff = Module.panjangMatriks(matriks_leaderboard, nmaks)

    for i in range(1, neff):
        indeks = i
        while indeks > 0 and matriks_leaderboard[indeks][1] > matriks_leaderboard[indeks - 1][1]:
            temp = matriks_leaderboard[indeks]
            matriks_leaderboard[indeks] = matriks_leaderboard[indeks - 1]
            matriks_leaderboard[indeks - 1] = temp

            indeks -= 1

    return matriks_leaderboard


def printLeaderboard(matriks_leaderboard):
    nmaks = 100
    neff = Module.panjangMatriks(matriks_leaderboard, nmaks)

    for data in range(neff):
        print(f"{data+1}. \"{matriks_leaderboard[data][0]}\": {matriks_leaderboard[data][1]}")


printLeaderboard(dataLeaderboard(matriks_candi, "jin"))