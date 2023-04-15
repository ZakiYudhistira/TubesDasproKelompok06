import Module

matriks_user = Module.MatriksData("save\\backup\\user.csv", "user", 3, 102)
matriks_candi = Module.MatriksData("save\\backup\\candi.csv", "candi", 5, 100)
matriks_bahan = Module.MatriksData("save\\backup\\bahan_bangunan.csv", "bahan_bangunan", 3, 3)
tuple_matriks_data = ([matriks_user, matriks_candi, matriks_bahan], 3)

def data_leaderboard(matriks_data):
    
    nmaks = 100
    neff = Module.panjang_matriks(matriks_data, nmaks)
    matriks_leaderboard = matriks_data

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
    neff = Module.panjang_matriks(matriks_leaderboard, nmaks)

    for data in range(neff):
        print(f"{data+1}. \"{matriks_leaderboard[data][0]}\": {matriks_leaderboard[data][1]}")


printLeaderboard(data_leaderboard(Module.dataHargaCandi(matriks_candi)))