#Surya Nathaniel Kattu
#Nim: 71160108
#Soal No 1

s = str(input("Masukkan string : "))

def cekString():
    #ubah string (str) ke float
    f = float(s)
    if f % 2 == 0: #bilangan genap 
        gnp = f/2
        print(gnp)
    elif f % 2 == 1: #bilangan ganjil
        gnjl = (f + 5)/2
        print(gnjl)  
        
cekString()   