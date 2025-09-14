import tkinter as tk
from tkinter import font as tkfont
import winsound
import time
from tkinter import filedialog
print("V1.9")
def l():
    winsound.Beep(500, 500)
def f():
    winsound.Beep(1000, 250)
def s():
    winsound.Beep(500, 250)
def n():
    time.sleep(1)
def li():
    root = tk.Tk()
    root.title("Caricamento file...")
    nome_file = filedialog.askopenfilename()
    root.title("Riproduzione finita")
    aa = tk.Label(root, text="Riproduzione finita", font=("Sans-Serif", 50))
    aa.pack()
    with open(nome_file, "r") as file:
        while True:
            carattere = file.read(1)
            if not carattere: # Se read(1) restituisce una stringa vuota, significa che siamo alla fine del file
                winsound.Beep(1000, 5000)
                break
            if carattere == "s":
                s()
            if carattere == "n":
                n()
            if carattere == "l":
                l()
            if carattere == "f":
                f()
    root.mainloop()
def c():
    value = ""
    
    bl = tk.Tk()
    bl.title("Creazione file - SREditor")

    def salva():
        nome_file = a.get()
        with open(nome_file, "w") as file:
            file.write(value)
            bl.destroy()
    def oh(valore):
        nonlocal value
        value = value + valore
        print(f"La melodia attuale è: {value}")

    a = tk.Entry(bl, width=12)
    a.insert('end', ".sre")
    b = tk.Button(
        bl,
        text="n",
        font=("Helvetica", 14),
        bg="#1598F5",
        fg="#9A8828",
        command=lambda: oh("n")
    )
    c_button = tk.Button(
        bl,
        text="s",
        font=("Helvetica", 14),
        bg="#1598F5",
        fg="#9A8828",
        command=lambda: oh("s")
    )
    d = tk.Button(
        bl,
        text="l",
        font=("Helvetica", 14),
        bg="#1598F5",
        fg="#9A8828",
        command=lambda: oh("l")
    )
    e = tk.Button(
        bl,
        text="f",
        font=("Helvetica", 14),
        bg="#1598F5",
        fg="#9A8828",
        command=lambda: oh("f")
    )
    f_button = tk.Button(
        bl,
        text="Salva",
        font=("Helvetica", 14),
        bg="#1598F5",
        fg="#9A8828",
        command=salva
    )

    a.pack()
    b.pack(pady=5)
    c_button.pack()
    d.pack()
    e.pack()
    f_button.pack()

    bl.mainloop()
scena = tk.Tk()
scena.title("SREditor")
a = tk.Label(scena, text="SREditor", font=("Sans-Serif", 50))
b = tk.Button(
    scena,
    text="Apri e riproduci file",
    font=("Helvetica", 14),
    bg="#03fca1",
    fg="#fc035e",
    command=li
    )
c = tk.Button(
    scena,
    text="Crea nuova melodia",
    font=("Helvetica", 14),
    bg="#1598F5",
    fg="#9A8828",
    command=c
    )
def aiuto():
    aiuto = tk.Tk()
    aiuto.title("Aiuto")
    with open("aiuto.txt", "r") as file:
        aiuti = file.read()
    j = tk.Label(aiuto, text=aiuti, font=("Sans-Serif", 15))
    j.pack()
    aiuto.mainloop()
d = tk.Button(
    scena,
    text="Aiuto",
    font=("Helvetica", 14),
    bg="#EAEAEA",
    fg="#FF6B6B",
    command=aiuto
    )
v = tk.Label(scena, text="V1.9", font=("Sans-Serif", 5))
a.pack()
b.pack(pady=5)
c.pack(pady=5)
d.pack(pady=5)
v.pack()
scena.mainloop()