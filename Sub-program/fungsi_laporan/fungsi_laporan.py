import Module

matriks_user = Module.MatriksData("save\\backup\\user.csv", "user", 3, 102)
matriks_candi = Module.MatriksData("save\\backup\\candi.csv", "candi", 5, 100)
matriks_bahan = Module.MatriksData("save\\backup\\bahan_bangunan.csv", "bahan_bangunan", 3, 3)
tuple_matriks_data = ([matriks_user, matriks_candi, matriks_bahan], 3)

def jumlahBahan(matriks_candi:Module.MatriksData):
    pasir, batu, air = 0, 0, 0

    for candi in range(Module.panjang_matriks(matriks_candi.matriks, matriks_candi.n_maks)):
        pasir += int(matriks_candi.matriks[candi][2])
        batu += int(matriks_candi.matriks[candi][3])
        air += int(matriks_candi.matriks[candi][4])

    return pasir, batu, air


def jumlahJin(matriks_user:Module.MatriksData):
    jumlah_jin, jumlah_pengumpul, jumlah_pembangun = 0, 0, 0

    for jin in range(2, Module.panjang_matriks(matriks_user.matriks, matriks_user.n_maks)):
        jumlah_jin += 1
        if matriks_user.matriks[jin][2] == "jin_pengumpul":
            jumlah_pengumpul += 1
        else:
            jumlah_pembangun += 1

    return jumlah_jin, jumlah_pengumpul, jumlah_pembangun


def dataJinPembangun(matriks_candi:Module.MatriksData):
    nmaks_jin = 100
    neff_jin = Module.panjang_matriks(matriks_candi.matriks, nmaks_jin)
    matriks_data_pembangun = [[None, None] for i in range(nmaks_jin)]

    for candi in range(neff_jin):
        pembuat = matriks_candi.matriks[candi][1]
        id_pembuat = Module.getIndeks(matriks_data_pembangun, pembuat, nmaks_jin)
        id_kosong = Module.panjang_matriks(matriks_data_pembangun, nmaks_jin)

        if id_pembuat is None:
            matriks_data_pembangun[id_kosong] = [pembuat, 1]
        else:
            matriks_data_pembangun[id_pembuat][1] += 1

    return matriks_data_pembangun


def dataHargaCandi(matriks_candi:Module.MatriksData):
    nmaks_candi = 100
    neff_candi = Module.panjang_matriks(matriks_candi.matriks, nmaks_candi)
    matriks_data_harga = [[None, None] for i in range(nmaks_candi)]

    for candi in range(neff_candi):
        id_candi = matriks_candi.matriks[candi][0]
        pasir = int(matriks_candi.matriks[candi][2])
        batu = int(matriks_candi.matriks[candi][3])
        air = int(matriks_candi.matriks[candi][4])
        harga = pasir*10000 + batu*15000 + air*7500

        matriks_data_harga[candi] = [id_candi, harga]

    return matriks_data_harga


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


def hapusData(matriks_data:Module.MatriksData, data):
    neff = Module.panjang_matriks(matriks_data.matriks, matriks_data.n_maks)
    i_data = Module.getIndeks(matriks_data.matriks, data, matriks_data.n_maks)

    for param in range(matriks_data.n_param):
        matriks_data.matriks[i_data][param] = None

    for data in range(i_data, neff):
        matriks_data.matriks[data] = matriks_data.matriks[data + 1]

    for param in range(matriks_data.n_param):
        matriks_data.matriks[neff][param] = None


def laporanJin(matriks_user:Module.MatriksData, matriks_candi:Module.MatriksData, matriks_bahan:Module.MatriksData):
    total_jin, total_pengumpul, total_pembangun = jumlahJin(matriks_user)
    sisa_pasir = matriks_bahan.matriks[0][2]
    sisa_batu = matriks_bahan.matriks[1][2]
    sisa_air = matriks_bahan.matriks[2][2]
    jin_terajin, jin_termalas = "-", "-"

    if total_jin > 0:
        i_maks = 0
        i_min = total_jin - 1

        if data_leaderboard(dataJinPembangun(matriks_candi))[i_maks][0] is not None:
            id_termahal = data_leaderboard(dataJinPembangun(matriks_candi))[i_maks][0]
            harga_termahal = f"({data_leaderboard(dataJinPembangun(matriks_candi))[i_maks][1]})"

        if data_leaderboard(dataJinPembangun(matriks_candi))[i_min][0] is not None:
            id_termurah = data_leaderboard(dataJinPembangun(matriks_candi))[i_min][0]
            harga_termurah = f"({data_leaderboard(dataJinPembangun(matriks_candi))[i_min][1]})"

    print(f"""
> Total Jin: {total_jin}
> Total Jin Pengumpul: {total_pengumpul}
> Total Jin Pembangun: {total_pembangun}
> Jin Terajin: {jin_terajin}
> Jin Termalas: {jin_termalas}
> Jumlah Pasir Tersisa: {sisa_pasir} unit
> Jumlah Air Tersisa: {sisa_air} unit
> Jumlah Batu Tersisa: {sisa_batu} unit
""")


def laporanCandi(matriks_candi:Module.MatriksData):
    total_candi = Module.panjang_matriks(matriks_candi.matriks, matriks_candi.n_maks)
    total_pasir, total_batu, total_air = jumlahBahan(matriks_candi)
    id_termahal, id_termurah = "-", "-"
    harga_termahal, harga_termurah = "", ""

    if total_candi > 0:
        i_maks = 0
        i_min = total_candi - 1

        if data_leaderboard(dataHargaCandi(matriks_candi))[i_maks][0] is not None:
            id_termahal = data_leaderboard(dataHargaCandi(matriks_candi))[i_maks][0]
            harga_termahal = f"({data_leaderboard(dataHargaCandi(matriks_candi))[i_maks][1]})"

        if data_leaderboard(dataHargaCandi(matriks_candi))[i_min][0] is not None:
            id_termurah = data_leaderboard(dataHargaCandi(matriks_candi))[i_min][0]
            harga_termurah = f"({data_leaderboard(dataHargaCandi(matriks_candi))[i_min][1]})"
        
    print(f"""
> Total Candi: {total_candi}
> Total Pasir yang Digunakan: {total_pasir}
> Total Air yang Digunakan: {total_air}
> Total Batu yang Digunakan: {total_batu}
> ID Candi Termahal: {id_termahal} {harga_termahal}
> ID Candi Termurah: {id_termurah} {harga_termurah}
""")


laporanCandi(matriks_candi)