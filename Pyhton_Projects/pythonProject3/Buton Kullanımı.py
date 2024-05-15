#Button
from tkinter import *
pen= Tk()
pen.geometry("400x400")
pen.config(bg="pink")
pen.attributes("-alpha",0.9)
myFont=("Helvetica",16,"bold","italic")

myLabel = Label(pen, text="",bg="pink")
def tıkla():
    myLabel["text"]="Butona Tıklandı"
    myLabel["bg"]="pink"
    myLabel["font"]=myFont
    #myLabel.config(text="Butona Basıldı")
def temizle():
    myLabel["text"]=""
    myLabel["bg"]="pink"

clickButton = Button(pen,text="Tıkla",borderwidth=5, width=25,command=tıkla)
clearButton = Button(pen,text="Temizle",borderwidth=5, width=25,command=temizle)

clickButton.grid(row=0,column=0,sticky=W)
clearButton.grid(row=0,column=1,sticky=W)
myLabel.grid(row=1, column=0, sticky=W)

pen.mainloop()