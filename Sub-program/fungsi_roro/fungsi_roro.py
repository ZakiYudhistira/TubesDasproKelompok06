import Module, time

matriks_user = Module.MatriksData("save\\backup\\user.csv", "user", 3, 102)
matriks_candi = Module.MatriksData("save\\backup\\candi.csv", "candi", 5, 100)
matriks_bahan = Module.MatriksData("save\\backup\\bahan_bangunan.csv", "bahan_bangunan", 3, 3)
tuple_matriks_data = ([matriks_user, matriks_candi, matriks_bahan], 3)

def getIndeks(matriks_data:Module.MatriksData, id):
    indeks = None
    for i in range(Module.panjang_matriks(matriks_data)):
        if matriks_data.matriks[i][0] == id:
            indeks = i
    return indeks

def ayamBerkokok(matriks_data:Module.MatriksData):
    jumlah_candi = Module.panjang_matriks(matriks_data)
    print("Kukuruyuk..", end=" ", flush=True)
    time.sleep(0.5)
    print("Kukuruyuk..\n", flush=True)
    time.sleep(0.5)
    print(f"Jumlah candi: {jumlah_candi}\n")
    time.sleep(1)

    if jumlah_candi < 100:
        print("""Selamat, Roro Jonggrang memenangkan permainan!
        
*Bandung Bondowoso angry noises*
Roro Jonggrang dikutuk menjadi candi!""")
        
    else:
        print("Yah, Bandung Bondowoso memenangkan permainan!")


def hancurkanCandi(matriks_data:Module.MatriksData):
    id = input("Masukkan ID candi: ")
    indeks = getIndeks(matriks_data, id)

    if indeks is None:
        print("Tidak ada candi dengan ID tersebut.")
    else:
        opsi = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)? ").upper()

        if opsi == "Y":
            for i in range(matriks_data.n_param):
                matriks_data.matriks[indeks][i] = None
            print("Candi telah berhasil dihancurkan.")
        elif opsi == "N":
            print("Understandable, have a nice day.")
        else:
            print("Input tidak diketahui.")

ayamBerkokok(matriks_candi)