import tkinter as tk
from PIL import Image, ImageTk

def on_button_click():
    # Butona tıklandığında yapılacak işlemler
    print("Butona tıklandı!")

def open_new_window():
    # Yeni pencereyi açma işlemi
    new_window = tk.Toplevel(root)
    new_window.title("Yeni Pencere")
    new_window.geometry("300x200")
    label = tk.Label(new_window, text="Yeni pencereye hoş geldiniz!")
    label.pack()

# Ana pencere oluşturma
root = tk.Tk()
root.title("Resimli Buton Örneği")

# Resmi yükleme ve buton oluşturma
image = Image.open("path/to/your/image.jpg")  # Resminizin yolunu belirtin
photo = ImageTk.PhotoImage(image)
button = tk.Button(root, image=photo, command=on_button_click)
button.pack(pady=10)

# İkinci bir buton oluşturma (yeni pencereyi açmak için)
open_window_button = tk.Button(root, text="Yeni Pencere Aç", command=open_new_window)
open_window_button.pack(pady=10)

# Ana döngüyü başlatma
root.mainloop()
