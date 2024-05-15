anaPara = float(input("Lütfen Paranızı Giriniz :"))
print("ANA PARANIZ =", anaPara)
gunlukFaiz = 20
gun = int(input("Kaç gün bankamızda paranızı tutucaksınız :"))
faiz = (anaPara / 100) * (gunlukFaiz / 365) * gun
print("Anaparanız", anaPara, gun, "gün için faiz oranı ", faiz, "olacaktır")
sonpara = faiz + anaPara
sonpara = int(sonpara)
print("Son Paranız :", sonpara)




