import tkinter as tk
from tkinter import messagebox
import sqlite3
import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\mathe\Documents\Programação\build2\img_Login")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def login_page():
    window.destroy()
    import Registro


def login():
    email = entry_1.get()
    password = entry_2.get()
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE email=? AND password=?', (email, password))
    
    if cursor.fetchone():
        messagebox.showinfo("Sucesso", "Login bem-sucedido!")
        load_user_db(email)
        window.destroy()
        import gui_teste
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")
    
    conn.close()

# Função para carregar o banco de dados do usuário
def load_user_db(username):
    conn = sqlite3.connect(f'{username}.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM data')
    
    # Exibir dados do banco de dados do usuário
    for row in cursor.fetchall():
        print(row)
    
    conn.close()



window = Tk()

window.geometry("1090x700")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 700,
    width = 1090,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    719.0,
    147.0,
    anchor="nw",
    text="Login",
    fill="#000000",
    font=("MontserratRoman SemiBold", 48 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    793.0,
    323.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=623.0,
    y=302.0,
    width=340.0,
    height=40.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    793.0,
    409.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=623.0,
    y=388.0,
    width=340.0,
    height=40.0
)

canvas.create_text(
    618.0,
    277.0,
    anchor="nw",
    text="Endereço de E-mail",
    fill="#000000",
    font=("MontserratRoman Regular", 16 * -1)
)

canvas.create_text(
    618.0,
    363.0,
    anchor="nw",
    text="Senha",
    fill="#000000",
    font=("MontserratRoman Regular", 16 * -1)
)

canvas.create_text(
    618.0,
    442.0,
    anchor="nw",
    text="ou se registre",
    fill="#000000",
    font=("MontserratRoman Regular", 16 * -1)
)

button_aqui = Button(
    fg = "#0066FF",
    bg = "white",
    text="AQUI !",
    activebackground="white",
    activeforeground="#0066FF",
    font=("MontserratRoman Light", 16 * -1,),
    cursor="hand2",
    bd=0,
    command= login_page
)
button_aqui.place(x = 717.0, y = 438.0)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= login,
    relief="flat"
)
button_1.place(
    x=618.0,
    y=507.0,
    width=350.0,
    height=45.680999755859375
)

canvas.create_rectangle(
    0.0,
    0.0,
    469.0,
    700.0,
    fill="#D7E6C5",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    234.0,
    350.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    234.0,
    325.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
