urunBedeli = 500
kdv1 = 1
kdv2=10
kdv3=20

kdv1Degeri = urunBedeli*kdv1/100
kdv2Degeri = urunBedeli*kdv2/100
kdv3Degeri = urunBedeli*kdv3/100

kdv1Dahil = urunBedeli + kdv1Degeri
kdv2Dahil = urunBedeli + kdv2Degeri
kdv3Dahil = urunBedeli + kdv3Degeri

print("""Bedeli {} olan %1 KDV değeği {} ve KDV Dahil {}
%10 KDV değeği {} ve KDV Dahil {}
%20 KDV değeği {} ve KDV Dahil {}
""".format(urunBedeli,kdv1Degeri,kdv1Dahil,kdv2Degeri,kdv2Dahil,kdv3Degeri,kdv3Dahil))

#UYGULAMA - 2 FAİZ HESAPLAMA

anapara = 500000
günlükFaizOrani= 40
gün = 32 # Parayı kaç gün koyacağım

günlükFaizGetirisi = (anapara/100)*(günlükFaizOrani/365)*gün

