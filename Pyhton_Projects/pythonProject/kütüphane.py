kutuphaneKitaplar = {
    "Kitap1": 50,
    "Kitap2": 60
}
kullanicilar = {
    "admin": 123
}
kullaniciKitap = {}


def kayit():
    isim_ekle = input("Kullanıcı Adı: ")
    sifre_ekle = int(input("Kullanıcı Şifre: "))
    kullanicilar[isim_ekle] = sifre_ekle #kullanıcılar sözlüğüne git [] ile key'i belirt = ile karşılık gelen value belirt
    print("Kayıt Oluşturuldu!")


def kutuphane():
    bakiye = 0

    while True:
        islem = int(input("""
        Yapmak istediğiniz işlemi seçiniz
        0- Çıkış
        1- Kütüphanedeki Kitapları Göster
        2- Bakiye İşlemleri
        3- Kütüphaneden Kitap Al
        4- Kütüphaneye Kitap Ver
        5- Benim Kitaplarımı Göster
        ==
        """))

        if islem == 0:
            print("İşlem sonladırıldı,Hoşçakal...")
            break

        elif islem == 1:
            print(f"Kütüphanedeki kitaplar: {kutuphaneKitaplar}")

        elif islem == 2:
            while True:
                bakiye_islem = int(input("""
                Yapmak istediğiniz işlemi seçiniz
                0- Çıkış
                1- Bakiye Sorgula
                2- Para Yatır
                ==
                """))

                if bakiye_islem == 0:
                    print("İşlem sonlandırıldı")
                    break

                elif bakiye_islem == 1:
                    print(f"Bakiyeniz: {bakiye}")

                elif bakiye_islem == 2:
                    miktar = float(input("Yatırmak istediğiniz miktarı girin: "))
                    if miktar < 0:
                        print("Negatif miktar giremezsiniz.")
                    else:
                        bakiye += miktar
                        print(f"Güncel bakiyeniz: {bakiye}")

                else:
                    print("Lütfen sadece belirtilen işlemleri seçiniz!!")

        elif islem == 3:
            print("Kütüphanedeki kitaplar :", kutuphaneKitaplar)
            sil = input("Almak İstediğiniz Kitap Hangisi : ")
            if sil in kutuphaneKitaplar and bakiye >= kutuphaneKitaplar[sil]:
                kullaniciKitap[sil] = kutuphaneKitaplar.pop(sil)
                bakiye=bakiye-kullaniciKitap[sil]
                print("Güncel Bakiyeniz :",bakiye)
                print("İyi okumalar!")
            elif sil in kutuphaneKitaplar and bakiye < kutuphaneKitaplar[sil]:
                print("Yetersiz bakiye!")
            else:
                print(f"{sil}, kütüphanemizde mevcut değil!")

        elif islem == 4:
            print(kullaniciKitap)
            kitap = input("Vermek istediğiniz kitabın ismi : ")
            if kitap in kullaniciKitap:
                kutuphaneKitaplar[kitap] = kullaniciKitap.pop(kitap)
                print("Başarıyla teslim ettiniz!")
            else:
                print("Kitap sizde yok!")

        elif islem == 5:
            print("Kitaplarınız :", kullaniciKitap)

        else:
            print("Lütfen sadece belirtilen işlemleri seçiniz!")


def giris():
    kullanici_adi = input("Kullanıcı Adı: ")
    kullanici_sifre = int(input("Kullanıcı Şifre: "))
    if kullanici_adi in kullanicilar and kullanicilar[kullanici_adi] == kullanici_sifre:
        print("Giriş Başarılı! Hoş geldiniz, {}".format(kullanici_adi))
        kutuphane()
    else:
        print("Giriş Başarısız! Kullanıcı adı veya şifre hatalı.")


while True:
    islem = int(input("""
    *************************
    KÜTÜPHANEMİZE HOŞGELDİNİZ
    *************************
    Yapmak istediğiniz işlemi seçiniz
    0- Çıkış
    1- Giriş Yap
    2- Kayıt Ol
    ==
    """))

    if islem == 0:
        print("İşlem sonlandırıldı")
        break

    elif islem == 1:
        giris()

    elif islem == 2:
        kayit()

    else:
        print("LÜTFEN GEÇERLİ İŞLEMİ SEÇİN!!")
