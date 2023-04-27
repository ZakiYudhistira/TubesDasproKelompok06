import argparse, os, time, Module

parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", help = "folder data yang ingin di-load")
args = parser.parse_args()

nama_folder = args.nama_folder
parent_folder = "save"
save_directory = f"{parent_folder}\\{nama_folder}"

if os.path.exists(save_directory):
    
    Module.dotdotdot("Loading", 3, 0.5)

    matriks_user = Module.MatriksData(f"{save_directory}\\user.csv", "user", 3, 102)
    matriks_candi = Module.MatriksData(f"{save_directory}\\candi.csv", "candi", 5, 100)
    matriks_bahan = Module.MatriksData(f"{save_directory}\\bahan_bangunan.csv", "bahan_bangunan", 3, 3)
    tuple_matriks_data = ([matriks_user, matriks_candi, matriks_bahan], 3)
    
    print("Selamat datang di program \"Manajerial Candi\"")
    print("Ketik help untuk menampilkan command")

    program_jalan = True
    logged_in = False
    logged_in_as = ""
    user = ""

    while program_jalan:
        command = input(">>> ")
        if command == "login":
            if logged_in:
                print("Login gagal! Anda telah login dengan username "+user+", silakan lakukan “logout” sebelum melakukan login kembali.")
            else:
                logged_in,user,logged_in_as = Module.login(matriks_user)

        elif command == "logout":
            if logged_in:
                print("Terimakasih "+user+"! Sampai jumpa di lain waktu")
                logged_in,user,logged_in_as = Module.logout()
            else:
                print("Logout gagal!\nAnda belum login, silakan login terlebih dahulu sebelum melakukan logout.")
        
        elif command == "bangun":
            if logged_in_as == "jin_pembangun":
                pasir, batu, air = Module.generateBahan()
                Module.bangun(matriks_bahan, matriks_candi, user, pasir, batu, air, False)
            else:
                print("User bukan jin pembangun\nPembangunan candi tidak dilakukan.")
        
        elif command == "hapusjin":
            if logged_in:
                if logged_in_as == "bandung_bondowoso":
                    Module.hapusJin(matriks_user, matriks_candi)
                else:
                    print("User bukan Bandung Bondowoso\nPengubahan jin tidak dilakukan.")
            else:
                print("User belum login.\nMohon lakukan login terlebih dahulu sebelum melakukan perintah.")

        elif command == "ubahjin":
            if logged_in:
                if logged_in_as == "bandung_bondowoso":
                    Module.ubahTipeJin(matriks_user)
                else:
                    print("User bukan Bandung Bondowoso\nPengubahan jin tidak dilakukan.")
            else:
                print("User belum login.\nMohon lakukan login terlebih dahulu sebelum melakukan perintah.")
        
        elif command == "summonjin":
            if logged_in:
                if logged_in_as == "bandung_bondowoso":
                    Module.summonJin(matriks_user)
                else:
                    print("User bukan Bandung Bondowoso\nSummon jin tidak dilakukan.")
            else:
                print("User belum login.\nMohon lakukan login terlebih dahulu sebelum melakukan perintah.")

        elif command == "kumpul":
            if logged_in:
                if logged_in_as == "jin_pengumpul":
                    Module.kumpul(matriks_bahan,False)
                else:
                    print("User bukan jin pengumpul\nPembangunan candi tidak dilakukan.")
            else:
                print("User belum login.\nMohon lakukan login terlebih dahulu sebelum melakukan perintah.")
        
        elif command == "batchkumpul":
            if logged_in_as == "bandung_bondowoso":
                Module.batchKumpul(matriks_bahan,matriks_user)
            else:
                print("User bukan Bandung Bondowoso\nBatch kumpul bahan tidak dilakukan.")

        elif command == "batchbangun":
            if logged_in_as == "bandung_bondowoso":
                Module.batchBangun(matriks_bahan,matriks_candi,matriks_user)
            else:
                print("User bukan Bandung Bondowoso\nBatch bangun bahan tidak dilakukan.")

        elif command == "laporanjin":
            if logged_in_as == "bandung_bondowoso":
                Module.laporanJin(matriks_user, matriks_candi, matriks_bahan)   
            else:
                print("User bukan Bandung Bondowoso\nTidak bisa mengambil laporan jin!")

        elif command == "laporancandi":
            if logged_in_as == "bandung_bondowoso":
                Module.laporanCandi(matriks_user, matriks_candi, matriks_bahan)
            else:
                print("User bukan Bandung Bondowoso\nTidak bisa mengambil laporan candi!")

        elif command == "hancurkancandi":
            if logged_in_as == "roro_jonggrang":
                Module.hancurkanCandi(matriks_candi)
            else:
                print("User bukan Roro Jonggrang\nTidak boleh menghancurkan candi orang!")

        elif command == "ayamberkokok":
            if logged_in_as == "roro_jonggrang":
                Module.ayamBerkokok(matriks_candi)
            else:
                print("User bukan Roro Jonggrang\nAyam tidak mau berkokok!")

        elif command == "leaderboardjin":
            print("Berikut merupakan leaderboard jin pembuat candi terbanyak:")
            time.sleep(0.5)
            Module.printLeaderboard(matriks_user, matriks_candi, matriks_bahan, "jin")
        
        elif command == "leaderboardcandi":
            print("Berikut merupakan leaderboard candi dengan bahan termahal:")
            time.sleep(0.5)
            Module.printLeaderboard(matriks_user, matriks_candi, matriks_bahan, "candi")

        elif command == "showbahan":
            Module.showBahan(matriks_bahan)
        
        elif command == "exit":
            if logged_in:
                print("Mohon logout dulu sebelum keluar dari program.")
            else:
                opsi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ").upper()
                while not(opsi == "Y" or opsi == "N"):
                    print("Perintah tidak valid, tolong input ulang perintah.")
                    opsi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ").upper()

                if opsi == "Y":
                    tuple_matriks_data = ([matriks_user, matriks_candi, matriks_bahan], 3)
                    Module.saveData(tuple_matriks_data)
                    time.sleep(0.5)
                    print("Terima kasih sudah menjalankan program!")
                    time.sleep(0.5)
                else:
                    print("Baik.")
                    time.sleep(0.5)
                    print("Terima kasih sudah menjalankan program!")
                    time.sleep(0.5)

                program_jalan = False
        
        elif command == "save":
            tuple_matriks_data = ([matriks_user, matriks_candi, matriks_bahan], 3)
            Module.saveData(tuple_matriks_data)
        
        elif command == "help":
            if logged_in:
                Module.help(logged_in_as)
            else:
                print("""1.login: Untuk masuk menggunakan akun.
2.save: Untuk menyimpan hasil permainan.
3.exit: untuk keluar dari program.""")

        else:
            print("Perintah tidak dikenali")
            
else:
    print(f"Folder \"{nama_folder}\" tidak ditemukan.")