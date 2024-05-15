import random
pc= random.randint(0,50)

hakSayisi = 7
seviye=1

while seviye==1:
    user = int(input("Tahmininizi Giriniz"))
    if hakSayisi==0:
        print("Hakkınız Kalmadı")
        break
    if user<pc:
        print("Daha büyük bir sayı giriniz")
        hakSayisi= hakSayisi-1
        print("Kalan Hakkınız",hakSayisi)
        #hakSayisi-=1
    elif user>pc:
        print("Daha küçük bir sayı giriniz")
        hakSayisi=hakSayisi-1
        print("Kalan Hakkınız", hakSayisi)
    elif user==pc:
        print("Tebrikler buldunuz")
        print("2. Seviyeye Geçiyorsunuz")
        pc= random.randint(0,100)
        hakSayisi=5
        seviye=2
        break
while seviye==2:
    user = int(input("Tahmininizi Giriniz"))
    if hakSayisi==0:
        print("Hakkınız Kalmadı")
        break
    if user < pc:
        print("Daha büyük bir sayı giriniz")
        hakSayisi = hakSayisi - 1
        print("Kalan Hakkınız", hakSayisi)
        # hakSayisi-=1
    elif user > pc:
        print("Daha küçük bir sayı giriniz")
        hakSayisi = hakSayisi - 1
        print("Kalan Hakkınız", hakSayisi)
    elif user == pc:
        print("Tebrikler buldunuz")
        print("2. Seviyeye Geçiyorsunuz")
        print("Oyun Bitti")
        break

