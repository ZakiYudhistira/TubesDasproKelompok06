import fungsi_login_logout
program_jalan = True
logged_in = False
logged_in_as = " "
print("Selamat datang pada program summon Jin")
while program_jalan:
    command = str(input(">>> "))
    if command == "login":
        if logged_in:
            print("Login gagal! Anda telah login dengan username "+user+", silahkan lakukan “logout” sebelum melakukan login kembali.")
        else:
            logged_in,user,logged_in_as = fungsi_login_logout.login()
    elif command == "logout":
        if logged_in:
            print("Terimakasih "+user+"! sampai jumpa di lain waktu")
            logged_in,user,logged_in_a = fungsi_login_logout.logout()
        else:
            print("Logout gagal!"+'\n'+"Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    elif command == "exit":
        if logged_in:
            print("Mohon logout dulu sebelum keluar dari program")
        else:
            print("Terimakasih")
            program_jalan = False
    else:
        print("Perintah tidak dikenali")