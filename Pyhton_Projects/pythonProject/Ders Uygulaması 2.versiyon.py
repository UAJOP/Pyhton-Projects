ogrenciler= ["Burak","Cansel","Çağatay","Cansu"]

def ogrencileriAyir(ogrenciListesi):
    tek=[]
    cift=[]
    tümListe=[]
    for i, item in enumerate(ogrenciListesi):
        if i %2==0:
            cift.append(item)
        else:
            tek.append(item)
    tümListe.append(tek)
    tümListe.append(cift)
    return tümListe

liste=ogrencileriAyir(ogrenciler)
print(liste)
print("tekler",liste[0])
print("ciftler",liste[1])