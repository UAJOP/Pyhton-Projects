def kdvHesapla(fiyat,kdvOran):
    if kdvOran==1 or kdvOran==10 or kdvOran==20:
        kdvMiktarı = fiyat*kdvOran/100
        toplam = fiyat+kdvMiktarı
        print(f"Bedeliniz {fiyat}, kdv değeriniz : {kdvMiktarı}, toplam {toplam}")
    else:
        print("KDV oranı 1-10 ya da 20 olmalı")

while True:
    bedel = int(input("KDV Hesaplanacak bedeli giriniz"))
    kdvOran = int(input("KDV oranınızı giriniz"))
    kdvHesapla(bedel,kdvOran)
