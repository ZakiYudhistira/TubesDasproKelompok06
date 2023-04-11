import Module
#------------------------------------------------------------------------------------------------------------ Fungsi login
def login(): # fungsi login yang akan mengoutput True bila login berhasil dan False bila login tidak berhasil
    data_user = Module.load_data('user.csv')
    akses = False
    username = True
    password_p = True
    user = input("Masukkan username : ")
    password = input("Masukkan password : ")
    for i in range(102): # loop pemrosesan file csv untuk menentukan password dan username
        if data_user[i][0] == user:
            if data_user[i][1] == password:
                akses = True
                break
            else:
                akses = False
                password_p = False
        else:
            akses = False
    if akses:
        print("Selamat Datang, "+user+"!")
        print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
        return akses,data_user[i][0],data_user[i][2]
    else :
        if username and not(password_p):
            print("Password salah!")
        elif not(username):
            print("Username tidak terdaftar!")
        return akses," ", " "

#------------------------------------------------------------------------------------------------------------ Fungsi logout    
def logout():
    return False, " ", " "