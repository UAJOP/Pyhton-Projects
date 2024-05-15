ogrenciler= ["Burak","Cansel","Çağatay","Cansu"]
def ogrencileriAyir(ogrenciListesi):
    tek=[]
    cift=[]
    for i, item in enumerate(ogrenciListesi):
        if i %2==0:
            cift.append(item)
        else:
            tek.append(item)
    return tek,cift

tek,cift=ogrencileriAyir(ogrenciler)
print("Tekler",tek)
print("Çiftler",cift)