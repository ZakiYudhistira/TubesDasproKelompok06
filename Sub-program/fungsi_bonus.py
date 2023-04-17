import Module

matriks_user = Module.MatriksData("save\\backup\\user.csv", "user", 3, 102)
matriks_candi = Module.MatriksData("save\\backup\\candi.csv", "candi", 5, 100)
matriks_bahan = Module.MatriksData("save\\backup\\bahan_bangunan.csv", "bahan_bangunan", 3, 3)
tuple_matriks_data = ([matriks_user, matriks_candi, matriks_bahan], 3)

def bubbleSortMatriks(matriks_data:list[list], nmaks:int, i_data:int, naik=False):
    matriks_sorted = matriks_data
    neff = Module.panjangMatriks(matriks_sorted, nmaks)

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
    

def isTerurutLeksi(kata1:str, kata2:str):
    terurut = True
    i_huruf = 0

    if kata1 != "" and kata2 != "":
        if len(kata1) > len(kata2):
            ref_len = len(kata2)
        else:
            ref_len = len(kata1)

        while terurut:
            if i_huruf > ref_len - 1:
                if ref_len == len(kata2):
                    terurut = False
                break    
                
            if kata1[i_huruf] > kata2[i_huruf]:
                terurut = False

            i_huruf += 1

    else:
        if kata1 == "":
            terurut = False

    return terurut


def dataLeaderboard(matriks_data:Module.MatriksData, tipe:str):
    nmaks = 100
    if tipe == "jin":
        matriks_leaderboard = Module.dataJinPembangun(matriks_data)
    elif tipe == "candi":
        matriks_leaderboard = Module.dataHargaCandi(matriks_data)

    neff = Module.panjangMatriks(matriks_leaderboard, nmaks)
    for i in range(1, neff):
        indeks = i 

        while indeks > 0 and matriks_leaderboard[indeks][1] >= matriks_leaderboard[indeks-1][1]:
            kondisi_lekso = isTerurutLeksi(matriks_leaderboard[indeks-1][0], matriks_leaderboard[indeks][0])

            if matriks_leaderboard[indeks][1] == matriks_leaderboard[indeks-1][1] and not kondisi_lekso:
                temp = matriks_leaderboard[indeks]
                matriks_leaderboard[indeks] = matriks_leaderboard[indeks-1]
                matriks_leaderboard[indeks-1] = temp

            else:
                temp = matriks_leaderboard[indeks]
                matriks_leaderboard[indeks] = matriks_leaderboard[indeks-1]
                matriks_leaderboard[indeks-1] = temp

            indeks -= 1

    return matriks_leaderboard


def printLeaderboard(matriks_leaderboard:list[list]):
    nmaks = 100
    neff = Module.panjangMatriks(matriks_leaderboard, nmaks)

    for data in range(neff):
        print(f"{data+1}. \"{matriks_leaderboard[data][0]}\": {matriks_leaderboard[data][1]}")


printLeaderboard(dataLeaderboard(matriks_candi, 'jin'))