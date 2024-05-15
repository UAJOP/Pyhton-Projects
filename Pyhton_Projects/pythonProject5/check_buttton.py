from tkinter import *
pen =Tk()
pen.geometry("500x500")
pen.title("CHECK KULLANIMI")
lasbel=Label(pen,text="")

v1 = StringVar()
check1= Checkbutton(pen,text="KVKK Kabul Ediyorum",variable=v1,onvalue="onKVKK",offvalue="offKVKK")
v2=StringVar()
check2= Checkbutton(pen,text="Sözleşmeyi Kabul Ediyorum",variable=v2,onvalue="onSozlesme",offvalue="offSozlesme")

def kontrol():
    if v1.get()=="k":
        lasbel["text"]="Kadın Seçtiniz"
    elif v2.get()=="e":
        lasbel["text"]="Erkek Seçtiniz"


btn=Button(pen,text="Kontrol",command=kontrol)

check1.deselect()
check2.deselect()

check1.grid(row=0,column=0,sticky=W,padx=10,pady=10)
check2.grid(row=1,column=0,sticky=W,padx=10,pady=10)
lasbel.grid(row=2,column=0,stcky=W,padx=10,pady=10)
btn.grid(row=3,column=0,stcky=W,padx=10,pady=10)

pen.mainloop()