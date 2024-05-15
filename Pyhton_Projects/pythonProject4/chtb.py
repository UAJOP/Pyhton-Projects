import tkinter as tk
from tkinter import ttk

def on_button_click():
    print("Button clicked!")

# Ana pencere
root = tk.Tk()
root.title("Tkinter Widget Örnekleri")

# Label widget
label = tk.Label(root, text="Label Widget")
label.pack(pady=5)

# Entry widget
entry = tk.Entry(root)
entry.insert(0, "Entry Widget")
entry.pack(pady=5)

# Button widget
button = tk.Button(root, text="Button Widget", command=on_button_click)
button.pack(pady=5)

# Checkbutton widget
check_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(root, text="Checkbutton Widget", variable=check_var)
checkbutton.pack(pady=5)

# Radiobutton widget
radio_var = tk.StringVar()
radio_button1 = tk.Radiobutton(root, text="Radiobutton 1", variable=radio_var, value="Option 1")
radio_button2 = tk.Radiobutton(root, text="Radiobutton 2", variable=radio_var, value="Option 2")
radio_button1.pack()
radio_button2.pack(pady=5)

# Listbox widget
listbox = tk.Listbox(root)
for item in ["Listbox Item 1", "Listbox Item 2", "Listbox Item 3"]:
    listbox.insert(tk.END, item)
listbox.pack(pady=5)

# Combobox widget
combo_var = tk.StringVar()
combobox = ttk.Combobox(root, textvariable=combo_var)
combobox['values'] = ("Combobox Item 1", "Combobox Item 2", "Combobox Item 3")
combobox.pack(pady=5)

# Text widget
text_widget = tk.Text(root, height=5, width=30)

text_widget.pack(pady=5)

# Canvas widget
canvas = tk.Canvas(root, width=200, height=100, bg='lightgray')
canvas.pack(pady=5)

# Scrollbar widget
scrollbar = tk.Scrollbar(root, command=text_widget.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_widget.config(yscrollcommand=scrollbar.set)

# Frame widget
frame = tk.Frame(root, bd=2, relief=tk.GROOVE)
frame.pack(pady=5)

# Scale widget
scale = tk.Scale(frame, from_=0, to=100, orient=tk.HORIZONTAL)
scale.pack()

# Progressbar widget
progressbar = ttk.Progressbar(root, length=200, mode='indeterminate')
progressbar.start()
progressbar.pack(pady=5)

# Spinbox widget
spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.pack(pady=5)

# Menubutton widget
menubutton = tk.Menubutton(root, text="Menubutton")
menubutton.pack(pady=5)

# Menu widget
menu = tk.Menu(menubutton, tearoff=0)
menu.add_command(label="Menu Item 1")
menu.add_command(label="Menu Item 2")
menu.add_separator()
menu.add_command(label="Menu Item 3")
menubutton["menu"] = menu

# Message widget
message = tk.Message(root, text="Message Widget", width=200)
message.pack(pady=5)

# PhotoImage widget
photo = tk.PhotoImage(width=50, height=50)
canvas.create_image(10, 10, anchor=tk.NW, image=photo)

import tkinter as tk
from tkinter import ttk

def on_listbox_select(event):
    selected_item = listbox.get(listbox.curselection())
    print("Selected item:", selected_item)

# Ana pencere
root = tk.Tk()
root.title("Daha Fazla Tkinter Widget Örnekleri")

# Messagebox widget
def show_info():
    tk.messagebox.showinfo("Bilgi", "Bu bir messagebox örneğidir.")

info_button = tk.Button(root, text="Bilgi Mesajı Göster", command=show_info)
info_button.pack(pady=5)

# Entry widget (Password)
password_entry = tk.Entry(root, show="*")
password_entry.insert(0, "password")
password_entry.pack(pady=5)

# Spinbox widget (with range)
spinbox_with_range = tk.Spinbox(root, from_=0, to=10)
spinbox_with_range.pack(pady=5)

# Treeview widget
treeview = ttk.Treeview(root, columns=("Name", "Age"))
treeview.heading("Name", text="Ad")
treeview.heading("Age", text="Yaş")

treeview.insert("", tk.END, values=("John", 30))
treeview.insert("", tk.END, values=("Alice", 25))
treeview.pack(pady=5)

# Listbox widget with scrollbar
listbox_frame = tk.Frame(root)
listbox_scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL)
listbox = tk.Listbox(listbox_frame, yscrollcommand=listbox_scrollbar.set)
listbox_scrollbar.config(command=listbox.yview)
listbox.pack(side=tk.LEFT)
listbox_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

for item in range(1, 21):
    listbox.insert(tk.END, f"Item {item}")

listbox_frame.pack(pady=5)

listbox.bind("<<ListboxSelect>>", on_listbox_select)

# OptionMenu widget
option_var = tk.StringVar()
option_var.set("Seçenekler")
option_menu = tk.OptionMenu(root, option_var, "Seçenek 1", "Seçenek 2", "Seçenek 3")
option_menu.pack(pady=5)

# PanedWindow widget
paned_window = tk.PanedWindow(root, orient=tk.HORIZONTAL)
frame1 = tk.Frame(paned_window, relief=tk.SUNKEN, borderwidth=2)
frame2 = tk.Frame(paned_window, relief=tk.SUNKEN, borderwidth=2)
paned_window.add(frame1)
paned_window.add(frame2)

paned_window.pack(pady=5)

# Notebook widget
notebook = ttk.Notebook(root)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

notebook.pack(pady=5)

# Color Chooser
def choose_color():
    color = tk.colorchooser.askcolor(title="Renk Seç")
    print("Seçilen renk:", color)

color_button = tk.Button(root, text="Renk Seç", command=choose_color)
color_button.pack(pady=5)

# File Chooser
def choose_file():
    file_path = tk.filedialog.askopenfilename(title="Dosya Seç")
    print("Seçilen dosya:", file_path)

file_button = tk.Button(root, text="Dosya Seç", command=choose_file)
file_button.pack(pady=5)

# Main loop
root.mainloop()




# Main loop
root.mainloop()
