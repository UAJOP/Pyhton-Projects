#FAİZ UYGULAMASI
f1=32 #gunluk faiz oranı
f2=34 #aylık faiz oranı
f3=40 #yıllık faiz oranı

def gunlukFaizHesapla(anapara,gun):
    faizGetirisi = (anapara/100)*(f1/365)*gun
    return faizGetirisi

def aylıkFaizHesapla(anapara,ay):
    faizGetirisi = (anapara/100)*(f2/12)*ay
    return faizGetirisi

def yillikFaizHesapla(anapara,yil):
    faizGetirisi = (anapara/100)*(f3)*yil
    return faizGetirisi

while True:
    islem=int(input("""
    0- Çıkış
    1- Günlük Faiz
    2- Aylık Faiz
    3- Yıllık Faiz
    
    """))
    if islem==1:
        anapara = int(input("Anaparanızı Giriniz"))
        gun = int(input("Gün Değerini Giriniz"))
        faizGetirisi = gunlukFaizHesapla(anapara,gun)
        toplam = anapara+faizGetirisi
        print(f"Faiz Getiriniz {faizGetirisi},Toplam {toplam}")

