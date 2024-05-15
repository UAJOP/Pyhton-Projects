from tkinter import * 


root = Tk() 

def topla():
    winTopla = Tk()
    winTopla.title("Toplama İşlemi")
    winTopla.geometry("400x400")
    
    def topla():
        toplam = int(number1.get()) + int(number2.get())
        sumLabel = Label(winTopla, text=toplam)
        sumLabel.grid(row=2,column=2)
    
    def close():
        pass
    
    number1 = Entry(winTopla)
    number2= Entry(winTopla)
    numberLabel1 = Label(winTopla,text="Sayı1")
    numberLabel2 = Label(winTopla,text="Sayı2")
    buttonTopla = Button(winTopla,text= "Topla", command=topla)
    cikisButton= Button (winTopla, text="Çıkış", command=close)
    
    numberLabel1.grid(row=0, column=0)
    numberLabel2.grid(row=1, column=0)
    number1.grid(row=0, column=1)
    number2.grid(row=1, column=1)
    buttonTopla.grid(row=2, column=0)
    cikisButton.grid(row=3,column=0)

    
    winTopla.mainloop()

def cikar():
    pass

def böl():
    pass

def çarp():
    pass

def clickMe():
    myLabel.grid_forget()
    
def showMe():
    myLabel.grid(row=1,column=0)
    
root.title("Menu İşlemleri")
root.geometry("400x400")

myMenu = Menu(root)

root.config(menu=myMenu)

myButton = Button(root, text="Click Me", command= clickMe)
myLabel = Label(root, text ="Burak")
myShowButton = Button(root, text= "Show Me", command=showMe)

myLabel.grid(row=1,column=0)
myButton.grid(row=0,column=0)
myShowButton.grid(row=0,column=1)

fileMenu = Menu(myMenu)
editMenu = Menu(myMenu)
searchMenu = Menu(myMenu)

myMenu.add_cascade(label="File", menu=fileMenu)
myMenu.add_cascade(label="Edit", menu=editMenu)
myMenu.add_cascade(label="Search", menu=searchMenu)

fileMenu.add_command(label="Toplama İşlemi Yap", command=topla)
fileMenu.add_command(label="Çıkarma İşlemi Yap", command=cikar)
fileMenu.add_command(label="Bölme İşlemi Yap", command=böl)
fileMenu.add_command(label="Çarpma İşlemi Yap", command=çarp)
root.mainloop()
