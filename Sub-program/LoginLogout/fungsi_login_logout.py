import csv # melakukan import library
data_user_read = open('user.csv','r') #inisialisasi read file csv
data_user_reader = csv.reader(data_user_read,delimiter=';')

def login(): # fungsi login yang akan mengoutput True bila login berhasil dan False bila login tidak berhasil
    akses = False
    username = True
    password_p = True
    user = input("Masukkan username : ")
    password = input("Masukkan password : ")
    for row in data_user_reader: # loop pemrosesan file csv untuk menentukan password dan username
        cek_user = (row[0],row[1])
        if cek_user == (user,password):
            akses = True
        elif user == row[0] and password != row[1]:
            username = True
            password_p = False
        elif user != row[0]:
            username = False
    if akses:
        print("Selamat Datang, "+user+"!")
        print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
        return akses, user
    else :
        if username and not(password_p):
            print("Password salah!")
        elif not(username):
            print("Username tidak terdaftar!")
        return akses," "
    
def logout():
    return False, " "
        
program_jalan = True
logged_in = False
while program_jalan:
    command = str(input(">>> "))
    if command == "login":
        data_user_read = open('user.csv','r') # reset pembacaan file csv
        data_user_reader = csv.reader(data_user_read,delimiter=';')
        if logged_in:
            print("Login gagal! Anda telah login dengan username "+user+", silahkan lakukan “logout” sebelum melakukan login kembali.")
        else:
            logged_in,user = login()
    elif command == "logout":
        if logged_in:
            print("Terimakasih "+user+"! sampai jumpa di lain waktu")
            logged_in,user = logout()
        else:
            print("Logout gagal! Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    elif command == "exit":
        if logged_in:
            print("Mohon logout dulu sebelum keluar dari program")
        else:
            print("Terimakasih")
            program_jalan = False
    else:
        print("Perintah tidak dikenali")