#UYGULAMA - 1

bakiye = 5000

while True:
    islem = int(input("""
    Yapmak istediğiniz işlemi seçiniz
    0- Çıkış
    1- Bakiye Sorgula
    2- Para Yatır\n
    """))
    if islem==0:
        print("İşlem sonladırıldı")
        break
    elif islem==1:
        print(f"Bakiyeniz {bakiye}")
        #print("Bakiyeniz {}".format(bakiye))
        #print("Bakiyeniz", bakiye)
    elif islem==2:
        miktar = float(input("Yatırmak istediğiniz değeri girin"))
        bakiye = bakiye+miktar
        print(f"Güncel bakiyeniz {bakiye}")
    elif islem==3:
        miktar = float(input("Çekmek istediğiniz değeri girin"))
        if miktar>bakiye:
            print("Çekmek istediğiniz tutar bakiyenizden yüksek")
        else:
            bakiye = bakiye-miktar
            print(f"Güncel bakiyeniz {bakiye}")
    else:
        print("Lütfen sadece belirtilen işlemleri seçiniz")


#UYGULAMA - 2
tekSayisi = 0
ciftSayisi = 0
sayılar = list()
while True:
    sayı = int(input("Sayınızı giriniz : "))
    if sayı == 0:
        print("Girdiğniz Sayılar", sayılar)
        print("Tek Sayılarınızın Sayısı:",tekSayisi)
        print("Çift Sayılarınızın Sayısı:", ciftSayisi)
        break
    else:
        sayılar.append(sayı)
        if sayı%2==0:
            ciftSayisi=ciftSayisi+1
            #tekSayisi+=1
        elif sayı%2==1:
            tekSayisi = tekSayisi+1
