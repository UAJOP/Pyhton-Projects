from math import *
# print(ceil(5.6))
# print(floor(5.6))
# print(factorial(5))
# print(pow(5,2))
# print(sqrt(16))

while True:
    try:
        sayi1 = int(input("Sayı 1 i giriniz :"))
        sayi2 =int(input("Sayı 2 i giriniz :"))
        print(sayi1/sayi2)
    except ValueError:
        print("SADECE İNT DEĞERLERİ GİRİNİZ!")

    except ZeroDivisionError:
         print("2. SAYI 0 OLAMAZ")


    except Exception as e:
        print("Hatanız :", e)
