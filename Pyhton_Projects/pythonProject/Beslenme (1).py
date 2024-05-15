isimler = ["Burak","Cem","Rabia","Doğukan"]
yiyecekler = ["Elma","Burger","Salata","Yumurta","Pizza","Kebap"]
tekİsim= []
ciftİsim = []
tekYiyecek= []
ciftYiyecek=[]
while True:
    isim = input("Adınızı Giriniz")

    for index, item in enumerate(yiyecekler):
        if index%2==0:
            ciftYiyecek.append(item)
        else:
            tekYiyecek.append(item)

    if isim in isimler:
        for index,item in enumerate(isimler):
            if item==isim:
                print(index)
                if index%2==0:
                    print(f"{isim} yiyebilir {ciftYiyecek}")
                else:
                    print(f"{isim} yiyebilir {tekYiyecek}")






