import tkinter as tk
from tkinter import ttk

def on_select(event):
    selected_item = tree.selection()
    item_text = tree.item(selected_item, "text")
    print(f"Selected item: {item_text}")

def add_node():
    item_text = entry.get()
    tree.insert("", "end", text=item_text)

# Tkinter penceresini oluştur
root = tk.Tk()
root.title("TreeView Örneği")

# TreeView oluştur
tree = ttk.Treeview(root)
tree["columns"] = ("1", "2")

# Sütunları konfigüre et
tree.column("#0", width=150, minwidth=150)
tree.column("1", anchor=tk.W, width=150)
tree.column("2", anchor=tk.W, width=150)

# Başlıkları belirle
tree.heading("#0", text="Başlık 1", anchor=tk.W)
tree.heading("1", text="Başlık 2", anchor=tk.W)
tree.heading("2", text="Başlık 3", anchor=tk.W)

# Ağaç öğelerini ekle
tree.insert("", "end", text="Kök", values=("Değer 1", "Değer 2"))
tree.insert("", "end", text="Kök 2", values=("Değer 3", "Değer 4"))
tree.insert("", "end", text="Kök 3", values=("Değer 5", "Değer 6"))

# TreeView'ın olaylarını bağla
tree.bind("<ButtonRelease-1>", on_select)

# Entry ve ekle butonunu ekleyerek yeni öğeler eklemek için bir arayüz oluştur
entry = tk.Entry(root)
add_button = tk.Button(root, text="Ekle", command=add_node)

# Widget'ları yerleştir
entry.pack(pady=10)
add_button.pack(pady=10)
tree.pack(expand=True, fill=tk.BOTH)

# Pencereyi göster
root.mainloop()
