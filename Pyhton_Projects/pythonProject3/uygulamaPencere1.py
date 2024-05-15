from tkinter import *

pen =Tk()
pen.title("MENU")
pen.geometry("400x400")


def ıkıncıpen():
    myFont = ("Helvetica", 5, "italic", "bold")
    win= Toplevel()
    win.title("Hakkında")
    win.geometry("400x400")
    hakkındalabel = Label(win, text="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.", font=myFont)
    hakkındalabel.grid(row=0, column=0, sticky=W)
    win.mainloop()

def ucuncupen():
    wun= Toplevel()
    wun.title("Toplama UYGULAMASI")
    wun.geometry("400x400")
    resultLabel = Label(wun, text="")
    def clearEntry():
        number1Entry.delete(0, END)
        number2Entry.delete(0, END)

    def getir():
        sayı1 = int(number1Entry.get())
        sayı2 = int(number2Entry.get())
        toplam = sayı1 + sayı2
        resultLabel["text"] = f"sonucunuz {toplam}"
        clearEntry()

    number1Entry = Entry(wun, width=25, borderwidth=10, bg="red", fg="white")
    number2Entry = Entry(wun, width=25, borderwidth=10, bg="red", fg="white")
    getirButton = Button(wun, text="Hesapla", width=20, command=getir)
    number1Entry.grid(row=0, column=0, sticky=W)
    number2Entry.grid(row=1, column=0, sticky=W)
    getirButton.grid(row=2, column=0, sticky=W)
    resultLabel.grid(row=3, column=0, sticky=W)
    wun.mainloop()


def dorduncupen():
    wan= Toplevel()
    wan.title("Çıkarma Uygulaması")
    wan.geometry("400x400")
    resultLabel = Label(wan, text="")
    def clearEntry():
        number1Entry.delete(0, END)
        number2Entry.delete(0, END)
    def getir():
        sayı1 = int(number1Entry.get())
        sayı2 = int(number2Entry.get())
        toplam = sayı1 - sayı2
        resultLabel["text"] = f"sonucunuz {toplam}"
        clearEntry()
    number1Entry = Entry(wan, width=25, borderwidth=10, bg="blue", fg="white")
    number2Entry = Entry(wan, width=25, borderwidth=10, bg="blue", fg="white")
    getirButton = Button(wan, text="Hesapla", width=20, command=getir)
    number1Entry.grid(row=0, column=0, sticky=W)
    number2Entry.grid(row=1, column=0, sticky=W)
    getirButton.grid(row=2, column=0, sticky=W)
    resultLabel.grid(row=3, column=0, sticky=W)
    wan.mainloop()

def besincipen():
    won = Toplevel()
    won.title("Çarpma Uygulaması")
    won.geometry("400x400")
    resultLabel = Label(won, text="")

    def clearEntry():
        number1Entry.delete(0, END)
        number2Entry.delete(0, END)

    def getir():
        sayı1 = int(number1Entry.get())
        sayı2 = int(number2Entry.get())
        toplam = sayı1 * sayı2
        resultLabel["text"] = f"sonucunuz {toplam}"
        clearEntry()

    number1Entry = Entry(won, width=25, borderwidth=10, bg="purple", fg="white")
    number2Entry = Entry(won, width=25, borderwidth=10, bg="purple", fg="white")
    getirButton = Button(won, text="Hesapla", width=20, command=getir)
    number1Entry.grid(row=0, column=0, sticky=W)
    number2Entry.grid(row=1, column=0, sticky=W)
    getirButton.grid(row=2, column=0, sticky=W)
    resultLabel.grid(row=3, column=0, sticky=W)
    won.mainloop()




def altincipen():
    wen = Toplevel()
    wen.title("Bölme Uygulaması")
    wen.geometry("400x400")
    resultLabel = Label(wen, text="")

    def clearEntry():
        number1Entry.delete(0, END)
        number2Entry.delete(0, END)

    def getir():
        sayı1 = int(number1Entry.get())
        sayı2 = int(number2Entry.get())
        toplam = sayı1 / sayı2
        resultLabel["text"] = f"sonucunuz {toplam}"
        clearEntry()

    number1Entry = Entry(wen, width=25, borderwidth=10, bg="green", fg="white")
    number2Entry = Entry(wen, width=25, borderwidth=10, bg="green", fg="white")
    getirButton = Button(wen, text="Hesapla", width=20, command=getir)
    number1Entry.grid(row=0, column=0, sticky=W)
    number2Entry.grid(row=1, column=0, sticky=W)
    getirButton.grid(row=2, column=0, sticky=W)
    resultLabel.grid(row=3, column=0, sticky=W)
    wen.mainloop()



ılkmenu = Menu(pen)
pen.config(menu=ılkmenu)

Bilgi = Menu(ılkmenu)
Hesap= Menu(ılkmenu)

ılkmenu.add_cascade(label="Hakkında",menu=Bilgi)
ılkmenu.add_cascade(label="Hesap",menu=Hesap)

Bilgi.add_cascade(label="Hakkında",command=ıkıncıpen)
Bilgi.add_cascade(label="Close Window",command=pen.quit)
Hesap.add_cascade(label="Toplama",command=ucuncupen)
Hesap.add_cascade(label="Çıkarma",command=dorduncupen)
Hesap.add_cascade(label="Çarpma",command=besincipen)
Hesap.add_cascade(label="Bölme",command=altincipen)
pen.mainloop()