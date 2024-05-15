import random
import time

sayı = random.randint(0,51)
seviye = 1
puan = 0
hak=7

while seviye==1:
    user = int(input("Tahminin Ne(0,50)? :"))
    if hak==0:
        time.sleep(1)
        print("HAKKINIZ BİTTİ!")
        print(sayı)
        break
    if user>sayı:
        time.sleep(1)
        print("Daha küçük bir sayı giriniz!")
        hak=hak-1
        print("Kalan Hakkınız :" , hak)
    elif user<sayı:
        time.sleep(1)
        print("Daha büyük bir sayı giriniz!")
        hak=hak-1
        print("Kalan Hakkınız :" , hak)
    elif user==sayı:
        time.sleep(1)
        print("******************************************\n"
              "               KAZANDINIZ                 \n"
              "********************************************\n"
              )
        puan = puan + hak * 10
        print("///////////PUANINIZ :" , puan , "///////////")
        sayı = random.randint(0,101)
        hak = 5
        print("SEVİYE 2'YE GEÇTİNİZ!")
        print("Yeni Hakkınız :" , hak)
        seviye =2



        while seviye==2:
            user = int(input("Tahminin Ne(0,100)? :"))
            if hak == 0:
                time.sleep(1)
                print("HAKKINIZ BİTTİ!")
                print(sayı)
                break
            if user > sayı:
                time.sleep(1)
                print("Daha küçük bir sayı giriniz!")
                hak = hak - 1
                print("Kalan Hakkınız :" , hak)
            elif user < sayı:
                time.sleep(1)
                print("Daha büyük bir sayı giriniz!")
                hak = hak - 1
                print("Kalan Hakkınız :" , hak)
            elif user == sayı:
                time.sleep(1)
                print("******************************************\n"
                      "            OYUNU BİTİRDİNİZ               \n"
                      "********************************************\n"
                      )
                puan=puan+hak*20
                print("///////////TOPLAM PUANINIZ :" , puan , "///////////")
                break

