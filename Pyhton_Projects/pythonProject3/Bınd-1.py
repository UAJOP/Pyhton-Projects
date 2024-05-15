from tkinter import *

pen = Tk()
pen.title("Bind Metodu İle Tepki(Event) Örnekleri")
pen.geometry("400x400")

def tikla(event):
    myLabel["text"]=f"Koordinatlar ({event.x},{event.y})"

def enterButton(event):
    myLabel["text"]="düğmenin üzerindesin"

def cikisButton(event):
    myLabel["text"]="Düğmeden çıkıldı"

def tusaBasma(event):
    myLabel["text"]=f"Basılan Tuş {event.keysym}"

myLabel = Label(pen,text="Olay Bekleniyor")
myButton = Button(pen,text="Kontrol")

myButton.bind("<Button-1>", tikla)
myButton.bind("<Enter>", enterButton)
myButton.bind("<Leave>", cikisButton)
#<Double-1> Çift Tıklama Event i
#<KeyRelease> Tuşu bırakma
#<Return> Enter Tuşu
pen.bind("<KeyPress>",tusaBasma)

myLabel.grid(row=0,column=0,padx=10,pady=10,sticky=W)
myButton.grid(row=1,column=0,padx=10,pady=10,sticky=W)


pen.mainloop()