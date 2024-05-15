while True:
    try:
        sayı1= int(input("Sayı 1 giriniz"))
        sayı2= int(input("Sayı 2 giriniz"))
        print(sayı1/sayı2)
    except ValueError:
        print("Girdiğiniz değerler sayısal ifadel olmalıdır")
    except ZeroDivisionError:
        print("Sayı 2 sıfır olamaz")