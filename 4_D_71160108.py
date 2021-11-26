#Surya Nathaniel Kattu
#Nim: 71160108
#Soal No 4

um = int(input("Untuk memulai program masukkan (-1) untuk mulai : "))

def tebakangka () :
    nl1 = int(input("nilai: "))

    import random
    tbk = random.randint (0, 10)

    if tbk == nl1:
        print ("Hasil penjumlahan pasti!", tbk)       
    elif tbk != nl1:
        print ("Apakah tebakan sudah benar ?") 
        print ("lebih kecil (0)")
        print ("lebih besar (1)")
        print ("benar (2)")
    else :
        print ("Program selesai")

if um == -1 :
    tebakangka()       
    inputan = int(input(":"))
    if inputan == 2 :
        print ("Program selesai")
    elif inputan == 0 :
        tebakangka()
    elif inputan == 1 :
        tebakangka()  
              
elif um != -1 :
    print("Program selesai !")