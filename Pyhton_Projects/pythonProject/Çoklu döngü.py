while True:
    sayı = int(input("Sayı değeri"))
    if sayı == 0:
        break
    if sayı%2==0:
        print("Sayınız çifttir")
    elif sayı%2==1:
        print("Sayınız tektir")

