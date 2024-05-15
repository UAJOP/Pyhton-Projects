print("...BİR SAYI GİREBİLİRSİNİZ...\n"
          "..EGER PROGRAMDAN ÇIKMAK İSTİYORSANIZ 0 DEĞERİNİ GİRİNİZ..")
while True:
    sayı =  int(input("Lütfen bir sayı giriniz :"))
    if sayı==0:
        print(".......Program Sonlanıyor......")
        break
    if sayı%2==0:
        print("Sayınız çifttir")
    elif sayı%2==1:
        print("Sayınız tektir")
    else:
        print("Tam sayı giriniz")