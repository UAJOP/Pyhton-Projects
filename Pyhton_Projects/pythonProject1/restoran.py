menu = {
    "Sucuklu_yumurta":65,
    "peynir_tabağı":90,
    "menemen":45,
    "ızgara_tavuk":80,
    "köfte":100,
    "beyran":120}
def yemek_ekle (menu):
    try:
        ekle = input("Eklemek İstediğiniz yemeği giriniz :")
        para = int(input("Eklediğiniz yemeğin fiyatını giriniz :"))
        if ekle in menu:
            print(f"{ekle},menümüzde zaten var!")
        else:
            menu[ekle]=para
            print("Yemek başarıyla Eklendi...")
    except ValueError:
        print("Fiyat değeri tam sayı olmalıdır")

def menuyu_goster (menu):
    for yemek,fiyat in menu.items():
        print(f"{yemek}={fiyat}Tl")

def yemek_sil (menu):
    sil = input("Silmek istediğiniz yemeği girin: ")
    if sil in menu:
        menu.pop(sil)
        print(f"{sil},başarıyla silindi.")
    else:
        print(f"{sil},menude bulunamadı.")

while True:
    print("\nRESTORAN")
    print("1. Yemek Ekle")
    print("2. Menu")
    print("3. Yemek Sil")
    print("4. Çıkış")
    islem = input("Seçiminiz (1/2/3/4): ")
    if islem == "1":
        yemek_ekle(menu)
    elif islem == "2":
        menuyu_goster(menu)
    elif islem == "3":
        yemek_sil(menu)
    elif islem == "4":
        print("UYGULAMADAN ÇIKILIYOR....")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")