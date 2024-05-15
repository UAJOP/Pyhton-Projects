def kdv(fiyat,kdvU):
    if kdvU ==1 or kdvU ==10 or kdvU ==20:
        kdvOranı = fiyat * kdvU / 100
        toplam = fiyat + kdvOranı
        print(f"Bedeliniz {fiyat}, kdv değeriniz : {kdvOranı} toplam paranız : {toplam}")
    else:
        print("Lütfen geçerli kdv oranı giriniz....")


while True:
    fiyat = int(input("Lütfen fiyatı giriniz :" ))
    kdvU = float(input("Lütfen kdv oranını giriniz (1,10,20): "))
    kdv(fiyat,kdvU)






