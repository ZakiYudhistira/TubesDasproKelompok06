import Module

matriks_user = Module.MatriksData("save\\backup\\user.csv", "user", 3, 102)
matriks_candi = Module.MatriksData("save\\backup\\candi.csv", "candi", 5, 100)
matriks_bahan = Module.MatriksData("save\\backup\\bahan_bangunan.csv", "bahan_bangunan", 3, 3)
tuple_matriks_data = ([matriks_user, matriks_candi, matriks_bahan], 3)

def bubbleSortMatriks(matriks_data:list[list], nmaks:int, i_data:int, naik=False):
    matriks_sorted = matriks_data
    neff = Module.panjangMatriks(matriks_sorted, nmaks)
    print(matriks_data)

    for i in range(1, neff):
        indeks = i
        if naik:
            while indeks > 0 and matriks_sorted[indeks][i_data] < matriks_sorted[indeks-1][i_data]:
                temp = matriks_sorted[indeks]
                matriks_sorted[indeks] = matriks_sorted[indeks-1]
                matriks_sorted[indeks-1] = temp

                indeks -= 1
        else:
            while indeks > 0 and matriks_sorted[indeks][i_data] > matriks_sorted[indeks-1][i_data]:
                temp = matriks_sorted[indeks]
                matriks_sorted[indeks] = matriks_sorted[indeks-1]
                matriks_sorted[indeks-1] = temp

                indeks -= 1

    return matriks_sorted
    

def isTerurutLekso(kata1:str, kata2:str):
    terurut = True
    i_huruf = None

    if kata1 != "" and kata2 != "":
        while not terurut:
            

            i_huruf += 1
            pass
    else:
        if kata1 == "":
            terurut = False
        else:
            terurut = True


    return terurut


def dataLeaderboard(matriks_data:Module.MatriksData, tipe:str):
    nmaks = 100
    if tipe == "jin":
        matriks_leaderboard = Module.dataJinPembangun(matriks_data)
    elif tipe == "candi":
        matriks_leaderboard = Module.dataHargaCandi(matriks_data)

    return bubbleSortMatriks(matriks_leaderboard, nmaks, 1)


def printLeaderboard(matriks_leaderboard):
    nmaks = 100
    neff = Module.panjangMatriks(matriks_leaderboard, nmaks)

    for data in range(neff):
        print(f"{data+1}. \"{matriks_leaderboard[data][0]}\": {matriks_leaderboard[data][1]}")


printLeaderboard(dataLeaderboard(matriks_candi, "jin"))
