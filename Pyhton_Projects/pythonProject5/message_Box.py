from tkinter import *
from tkinter import messagebox

pen=Tk()

pen.title("popup_MessageBox")
pen.geometry("600x600")
myLabel = Label(pen,text="")

def popup1():
    messagebox.showinfo("Bilgi"," Bu program IEU tarafından yapıldı.")

def popup2():
    messagebox.showwarning("Uyarı","Bu bir uyarıdır.")

def popup3():
    messagebox.showerror("Uyarı","Bu bir hatadır")


def popup4():
    cevap=messagebox.askyesno("Soru","Devam etmek istermisiniz")
    myLabel["text"] = cevap
    if cevap==1:
        win = Toplevel()
        win.title("")
        win.config(bg="pink")
        win.mainloop()
    elif cevap==0:
        wan = Toplevel()
        wan.title("")
        wan.config(bg="purple")
        wan.mainloop()

def popup5():
    cevap=messagebox.askokcancel("soru","evet, iptal")
    myLabel["text"]=cevap
def popup6():
    cevap=messagebox.askquestion("soru","sor")
    myLabel["text"]=cevap



popup1 = Button(pen,text="Show İnfo",command=popup1,bg="pink")
popup2 = Button(pen,text="Show Warning",command=popup2,bg="purple")
popup3= Button(pen,text="Show Error",command=popup3,bg="blue")
popup4= Button(pen,text="YesNO",command=popup4,bg="green")
popup5= Button(pen,text="AskYesCancel",command=popup5,bg="red")
popup6= Button(pen,text="AskQuestion",command=popup6,bg="yellow")

popup1.grid(row=0,column=0,sticky=W)
popup2.grid(row=0,column=1,sticky=W)
popup3.grid(row=0,column=2,sticky=W)
popup4.grid(row=0,column=3,sticky=W)
popup5.grid(row=0,column=4,sticky=W)
popup6.grid(row=0,column=5,sticky=W)
myLabel.grid(row=0,column=6,sticky=W)




pen.mainloop()