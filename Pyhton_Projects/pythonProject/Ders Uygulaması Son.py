def cumleDegis(cumle):
    yeni_cumle=""
    for i,item in enumerate(cumle):
        if i%2==0:
            yeni_cumle+=item.lower()

        else:
            yeni_cumle+=item.upper()
    
    return  yeni_cumle

myString="merHaba BuGÜn PYTHon Dersi var Ve Ben Çok SEVİyoRuM"
print(cumleDegis(myString))
