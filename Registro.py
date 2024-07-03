from pathlib import Path
import tkinter as tk
from tkinter import messagebox
import sqlite3
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\mathe\Documents\Programação\build2\img_Resgistro")

# Função para criar o banco de dados de um novo usuário
def create_user_db(email):
    conn = sqlite3.connect(f'{email}.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS data (
                      id INT AUTO_INCREMENT PRIMARY KEY,
                      data DATE NOT NULL,
                      valor DECIMAL(10, 2) NOT NULL,
                      categoria VARCHAR(255) NOT NULL)''')
                      
    conn.commit()
    conn.close()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_login_window():
    import Login

def signup_page():
    register_result = register()
    if register_result:  # Se o registro for bem-sucedido
        window.destroy()
        open_login_window()

# Função para registrar um novo usuário
def register():
    email = entry_1.get()
    password = entry_2.get()
    confirm_password = entry_3.get()

    if email and password and confirm_password:
        if password == confirm_password:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS users (email TEXT, password TEXT)')
            
            cursor.execute('SELECT * FROM users WHERE email=?', (email,))
            if cursor.fetchone():
                messagebox.showerror("Erro", "Usuário já existe!")
                conn.close()
                return False
            else:
                cursor.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, password))
                conn.commit()
                create_user_db(email)
                messagebox.showinfo("Sucesso", "Usuário registrado com sucesso!")
                conn.close()
                return True
        else:
            messagebox.showerror("Erro", "As senhas não coincidem!")
            return False
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return False

window = Tk()
window.geometry("1090x700")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=700,
    width=1090,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    1090.0,
    700.0,
    fill="#D7E6C5",
    outline=""
)

canvas.create_rectangle(
    253.0,
    59.0,
    838.0,
    642.0,
    fill="#FEFFFE",
    outline=""
)

canvas.create_text(
    451.0,
    115.0,
    anchor="nw",
    text="Registro",
    fill="#000000",
    font=("MontserratRoman SemiBold", 48 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    557.0,
    303.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=387.0,
    y=282.0,
    width=340.0,
    height=40.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    557.0,
    389.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    show='*'  # Para ocultar os caracteres digitados (senha)
)
entry_2.place(
    x=387.0,
    y=368.0,
    width=340.0,
    height=40.0
)

canvas.create_text(
    382.0,
    257.0,
    anchor="nw",
    text="Endereço de E-mail",
    fill="#000000",
    font=("MontserratRoman Regular", 16 * -1)
)

canvas.create_text(
    382.0,
    343.0,
    anchor="nw",
    text="Senha",
    fill="#000000",
    font=("MontserratRoman Regular", 16 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    557.0,
    475.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    show='*'  # Para ocultar os caracteres digitados (senha)
)
entry_3.place(
    x=387.0,
    y=454.0,
    width=340.0,
    height=40.0
)

canvas.create_text(
    382.0,
    429.0,
    anchor="nw",
    text="Confirme a senha",
    fill="#000000",
    font=("MontserratRoman Regular", 16 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=signup_page
)
button_1.place(
    x=382.0,
    y=539.0,
    width=350.0,
    height=45.680999755859375
)
window.resizable(False, False)
window.mainloop()
