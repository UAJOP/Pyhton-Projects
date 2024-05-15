from tkinter import *
pen = Tk()
pen.geometry("400x400")
pen.config(bg="pink")
myFont=Font=("Helvatica",16)
oneLabel = Label(pen,text="",bg="pink")
def temizle():
    oneLabel["text"]=""
def tıkla():
    oneLabel["text"]="Butona Tıklandı"
    oneLabel["bg"]="pink"
    oneLabel["fg"]="yellow"
    oneLabel["font"]=myFont

clickButton = Button(pen,text="Tıkla",borderwidth=5,width=25,command=tıkla)
clearButton =Button(pen,text="Temizle",borderwidth=5,width=25,command=temizle)

clearButton.grid(row=1,column=1,sticky=W)
oneLabel.grid(row=0,column=0,sticky=W)
clickButton.grid(row=1,column=0,sticky=W)


pen.mainloop()

