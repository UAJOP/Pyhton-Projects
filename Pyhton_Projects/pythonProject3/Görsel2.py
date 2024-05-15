from tkinter import *

pen= Tk()
pen.title("Üye Formu")

pen.resizable(width=False,height=True)
pen.config(bg="pink")

ekran_genislik=pen.winfo_screenwidth()
ekran_boy=pen.winfo_screenheight()
en = 400
boy=400
x= (ekran_genislik-en)//2
y= (ekran_boy-boy)//2
pen.geometry(f"{en}x{boy}+{x}+{y}")

#widget

#Label -> üzerine veri ya da bilgi eklenen obje

adLabel = Label(pen,text="Burak",bg="yellow",fg="black")
soyadLabel = Label(pen,text="Evren",bg="yellow",fg="black")
#Pencereye Yerleştirme Yöntemleri

#adLabel.pack()
#adLabel.place(x=50,y=50)
adLabel.grid(row=0,column=0)
soyadLabel.grid(row=1,column=0)
pen.mainloop()