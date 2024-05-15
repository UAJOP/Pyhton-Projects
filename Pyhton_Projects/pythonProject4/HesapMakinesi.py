import tkinter as tk

class HesapMakinesi:
    def __init__(self, root):
        self.root = root
        self.root.title("Hesap Makinesi")

        # Ekran
        self.ekran = tk.Entry(root, width=16, font=('Arial', 20), borderwidth=2, relief="solid")
        self.ekran.grid(row=0, column=0, columnspan=4, pady=10)

        # Butonlar
        butonlar = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '%', '+/-'
        ]

        row_val = 1
        col_val = 0

        for buton in butonlar:
            tk.Button(root, text=buton, width=4, height=2, command=lambda b=buton: self.buton_tiklandi(b), bg="#E0E0E0").grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def buton_tiklandi(self, deger):
        if deger == '=':
            try:
                hesap = eval(self.ekran.get())
                self.ekran.delete(0, tk.END)
                self.ekran.insert(tk.END, str(hesap))
            except Exception as e:
                self.ekran.delete(0, tk.END)
                self.ekran.insert(tk.END, "Hata")
        elif deger == 'C':
            self.ekran.delete(0, tk.END)
        elif deger == '%':
            try:
                deger = float(self.ekran.get())
                sonuc = deger / 100
                self.ekran.delete(0, tk.END)
                self.ekran.insert(tk.END, str(sonuc))
            except Exception as e:
                self.ekran.delete(0, tk.END)
                self.ekran.insert(tk.END, "Hata")
        elif deger == '+/-':
            try:
                deger = float(self.ekran.get())
                sonuc = -deger
                self.ekran.delete(0, tk.END)
                self.ekran.insert(tk.END, str(sonuc))
            except Exception as e:
                self.ekran.delete(0, tk.END)
                self.ekran.insert(tk.END, "Hata")
        else:
            self.ekran.insert(tk.END, deger)

if __name__ == "__main__":
    root = tk.Tk()
    hesap_makinesi = HesapMakinesi(root)
    root.mainloop()
