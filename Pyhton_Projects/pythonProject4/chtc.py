from tkinter import *
import mysql.connector
from PIL import Image, ImageTk
import sys

def db_connect():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hastane"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Hata: {err}")
        return None

def hasta_ekle(ad, soyad, tc, dogum_tarihi, cinsiyet, telefon, email, adres, kullanici_adi, sifre):
    connection = db_connect()
    if connection is not None:
        cursor = connection.cursor()

        try:
            insert_query = "INSERT INTO hastalar (ad, soyad, tc_kimlik, dogum_tarihi, cinsiyet, telefon, email, adres, kullanici_adi, sifre) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (ad, soyad, tc, dogum_tarihi, cinsiyet, telefon, email, adres, kullanici_adi, sifre)

            cursor.execute(insert_query, values)

            connection.commit()
            print("Hasta başarıyla eklendi.")
        except mysql.connector.Error as err:
            print(f"Hasta eklenirken hata oluştu: {err}")
        finally:
            cursor.close()
            connection.close()

def save_hasta():
    ad = ad_entry.get()
    soyad = soyad_entry.get()
    tc = tc_entry.get()
    dogum_tarihi = dogum_tarihi_entry.get()
    cinsiyet = cinsiyet_entry.get()
    telefon = telefon_entry.get()
    email = email_entry.get()
    adres = adres_entry.get()
    kullanici_adi = kullanici_adi_entry.get()
    sifre = sifre_entry.get()

    hasta_ekle(ad, soyad, tc, dogum_tarihi, cinsiyet, telefon, email, adres, kullanici_adi, sifre)

    clear_entries()

def clear_entries():
    ad_entry.delete(0, 'end')
    soyad_entry.delete(0, 'end')
    tc_entry.delete(0, 'end')
    dogum_tarihi_entry.delete(0, 'end')
    cinsiyet_entry.delete(0, 'end')
    telefon_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    adres_entry.delete(0, 'end')
    kullanici_adi_entry.delete(0, 'end')
    sifre_entry.delete(0, 'end')

def merkez_pencere(pencere, genislik, yukseklik):
    ekran_genisligi = pencere.winfo_screenwidth()
    ekran_yuksekligi = pencere.winfo_screenheight()

    x = (ekran_genisligi - genislik) // 2
    y = (ekran_yuksekligi - yukseklik) // 2

    pencere.geometry(f"{genislik}x{yukseklik}+{x}+{y}")

def programdan_cik():
    pen.destroy()
    sys.exit()

def check_login(username, password):
    # Gerçek bir kimlik doğrulama mekanizması buraya eklenebilir.
    return True

def login_clicked(username_entry, password_entry, window):
    username = username_entry.get()
    password = password_entry.get()

    if check_login(username, password):
        print("Login successful!")
        window.destroy()
    else:
        print("Login failed. Please try again.")

def hastaKayitForm():
    def on_closing_one(wen):
        wen.destroy()
        pen.destroy()

    def clear_entries():
        ad_entry.delete(0, 'end')
        soyad_entry.delete(0, 'end')
        tc_entry.delete(0, 'end')
        dogum_tarihi_entry.delete(0, 'end')
        cinsiyet_entry.delete(0, 'end')
        telefon_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        adres_entry.delete(0, 'end')
        kullanici_adi_entry.delete(0, 'end')
        sifre_entry.delete(0, 'end')

    wen = Toplevel()
    pen.withdraw()
    wen.config(bg="DeepSkyBlue2")
    wen.resizable(width=False, height=False)
    wen.title("Hasta Kayıt")
    wen.geometry("600x400")
    icon_path1 = "images/iconico32.ico"
    wen.iconbitmap(icon_path1)
    wen.protocol("WM_DELETE_WINDOW", lambda: on_closing_one(wen))

    Label(wen, text="Ad:", font=myFont, bg="DeepSkyBlue2", fg="Snow").grid(row=0, column=0, pady=10)
    ad_entry = Entry(wen, width=25, borderwidth=10, bg="DeepSkyBlue3", fg="white")
    ad_entry.grid(row=0, column=1, pady=10)

    Label(wen, text="Soyad:", font=myFont, bg="DeepSkyBlue2", fg="Snow").grid(row=0, column=2, pady=10)
    soyad_entry = Entry(wen, width=25, borderwidth=10, bg="DeepSkyBlue3", fg="white")
    soyad_entry.grid(row=0, column=3, pady=10)

    Label(wen, text="TC Kimlik:", font=myFont, bg="DeepSkyBlue2", fg="Snow").grid(row=1, column=0, pady=10)
    tc_entry = Entry(wen, width=25, borderwidth=10, bg="DeepSkyBlue3", fg="white")
    tc_entry.grid(row=1, column=1, pady=10)

    Label(wen, text="Doğum Tarihi:", font=myFont, bg="DeepSkyBlue2", fg="Snow").grid(row=1, column=2, pady=10)
    dogum_tarihi_entry = Entry(wen, width=25, borderwidth=10, bg="DeepSkyBlue3", fg="white")
    dogum_tarihi_entry.grid(row=1, column=3, pady=10)

    Label(wen, text="Cinsiyet:", font=myFont, bg="DeepSkyBlue2", fg="Snow").grid(row=2, column=0, pady=10)
    cinsiyet_entry = Entry(wen, width=25, borderwidth=10, bg="DeepSkyBlue3", fg="white")
    cinsiyet_entry.grid(row=2, column=1, pady=10)

    Label(wen, text="Telefon:", font=myFont, bg="DeepSkyBlue2", fg="Snow").grid(row=2, column=2, pady=10)
    telefon_entry = Entry(wen, width=25, borderwidth=10, bg="    DeepSkyBlue3", fg="white")
    telefon_entry.grid(row=2, column=3, pady=10)

    Label(wen, text="Email:", font=myFont, bg="DeepSkyBlue2", fg="Snow").grid(row=3, column=0, pady=10)
    email_entry = Entry(wen, width=25, borderwidth=10, bg="DeepSkyBlue3", fg="white")
    email_entry.grid(row=3, column=1, pady=10)

    Label(wen, text="Adres:", font=myFont, bg="DeepSkyBlue2", fg="Snow").grid(row=3, column=2, pady=10)
    adres_entry = Entry(wen, width=25, borderwidth=10, bg="DeepSkyBlue3", fg="white")
    adres_entry.grid(row=3, column=3, pady=10)

    Label(wen, text="Kullanıcı Adı:", font=myFont, bg="DeepSkyBlue2", fg="Snow").grid(row=4, column=0, pady=10)
    kullanici_adi_entry = Entry(wen, width=25, borderwidth=10, bg="DeepSkyBlue3", fg="white")
    kullanici_adi_entry.grid(row=4, column=1, pady=10)

    Label(wen, text="Şifre:", font=myFont, bg="DeepSkyBlue2", fg="Snow").grid(row=4, column=2, pady=10)
    sifre_entry = Entry(wen, width=25, borderwidth=10, bg="DeepSkyBlue3", fg="white", show="*")
    sifre_entry.grid(row=4, column=3, pady=10)

    save_button = Button(wen, text="Kaydet", font=myFont, width=20, bg="yellow green", command=save_hasta)
    save_button.grid(row=5, column=1, columnspan=2, pady=20)

    clear_button = Button(wen, text="Temizle", font=myFont, width=20, bg="tomato", command=clear_entries)
    clear_button.grid(row=5, column=2, columnspan=2, pady=20)

    wen.mainloop()

def girisYapForm():
    def on_closing_two(wen):
        wen.destroy()
        pen.destroy()

    wen = Toplevel()
    pen.withdraw()
    wen.config(bg="DeepSkyBlue2")
    wen.resizable(width=False, height=False)
    wen.title("Giriş Yap")
    wen.geometry("600x300")
    icon_path2 = "images/iconico32.ico"
    wen.iconbitmap(icon_path2)
    wen.protocol("WM_DELETE_WINDOW", lambda: on_closing_two(wen))

    Label(wen, text="Kullanıcı Adı:", font=myFont, bg="DeepSkyBlue2", fg="Snow").grid(row=0, column=0, pady=10)
    username_entry = Entry(wen, width=25, borderwidth=10, bg="DeepSkyBlue3", fg="white")
    username_entry.grid(row=0, column=1, pady=10)

    Label(wen, text="Şifre:", font=myFont, bg="DeepSkyBlue2", fg="Snow").grid(row=1, column=0, pady=10)
    password_entry = Entry(wen, width=25, borderwidth=10, bg="DeepSkyBlue3", fg="white", show="*")
    password_entry.grid(row=1, column=1, pady=10)

    login_button = Button(wen, text="Giriş Yap", font=myFont, width=20, bg="yellow green", command=lambda: login_clicked(username_entry, password_entry, wen))
    login_button.grid(row=2, column=0, columnspan=2, pady=20)

    wen.mainloop()

pen = Tk()
pen.config(bg="DeepSkyBlue2")
pen.title("Hastane Otomasyonu")
pen.geometry("600x400")
myFont = ("Helvetica", 10)

icon_path = "images/iconico32.ico"
pen.iconbitmap(icon_path)

merkez_pencere(pen, 600, 400)

hasta_kayit_button = Button(pen, text="Hasta Kayıt", font=myFont, width=20, bg="yellow green", command=hastaKayitForm)
hasta_kayit_button.grid(row=0, column=0, pady=20)

giris_yap_button = Button(pen, text="Giriş Yap", font=myFont, width=20, bg="yellow green", command=girisYapForm)
giris_yap_button.grid(row=1, column=0, pady=20)

cikis_button = Button(pen, text="Çıkış", font=myFont, width=20, bg="tomato", command=programdan_cik)
cikis_button.grid(row=2, column=0, pady=20)

pen.mainloop()

