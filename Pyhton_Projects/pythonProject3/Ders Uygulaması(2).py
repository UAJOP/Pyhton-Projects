from tkinter import *
pen=Tk()
pen.title("Anasayfa")
pen.geometry("400x400")
pen.attributes("-alpha",0.9)
sonucLabel  =Label(pen,text="")
myFont= ("Helvetica",16,"italic","bold")
def elmaOgren():
    sonucLabel["text"]="APPLE"
    sonucLabel["font"]=("Helvetica",20,"bold")
    sonucLabel["bg"]="red"
def muzOgren():
    sonucLabel["text"]="BANANA"
    sonucLabel["font"] = ("Helvetica", 20, "bold")
    sonucLabel["bg"] = "yellow"
def portakalOgren():
    sonucLabel["text"]="ORANGE"
    sonucLabel["font"] = ("Helvetica", 20, "bold")
    sonucLabel["bg"] = "orange"

elmaLabel = Label(pen,text="Elma",font=myFont)
muzLabel = Label(pen,text="Muz",font=myFont)
portakalLabel = Label(pen,text="Portakal",font=myFont)

elmaButton = Button(pen,text="Öğren",command=elmaOgren)
muzButton = Button(pen,text="Öğren",command=muzOgren)
portakalButton = Button(pen,text="Öğren",command=portakalOgren)


elmaLabel.grid(row=0,column=0,sticky=W)
muzLabel.grid(row=1,column=0,sticky=W)
portakalLabel.grid(row=2,column=0,sticky=W)

elmaButton.grid(row=0,column=1,sticky=E)
muzButton.grid(row=1,column=1,sticky=E)
portakalButton.grid(row=2,column=1,sticky=E)

sonucLabel.grid(row=1,column=2)
pen.mainloop()