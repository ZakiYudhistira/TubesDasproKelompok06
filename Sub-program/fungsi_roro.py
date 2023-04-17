import Module, time

matriks_user = Module.MatriksData("save\\backup\\user.csv", "user", 3, 102)
matriks_candi = Module.MatriksData("save\\backup\\candi.csv", "candi", 5, 100)
matriks_bahan = Module.MatriksData("save\\backup\\bahan_bangunan.csv", "bahan_bangunan", 3, 3)
tuple_matriks_data = ([matriks_user, matriks_candi, matriks_bahan], 3)

def getIndeks(matriks_data, id, n_maks:int):
    indeks = None
    neff = Module.panjangMatriks(matriks_data, n_maks)
    for i in range(neff):
        if matriks_data[i][0] == id:
            indeks = i

    return indeks


def hapusData(matriks_data:Module.MatriksData, data):
    neff = Module.panjangMatriks(matriks_data.matriks, matriks_data.n_maks)
    i_data = getIndeks(matriks_data.matriks, data, matriks_data.n_maks)

    for param in range(matriks_data.n_param):
        matriks_data.matriks[i_data][param] = None

    for data in range(i_data, neff):
        matriks_data.matriks[data] = matriks_data.matriks[data + 1]

    for param in range(matriks_data.n_param):
        matriks_data.matriks[neff][param] = None


def ayamBerkokok(matriks_candi:Module.MatriksData):
    jumlah_candi = Module.panjangMatriks(matriks_candi.matriks, matriks_candi.n_maks)
    print("Kukuruyuk..", end=" ", flush=True)
    time.sleep(0.5)
    print("Kukuruyuk..\n", flush=True)
    time.sleep(0.5)
    print(f"Jumlah candi: {jumlah_candi}\n")
    time.sleep(1)

    if jumlah_candi < 100:
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        Module.dotdotdot("", 3, 0.5)
        print("*Bandung Bondowoso angry noises*\nRoro Jonggrang dikutuk menjadi candi!")
        
    else:
        print("Yah, Bandung Bondowoso memenangkan permainan!")


def hancurkanCandi(matriks_candi:Module.MatriksData):
    id = input("Masukkan ID candi: ")
    indeks = getIndeks(matriks_candi.matriks, id, matriks_candi.n_maks)

    if indeks is None:
        print("Tidak ada candi dengan ID tersebut.")
    else:
        opsi = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)? ").upper()
        while not (opsi == "Y" or opsi == "N"):
            print("Perintah tidak valid, tolong input ulang perintah.")
            opsi = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)? ").upper()

        if opsi == "Y":
            hapusData(matriks_candi, id)
            print("Candi telah berhasil dihancurkan.")
        else:
            print("Understandable, have a nice day.")


print(matriks_candi.matriks)
hancurkanCandi(matriks_candi)
print(matriks_candi.matriks)