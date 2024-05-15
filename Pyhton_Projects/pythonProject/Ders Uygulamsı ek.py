def hesapla(sayılarListesi):
    sonuc=[]
    for i, item in enumerate(sayılarListesi):
        if i%2==0:
            sayılarListesi[i]= sayılarListesi[i]+sayılarListesi[i]*10/100
        else:
            sayılarListesi[i]= sayılarListesi[i]-sayılarListesi[i]*10/100
    for item in sayılarListesi:
        if item>=50:
            sonuc.append(item)
    return sonuc
sayılar = [36,78,65,42,98,64,85]
sonuc= hesapla(sayılar)
print(sonuc)
