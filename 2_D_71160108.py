#Surya Nathaniel Kattu
#Nim: 71160108
#Soal No 2

ia = str(input("Masukkan sebuah kata/kalimat : "))
id = str(input("Masukkan karakter yang ingin disisipkan : "))

def sisipHuruf() :
    ssp = id.join(ia[i:i + 1] for i in range(0, len(ia), 1))
    print (ssp)

def sisipKata() :
    sl = len(ia)
    ssk = ia[0:int(sl/2)] + id + ia[int(sl/2):]
    print (ssk)

sisipHuruf()
sisipKata()