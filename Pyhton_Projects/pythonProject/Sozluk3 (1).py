menu= {
    "sucuklu_yumurta":25,
    "peynir_tabagi":15,
    "menemen":20,
    "izgara_tavuk":30,
    "köfte": 50,
    "balik": 36
}

while True:
    secim=int(input("Yapmak istediğiniz işlemi girin"))
    if secim==1:
        secilenYemek = input("Lütfen Yemek Seçiniz")
        if secilenYemek in menu:
            fiyat= menu[secilenYemek]
            print(f"{secilenYemek} fiyatı,{fiyat}")
        else:
            print("Seçtiğiniz yemek menümüzde yok")
    elif secim==2: #Ekle
        yemek=input("eklemek istediğiniz yemeği girin")
        fiyat=float(input("fiyatını giriniz"))
        try:
            menu[yemek]=fiyat
            print(f"{yemek},eklendi")
        except ValueError:
            print("Fiyat bilgisinde hata var!")
    elif secim==3: #Sil
        silinecek_yemek = input("Yemek giriniz")
        if silinecek_yemek in menu:
            menu.pop(silinecek_yemek)
            print(f"{silinecek_yemek}, silindi")
        else:
            print("Silinecek yemek hatalı")