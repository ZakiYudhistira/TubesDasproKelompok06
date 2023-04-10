import argparse, os, Module

parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", help = "folder data yang ingin di-load")
args = parser.parse_args()

filepath = os.path.dirname(os.path.realpath(__file__))
folder = args.nama_folder
pathfolder_save = f"{filepath}\\{folder}"

class MatriksData:
    def __init__(self, file, n_param, n_max, matriks = None):
        self.file = file
        self.n_param = n_param
        self.n_max = n_max
        self.matriks = Module.load_data(file, n_param, n_max)

if os.path.exists(pathfolder_save):
    print("Loading...")

    matriks_user = MatriksData(f"{pathfolder_save}\\user.csv", 3, 102)
    matriks_candi = MatriksData(f"{pathfolder_save}\\candi.csv", 5, 100)
    matriks_bahan = MatriksData(f"{pathfolder_save}\\bahan_bangunan.csv", 3, 3)

    print("Selamat datang di program \"Manajerial Candi\"")

    program_jalan = True
    logged_in = False
    logged_in_as = " "
    while program_jalan:
        command = str(input(">>> "))
        if command == "login":
            if logged_in:
                print("Login gagal! Anda telah login dengan username "+user+", silahkan lakukan “logout” sebelum melakukan login kembali.")
            else:
                logged_in,user,logged_in_as = Module.login()
        elif command == "logout":
            if logged_in:
                print("Terimakasih "+user+"! sampai jumpa di lain waktu")
                logged_in,user,logged_in_a = Module.logout()
            else:
                print("Logout gagal!")
                print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        elif command == "exit":
            if logged_in:
                print("Mohon logout dulu sebelum keluar dari program")
            else:
                print("Terimakasih")
                program_jalan = False
        else:
            print("Perintah tidak dikenali")
            
else:
    print(f"Folder \"{folder}\" tidak ditemukan.")

