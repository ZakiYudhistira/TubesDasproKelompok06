import argparse, os, time, Module

parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", help = "folder data yang ingin di-load")
args = parser.parse_args()

filepath = os.path.dirname(os.path.realpath(__file__))
folder = args.nama_folder
save_folderpath = f"{filepath}\\{folder}"



if os.path.exists(save_folderpath):
    
    Module.dotdotdot("Loading", 3, 0.5)

    matriks_user = Module.MatriksData(f"{save_folderpath}\\user.csv", "user", 3, 102)
    matriks_candi = Module.MatriksData(f"{save_folderpath}\\candi.csv", "candi", 5, 100)
    matriks_bahan = Module.MatriksData(f"{save_folderpath}\\bahan_bangunan.csv", "bahan_bangunan", 3, 3)
    tuple_matriks_data = ([matriks_user, matriks_candi, matriks_bahan], 3)
    
    print("Selamat datang di program \"Manajerial Candi\"")

    program_jalan = True
    logged_in = False
    logged_in_as = ""

    while program_jalan:
        command = str(input(">>> "))
        if command == "login":
            if logged_in:
                print("Login gagal! Anda telah login dengan username "+user+", silahkan lakukan “logout” sebelum melakukan login kembali.")
            else:
                logged_in,user,logged_in_as = Module.login(matriks_user.matriks)
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