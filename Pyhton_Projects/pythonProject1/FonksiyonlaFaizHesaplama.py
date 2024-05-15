f1=32
f2=34
f3 = 40


def gunlukFaizHesapka(anaPara,gun):
    faizGetirisi = (anaPara/100)*(f1/365)*gun
    return faizGetirisi

def aylıkFaizHesapla(anaPara,ay):
    faizGetirisi =(anaPara/100)*(f2/365)*ay
    return faizGetirisi

def yillikFaizHesapla(anaPara,yil):
    faizGetirisi =(anaPara/100)*(f3/365)*yil
    return faizGetirisi

while True:
    print("\nFaiz hesaplama Programına HOŞ GELDİNİZ!!")
    print("1. Günlük Faiz Hesapla")
    print("2. Aylık Faiz Hesapla")
    print("3. Yıllık Faiz Hesapla")
    print("4. Çıkış")
    secim = input("Seçiminiz (1/2/3/4): ")
    if secim == "1":
        anaParan = int(input("Lütfen anapara değerini giriniz :"))
        gun = int(input("Lütfen bankamızda paranızı kaç gün tutucağınızı giriniz :"))
        faizgetirisi1 = gunlukFaizHesapka(anaParan,gun)
        toplam1=anaParan+faizgetirisi1
        print(f"Günlük Faiz Oranınız : {faizgetirisi1} toplam paranız : {toplam1}")
    elif secim == "2":
        anaParan = int(input("Lütfen anapara değerini giriniz :"))
        ay = int(input("Lütfen bankamızda paranızı kaç ay tutucağınızı giriniz :"))
        faizgetirisi2 = aylıkFaizHesapla(anaParan,ay)
        toplam2 =anaParan+faizgetirisi2
        print(f"Aylık Faiz Oranınız : {faizgetirisi2} toplam paranız : {toplam2}")

    elif secim == "3":
        anaParan = int(input("Lütfen anapara değerini giriniz :"))
        yıl = int(input("Lütfen bankamızda paranızı kaç yıl tutucağınızı giriniz :"))
        faizgetirisi3 = yillikFaizHesapla(anaParan,yıl)
        toplam3 =anaParan+faizgetirisi3
        print(f"Yıllık Faiz Oranınız : {faizgetirisi3} toplam paranız : {toplam3}")
    elif secim == "4":
        print("UYGULAMADAN ÇIKILIYOR....")
        break

    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")