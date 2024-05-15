# teklerSayısı = 0
# cıftlerSayısı = 0
# for item in range (0,101,1):
#     if item%2==0:
#         cıftlerSayısı=cıftlerSayısı+1
#     else:
#         teklerSayısı+=1
# print("Tekler Sayısı",teklerSayısı)
# print("Çiftler Sayısı",cıftlerSayısı)1



baslangıc = int ( input ( "BAŞLANGIÇ DEĞERİ GİRİNİZ :" ) )
bitis = int(input("BİTİŞ DEĞERİ GİRİNİZ"))
ciftlerListesi = list()
teklerListesi = list()
if baslangıc < bitis:
    for i in range (baslangıc,bitis+1,1):
        if i%2==0:
            ciftlerListesi.append(i)
        elif i%2==1:
            teklerListesi.append(i)
elif baslangıc > bitis:
    for i in range(baslangıc,bitis-1,-1):
        if i%2==0:
            ciftlerListesi.append(i)
        elif i%2==1:
            teklerListesi.append(i)
else:
    print("BAŞLANGIÇ VE BİTİŞ DEĞERİNİ FARKLI GİRİN !!")

print("Tekler",teklerListesi)
print("Çiftler",ciftlerListesi)

print(f"Çift Adedi {len(ciftlerListesi)}")
print(f"Tek Adedi {len(teklerListesi)}")

print("""
Minimum Tek {}
Minimum Çift {}

Max Tek {}
Max Çift {}
""".format(min(teklerListesi),min(ciftlerListesi),max(teklerListesi),max(ciftlerListesi)))

