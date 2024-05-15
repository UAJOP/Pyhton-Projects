import tkinter as tk
from tkinter import ttk

def create_rounded_frame(parent, width, height, radius=20, color="lightblue"):
    frame = ttk.Frame(parent)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    canvas = tk.Canvas(frame, width=width, height=height, highlightthickness=0)
    canvas.pack(expand=True, fill=tk.BOTH)

    parent.update_idletasks()  # Güncellenmiş boyutları almak için

    # Yuvarlak kenarları çizmek için
    x, y, w, h = 0, 0, width, height
    canvas.create_polygon(
        (x + radius, y, x + w - radius, y, x + w, y + radius, x + w, y + h - radius,
         x + w - radius, y + h, x + radius, y + h, x, y + h - radius, x, y + radius),
        outline=color, width=2, fill=color
    )

    canvas.create_arc(
        (x, y, x + 2 * radius, y + 2 * radius),
        start=90, extent=90, outline=color, width=2, style=tk.ARC
    )
    canvas.create_arc(
        (x + w - 2 * radius, y, x + w, y + 2 * radius),
        start=0, extent=90, outline=color, width=2, style=tk.ARC
    )
    canvas.create_arc(
        (x + w - 2 * radius, y + h - 2 * radius, x + w, y + h),
        start=270, extent=90, outline=color, width=2, style=tk.ARC
    )
    canvas.create_arc(
        (x, y + h - 2 * radius, x + 2 * radius, y + h),
        start=180, extent=90, outline=color, width=2, style=tk.ARC
    )

    return frame

root = tk.Tk()
root.title("Rounded Frame Example")

# Tema konfigürasyonu
style = ttk.Style()
style.configure("RoundedFrame.TFrame", background="white")

rounded_frame = create_rounded_frame(root, 300, 200)

root.geometry("400x300")
root.mainloop()
