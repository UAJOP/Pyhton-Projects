# Entry Widget

from tkinter import *

pen = Tk()
pen.geometry("400x400")
resultLabel = Label(pen, text="")


def clearEntry():
    number1Entry.delete(0,END)
    number2Entry.delete(0,END)


def getir():
    sayı1 = int(number1Entry.get())
    sayı2 = int(number2Entry.get())
    toplam = sayı1+sayı2
    resultLabel["text"]=f"sonucunuz {toplam}"
    clearEntry()

number1Entry = Entry(pen, width=25, borderwidth=10, bg="blue", fg="white")
number2Entry = Entry(pen, width=25, borderwidth=10, bg="blue", fg="white")
number1Entry.insert(0,"Sayı1 Giriniz")
number2Entry.insert(0,"Sayı2 giriniz")
getirButton = Button(pen, text="Hesapla", width=20, command=getir)

number1Entry.grid(row=0, column=0, sticky=W)
number2Entry.grid(row=1, column=0, sticky=W)
getirButton.grid(row=2, column=0, sticky=W)
resultLabel.grid(row=3, column=0, sticky=W)

pen.mainloop()