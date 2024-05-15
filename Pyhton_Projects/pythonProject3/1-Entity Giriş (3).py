#Entry Widget

from tkinter import *

pen = Tk()
pen.geometry("400x400")
resultLabel = Label(pen,text="")
def clearEntry():
    nameEntry.delete(0,END)

def getir():
    ad = nameEntry.get()
    resultLabel["text"]=f"Hoş geldin {ad}"
    clearEntry()

nameEntry = Entry(pen,width=50, borderwidth=10, bg="blue",fg="white")
getirButton = Button(pen,text="Getir",width=10,command=getir)

nameEntry.grid(row=0, column=0,sticky=W)
getirButton.grid(row=1,column=0,sticky=W)
resultLabel.grid(row=2,column=0,sticky=W)

pen.mainloop()