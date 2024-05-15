from tkinter import *
pen = Tk()
pen.geometry("330x300")
pen.config(bg="pink")
myFont=Font=("Helvatica",16)
elmA1=Label(pen,text="Elma",bg="pink",fg="red",font=myFont)
muz1=Label(pen,text="Muz",bg="pink",fg="yellow",font=myFont)
portakal1=Label(pen,text="Portokal",bg="pink",fg="orange",font=myFont)

elma2=Label(pen,text="",bg="pink")
muz2=Label(pen,text="",bg="pink")
portakal2=Label(pen,text="",bg="pink")

def temizle():
    elma2["text"]=""
    muz2["text"]=""
    portakal2["text"] = ""
    muz2["bg"] = "pink"

    elma2["bg"] = "pink"

    portakal2["bg"] = "pink"

def degis1():
    elma2["text"]="APPLE"
    elma2["bg"]="red"
    elma2["fg"]="pink"
def degis2():
    muz2["text"]="BANANA"
    muz2["bg"]="yellow"
    muz2["fg"]="pink"
def degis3():
    portakal2["text"]="ORANGE"
    portakal2["bg"]="orange"
    portakal2["fg"]="pink"


ogren1=Button(pen,text="ÖĞREN",borderwidth=5,width=25,command=degis1)
ogren2=Button(pen,text="ÖĞREN",borderwidth=5,width=25,command=degis2)
ogren3=Button(pen,text="ÖĞREN",borderwidth=5,width=25,command=degis3)


clearButton =Button(pen,text="Temizle",borderwidth=5,width=25,command=temizle)

ogren1.grid(row=0,column=2,sticky=W)
ogren2.grid(row=1,column=2,sticky=W)
ogren3.grid(row=2,column=2,sticky=W)


clearButton.grid(row=4,column=2,sticky=W)

elmA1.grid(row=0,column=0,sticky=W)
muz1.grid(row=1,column=0,sticky=W)
portakal1.grid(row=2,column=0,sticky=W)

elma2.grid(row=0,column=3,sticky=W)
muz2.grid(row=1,column=3,sticky=W)
portakal2.grid(row=2,column=3,sticky=W)

pen.mainloop()