
"""BANKA UYGULAMASI"""


bakiye =float(input("Lütfen Mevcut Bakiyenizi Giriniz :"))
while True:
    işlem = int(input("""
0- ÇIKIŞ
1-BAKİYE SORGULA
2-PARA ÇEK
3-PARA YATIR
LÜTFEN HANGİ İŞLEMİ UYGULAMAK İSTEDİĞİNİZİ SEÇİNİZ :"""))
    if işlem==0:
        print(".....Program Sonlanıyor.....")
        break

    elif  işlem==1:
        print("GÜNCEL BAKİYE =",bakiye)

    elif işlem==2:
        cekilcek =float(input("NE KADAR PARA ÇEKİCEKSİNİZ :"))
        if cekilcek>bakiye:
            print("BAKİYE YETERSİZ")
        else:
            bakiye =bakiye-cekilcek
            print("GÜNCEL BAKİYE =",bakiye)


    elif işlem==3:
        yatırılcak=float(input("NE KADAR PARA YATIRCAKSINIZ :"))
        bakiye=yatırılcak+bakiye
        print("GÜNCEL BAKİYE =",bakiye)
    else:
        print("****LÜTFEN SADECE BELİRTİLEN İŞLEMLERİ SEÇİNİZ****")


"""TEK ÇİFT SAYILAR"""


tekSayılar = 0
ciftSayılar = 0
sayılar =list()
while True:
    sayı =int(input("Sayınızı Giriniz :"))

    if  sayı== 0:
        print("Girginiz Sayılar",sayılar)
        print("Tek Sayılarınızın Sayısı :",tekSayılar)
        print("Çift Sayılarınızın Sayısı :",ciftSayılar)
        break
    else:
        sayılar.append(sayı)
        if sayı%2==0:
            ciftSayılar=ciftSayılar+1
        elif sayı%2==1:
            tekSayılar = tekSayılar+1