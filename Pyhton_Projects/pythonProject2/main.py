from tkinter import *

pen= Tk()
pen.title("Üye Formu")

pen.resizable(width=False,height=False)
pen.config(bg="MediumPurple2")


ekran_genislik = pen.winfo_screenwidth()
ekran_boy=pen.winfo_screenheight()
en=800
boy=600
x = (ekran_genislik-en)//2
y = (ekran_boy-boy)//2

pen.geometry(f"{en}x{boy}+{x}+{y}")

#WİDGETLAR


#LABEL -> ÜZERİNE VERİ EKLEMEK İÇİN

adLabel = Label(pen,text="KAAN",bg="Thistle1",fg="Black")
soyadLabel = Label(pen,text="BALCI")
#PENCEREYE YERLEŞTİRME YÖNTEMLERİ

#adLabel.pack()
#adLabel.place(x=360,y=300)
adLabel.grid(row=0,column=0)
soyadLabel.grid(row=1,column=0)











pen.mainloop()