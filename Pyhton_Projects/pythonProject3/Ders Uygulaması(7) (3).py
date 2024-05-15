from tkinter import *

sozluk = {"kitap":"book",
          "masa":"table",
          "bilgisayar":"computer"}

pen = Tk()
pen.geometry("200x200")
pen.title("Çeviri Uygulaması")
result = Label(pen,text="")
def kontrol():
    kelime =kelimeEntry.get()

    if kelime in sozluk:
        ingilizce_kelime = sozluk[kelime]
        result["text"]= f"{kelime}'nin İngilizcesi {ingilizce_kelime}"
    else:
        result["text"]= f"{kelime}'nin İngilizcesi bulunamadı"


kelimeEntry = Entry(pen)
kontrolButton = Button(pen,text="Çevir",command=kontrol)

kelimeEntry.grid(row=0,column=0,sticky=W)
kontrolButton.grid(row=1,column=0,sticky=W)
result.grid(row=2,column=0,sticky=W)
pen.mainloop()