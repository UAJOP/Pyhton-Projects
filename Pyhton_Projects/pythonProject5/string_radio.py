from tkinter import *

pen = Tk()
pen.geometry("400x400")


myLabel = Label(pen,text="")

def kontrol():
    if v.get()=="k":
        myLabel["text"]="Kadın Seçtiniz"
    elif v.get()=="e":
        myLabel["text"]="Erkek Seçtiniz"
    elif  v.get()=="d":
        myLabel["text"]="Diğer Seçtiniz"

v = StringVar()

v.set("sd")

radiobtn1 = Radiobutton(pen,text="Kadın",variable=v,value="k")
radiobtn2 = Radiobutton(pen,text="Erkek",variable=v,value="e")
radiobtn3 = Radiobutton(pen,text="Diğer",variable=v,value="d")

kontrolbtn = Button(pen,text="Kontrol",command=kontrol)

radiobtn1.grid(row=0,column=0,sticky=W,padx=10,pady=10)
radiobtn2.grid(row=1,column=0,sticky=W,padx=10,pady=10)
radiobtn3.grid(row=2,column=0,sticky=W,padx=10,pady=10)

kontrolbtn.grid(row=3,column=0,sticky=W,padx=10,pady=10)

myLabel.grid(row=4,column=0,sticky=W,padx=10,pady=10)

pen.mainloop()