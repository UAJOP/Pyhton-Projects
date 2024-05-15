import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="notepad"
)

cursor = db.cursor()

def insert_note_to_database(yazi, dosya_adi):
    cursor.execute("INSERT INTO notlar (icerik, dosya_adi) VALUES (%s, %s)", (yazi, dosya_adi))
    db.commit()

def dosyayi_kayitet():
    dosya_lokasyonu = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Yazı dosyası", "*.txt"), ["Tüm dosyalar", "*.*"]]
    )
    if not dosya_lokasyonu:
        return
    with open(dosya_lokasyonu, "w") as dosya_cikisi:
        yazi = yazi_duzenleme.get(1.0, tk.END)
        dosya_cikisi.write(yazi)

    cursor.execute("INSERT INTO notlar (dosya_adi) VALUES (%s)", (dosya_lokasyonu,))
    db.commit()

    insert_note_to_database(yazi, dosya_lokasyonu)

    root.title(f"NOT DEFTERİ - {dosya_lokasyonu}")

def dosyayi_ac():
    dosya_lokasyonu = askopenfilename(
        filetypes=[("Yazı dosyası", "*.txt"), ["Tüm dosyalar", "*.*"]]
    )
    if not dosya_lokasyonu:
        return

    cursor.execute("SELECT icerik FROM notlar WHERE dosya_adi = %s", (dosya_lokasyonu,))
    veritabani_notlari = cursor.fetchone()

    if veritabani_notlari:
        yazi_duzenleme.delete(1.0, tk.END)
        yazi_duzenleme.insert(tk.END, veritabani_notlari[0], "tag_name")
    else:
        with open(dosya_lokasyonu, "r") as dosya_girisi:
            yazi = dosya_girisi.read()
            yazi_duzenleme.insert(tk.END, yazi)

        cursor.execute("INSERT INTO notlar (dosya_adi, icerik) VALUES (%s, %s)", (dosya_lokasyonu, yazi))
        db.commit()

    root.title(f"NOT DEFTERİ - {dosya_lokasyonu}")

def eski_notlari_goster():
    # Veritabanından tüm notları çekme
    cursor.execute("SELECT dosya_adi FROM notlar")
    eski_notlar = cursor.fetchall()

    # Eski notları gösteren bir pencere oluşturma
    eski_notlar_penceresi = tk.Toplevel(root)
    eski_notlar_penceresi.title("Eski Notlarım")

    # Eski notları gösteren bir metin kutusu ekleme
    eski_notlar_metin = tk.Text(eski_notlar_penceresi, spacing1=9)
    eski_notlar_metin.grid(row=0, column=0, sticky="nsew")

    # Eski notları metin kutusuna ekleyerek gösterme
    for dosya_adi in eski_notlar:
        eski_notlar_metin.insert(tk.END, dosya_adi[0] + "\n")

root = tk.Tk()
root.title("NOT DEFTERİ")
root.rowconfigure(0, minsize=600)
root.columnconfigure(1, minsize=600)

yazi_duzenleme = tk.Text(root, spacing1=9)
yazi_duzenleme.grid(row=0, column=1, sticky="nsew")

cerceve_butonu = tk.Frame(root, relief=tk.RAISED, bd=3)
cerceve_butonu.grid(row=0, column=0, sticky="ns")

buton_acis = tk.Button(cerceve_butonu, text="DOSYAYI AÇ", command=dosyayi_ac)
buton_acis.grid(row=0, column=0, padx=5, pady=5)

buton_kayit = tk.Button(cerceve_butonu, text="DOSYAYI KAYDET", command=dosyayi_kayitet)
buton_kayit.grid(row=1, column=0, padx=5)

buton_eski_notlar = tk.Button(cerceve_butonu, text="ESKİ NOTLARIM", command=eski_notlari_goster)
buton_eski_notlar.grid(row=2, column=0, padx=5)

root.mainloop()