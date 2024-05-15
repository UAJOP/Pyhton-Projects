from tkinter import *
pen = Tk()
pen.title("Menu")
pen.geometry("400x400")

def yeni_pencere_ac():
    win= Toplevel()
    win.title("Yeni pen")
    win.geometry("400x400")
    win.mainloop()

myMenu = Menu(pen)
pen.config(menu=myMenu)

fileMenu = Menu(myMenu)
editMenu = Menu(myMenu)

myMenu.add_cascade(label="File",menu=fileMenu)
myMenu.add_cascade(label="Edit",menu=editMenu)

fileMenu.add_cascade(label="New Window",command=yeni_pencere_ac)
fileMenu.add_cascade(label="Close Window",command=pen.quit)

pen.mainloop()