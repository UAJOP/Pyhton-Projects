from  tkinter import *

pen=Tk()
pen.title("TAKIMLAR")
pen.resizable(width=False,height=False)
pen.config(bg="Silver")
ekran_genislik = pen.winfo_screenwidth()
ekran_boy=pen.winfo_screenheight()
en=800
boy=600
x = (ekran_genislik-en)//2
y = (ekran_boy-boy)//2
pen.geometry(f"{en}x{boy}+{x}+{y}")

takımAd =Label(pen,text="Takım Adı",fg="Black")
kısaltma=Label(pen,text="KISALTMA",fg="Black")
renk1=Label(pen,text="RENK 1",fg="Black")
renk2=Label(pen,text="RENK 2",fg="Black")
galats=Label(pen,text="GALATASARAY")
GS=Label(pen,text="GS",fg="Black")
renk1gs=Label(pen,text="  ",bg="red")
renk2gs=Label(pen,text="  ",bg="yellow")
fener=Label(pen,text="FENERBAHÇE")
fb=Label(pen,text="FB",fg="Black")
renk1fb=Label(pen,text="  ",bg="yellow")
renk2fb=Label(pen,text="  ",bg="blue")
besiktas=Label(pen,text="BEŞİKTAŞ")
bjk=Label(pen,text="BJK",fg="Black")
renk1bjk=Label(pen,text="  ",bg="BLACK")
renk2bjk=Label(pen,text="  ",bg="Snow1")

takımAd.grid(row=0,column=0)
kısaltma.grid(row=0,column=1)
renk1.grid(row=0,column=2)
renk2.grid(row=0,column=3)
galats.grid(row=1,column=0)
GS.grid(row=1,column=1)
renk1gs.grid(row=1,column=2)
renk2gs.grid(row=1,column=3)
fener.grid(row=2,column=0)
fb.grid(row=2,column=1)
renk1fb.grid(row=2,column=2)
renk2fb.grid(row=2,column=3)
besiktas.grid(row=3,column=0)
bjk.grid(row=3,column=1)
renk1bjk.grid(row=3,column=2)
renk2bjk.grid(row=3,column=3)



pen.mainloop()