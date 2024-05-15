def doktorGirisForm():
    def clear_entries():
        username_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
    won = Toplevel()
    pen.withdraw()
    won.resizable(width=False, height=False)
    won.config(bg="RoyalBlue1")
    won.title("Doktor Giriş")
    won.geometry("300x200")
    icon_path3 = "images/doctor_icon_140508.ico"
    won.iconbitmap(icon_path3)
    won.protocol("WM_DELETE_WINDOW", lambda: on_closing_trh(won))
    Label(won, text="Kullanıcı Adı:", font=myFont, bg="RoyalBlue1", fg="Snow").grid(row=0, column=0, pady=10)
    username_entry = Entry(won, width=25, borderwidth=10, bg="RoyalBlue1", fg="white")
    username_entry.grid(row=0, column=1, pady=5)
    Label(won, text="Şifre:", font=myFont, bg="RoyalBlue1", fg="Snow").grid(row=1, column=0, pady=10)
    password_entry = Entry(won, show="*", width=25, borderwidth=10, bg="RoyalBlue1", fg="white")
    password_entry.grid(row=1, column=1, pady=5)
    login_button = Button(won, bg="Snow", fg="Gray21", text="Giriş Yap",command=lambda: login_clicked(username_entry, password_entry, won))
    login_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10)
    clear_button = Button(won, bg="Snow", fg="Gray21", text="Temizle", command=clear_entries)
    clear_button.grid(row=2, column=1, sticky=E, pady=10, padx=10)
    won.mainloop()

def on_closing_trh(won):
    won.destroy()
    pen.destroy()
