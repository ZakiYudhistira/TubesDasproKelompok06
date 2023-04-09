import csv # melakukan import library
data_user_read = open('user.csv','r') #inisialisasi read file csv
data_user_reader = csv.reader(data_user_read,delimiter=';')

def login(): # fungsi login yang akan mengoutput True bila login berhasil dan False bila login tidak berhasil
    akses = False
    user = input("Masukkan username : ")
    password = input("Masukkan password : ")
    if user == 'exit':
        akses = True
        return (akses,"logged out") # return value bila pengguna ingin keluar dari program
    else:
        for row in data_user_reader: # loop pemrosesan file csv untuk menentukan password dan username
            cek_user = (row[0],row[1])
            if cek_user == (user,password):
                akses = True
        if not(akses):
            print("Username dan password tidak sesuai atau username tidak terdaftar, mohon coba lagi")
            return akses
        else :
            print("Login berhasil")
            return akses
while True:
    logged_in = login()
    if logged_in == True:
        break
    elif logged_in == (True,"logged out"):
        print("Gagal login")
        break
    else:
        data_user_read = open('user.csv','r') #reset data csv agar bisa diproses ulang pada loop
        data_user_reader = csv.reader(data_user_read,delimiter=';')