from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
import customtkinter as ctk
from tkinter import ttk

# Funções do teste.py adaptadas para o gui.py
def add_transaction(date, amount, account):
    transactions.insert("", "end", values=(date, amount, account))

def on_button_click(button_id):
    global pressed_button
    # Resetar a imagem do botão previamente pressionado
    if pressed_button is not None:
        if pressed_button == 6:
            button_6.config(image=button_image_6)
        elif pressed_button == 7:
            button_7.config(image=button_image_7)
        elif pressed_button == 8:
            button_8.config(image=button_image_8)
        elif pressed_button == 9:
            button_9.config(image=button_image_9)

    # Atualizar a imagem do botão atualmente pressionado
    if button_id == 6:
        button_6.config(image=button_image_6_click)
        pressed_button = 6
    elif button_id == 7:
        button_7.config(image=button_image_7_click)
        pressed_button = 7
    elif button_id == 8:
        button_8.config(image=button_image_8_click)
        pressed_button = 8
    elif button_id == 9:
        button_9.config(image=button_image_9_click)
        pressed_button = 9


def delete_selected_transactions():
    for item in transactions.selection():
        transactions.delete(item)

def add_transaction_from_input():
    date = entry_date.get()
    amount = entry_amount.get()
    account = entry_account.get()
    if not date or not amount or not account:
        return
    add_transaction(date, amount, account)
    entry_date.delete(0, 'end')
    entry_amount.delete(0, 'end')
    entry_account.delete(0, 'end')

def format_date(event):
    content = entry_date.get().replace("/", "")
    formatted = ""
    for i, char in enumerate(content):
        if i in (2, 4):
            formatted += "/"
        formatted += char
    entry_date.delete(0, 'end')
    entry_date.insert(0, formatted[:10])

def format_amount(event):
    content = entry_amount.get()
    if not content.startswith("R$"):
        entry_amount.delete(0, 'end')
        entry_amount.insert(0, "R$" + content)

# Função para exibir o frame de despesas
def show_despesas_frame():
    clear_frame(main_frame)
    create_despesas_frame(main_frame)

def create_home_frame(frame):
    
    frame.config(bg="#FAFDF7")  # Define o fundo do frame

    canvas.create_rectangle(
        0.0, 68.0, 315.0, 700.0, fill="#FAFDF7", outline=""
    )
    canvas.create_rectangle(
        348.0, 154.0, 727.0, 382.0, fill="#FAFDF7", outline=""
    )
    canvas.create_rectangle(
        348.0, 399.0, 801.0, 678.0, fill="#FAFDF7", outline=""
    )
    canvas.create_rectangle(
        741.0, 154.0, 1071.0, 382.0, fill="#FAFDF7", outline=""
    )
    canvas.create_rectangle(
        816.0, 399.0, 1071.0, 678.0, fill="#FAFDF7", outline=""
    )

    canvas.create_text(
        348.0, 87.0, anchor="nw", text="Bem Vindo!", fill="#000000",
        font=("Montserrat", 26, "bold")
    )
    canvas.create_text(
        375.0, 175.0, anchor="nw", text="Minha Receita", fill="#000000",
        font=("Montserrat", 14, "bold")
    )
    canvas.create_text(
        375.0, 420.0, anchor="nw", text="Distribuição das Despesas", fill="#000000",
        font=("MontserratRoman Bold", 14, "bold")
    )
    canvas.create_text(
        771.0, 172.0, anchor="nw", text="Despesas Recentes", fill="#000000",
        font=("Montserrat", 14, "bold")
    )
    canvas.create_text(
        848.0, 423.0, anchor="nw", text="Top Despesas", fill="#000000",
        font=("Montserrat", 14, "bold")
    )
    canvas.create_text(
        375.0, 229.0, anchor="nw", text="Valor em Banco", fill="#000000",
        font=("Montserrat", 11, "bold")
    )
    canvas.create_text(
        601.0, 229.0, anchor="nw", text="R$ 4.531,00", fill="#000000",
        font=("Montserrat", 14, "bold")
    )
    canvas.create_text(
        601.0, 323.0, anchor="nw", text="R$ 2.210,00", fill="#000000",
        font=("Montserrat", 14, "bold")
    )
    canvas.create_text(
        601.0, 275.0, anchor="nw", text="R$ 2.321,00", fill="#000000",
        font=("Montserrat", 14, "bold")
    )
    canvas.create_text(
        375.0, 323.0, anchor="nw", text="Total Caixa", fill="#000000",
        font=("Montserrat", 11, "bold")
    )
    canvas.create_text(
        375.0, 275.0, anchor="nw", text="Despesas", fill="#000000",
        font=("Montserrat", 11, "bold")
    )
    canvas.create_text(
        11.0, 678.0, anchor="nw", text="All rights reserved © - P.O.B.R.E ", fill="#000000",
        font=("Montserrat", 12, "bold")
    )
def show_home_frame():
    clear_frame(main_frame)
    create_home_frame(main_frame)

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Função para criar o frame de despesas
def create_despesas_frame(frame):
    frame_right = ctk.CTkFrame(frame)
    frame_right.pack(fill="both", expand=True)

    header_frame = ctk.CTkFrame(frame_right)
    header_frame.pack(fill="x", pady=10)

    label_header = ctk.CTkLabel(header_frame, text="Despesas", font=ctk.CTkFont(size=20, weight="bold"))
    label_header.pack(side="left", padx=20)

    button_delete = ctk.CTkButton(header_frame, text="Delete", command=delete_selected_transactions)
    button_delete.pack(side="right", padx=10)

    entry_frame = ctk.CTkFrame(frame_right)
    entry_frame.pack(fill="x", pady=10)

    label_date = ctk.CTkLabel(entry_frame, text="Date")
    label_date.pack(side="left", padx=5)

    global entry_date
    entry_date = ctk.CTkEntry(entry_frame, validate="key")
    entry_date.pack(side="left", padx=5)
    entry_date.bind("<KeyRelease>", format_date)

    label_amount = ctk.CTkLabel(entry_frame, text="Amount")
    label_amount.pack(side="left", padx=5)
    global entry_amount
    entry_amount = ctk.CTkEntry(entry_frame)
    entry_amount.pack(side="left", padx=5)
    entry_amount.bind("<FocusOut>", format_amount)

    label_account = ctk.CTkLabel(entry_frame, text="Account")
    label_account.pack(side="left", padx=5)
    global entry_account
    entry_account = ctk.CTkEntry(entry_frame)
    entry_account.pack(side="left", padx=5)

    button_add = ctk.CTkButton(entry_frame, text="Add Transaction", command=add_transaction_from_input)
    button_add.pack(side="left", padx=10)

    columns = ("Date", "Amount", "Account")
    global transactions
    transactions = ttk.Treeview(frame_right, columns=columns, show="headings", height=20)
    for col in columns:
        transactions.heading(col, text=col)
        transactions.column(col, minwidth=0, width=200, stretch=True)
    transactions.pack(fill="both", padx=20, pady=20, expand=True)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", background="#E5EFDB", foreground="black", rowheight=25, fieldbackground="#E5EFDB")
    style.map('Treeview', background=[('selected', '#4CAF50')])

    sample_transactions = [
        {"date": "14/11/23", "amount": "R$2.011", "account": "Cash"},
        {"date": "14/11/23", "amount": "R$198", "account": "Vault"},
        {"date": "15/11/23", "amount": "R$690", "account": "Bank Account"},
        {"date": "15/11/23", "amount": "R$1.380", "account": "Bank Account"},
        {"date": "15/11/23", "amount": "R$8.900", "account": "Vault"},
        {"date": "16/11/23", "amount": "R$5.931", "account": "Cash"},
        {"date": "16/11/23", "amount": "R$340", "account": "Vault"},
        {"date": "17/11/23", "amount": "R$1.200", "account": "Bank Account"},
        {"date": "17/11/23", "amount": "R$8.305", "account": "Bank Account"},
        {"date": "17/11/23", "amount": "R$450", "account": "Cash"},
        {"date": "18/11/23", "amount": "R$250", "account": "Bank Account"},
        {"date": "18/11/23", "amount": "R$1.380", "account": "Bank Account"},
        {"date": "18/11/23", "amount": "R$460", "account": "Cash"},
    ]
    for transaction in sample_transactions:
        add_transaction(transaction["date"], transaction["amount"], transaction["account"])

# Código principal de gui.py
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\mathe\Documents\Programação\build2\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1090x700")
window.configure(bg = "#FFFFFF")
window.resizable(width=False, height=False)

button_image_6_click = PhotoImage(
    file=relative_to_assets("button_6_click.png"))

button_image_7_click = PhotoImage(
    file=relative_to_assets("button_7_click.png"))

button_image_8_click = PhotoImage(
    file=relative_to_assets("button_8_click.png"))

button_image_9_click = PhotoImage(
    file=relative_to_assets("button_9_click.png"))

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
canvas.create_rectangle(
    0.0,
    0.0,
    1090.0,
    68.0,
    fill="#D7E7C4",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    128.0,
    33.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    activebackground="#D7E7C4",
    bd=0,
    bg="#D7E7C4"
    
)
button_1.place(
    x=968.0,
    y=15.0,
    width=40.0,
    height=40.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
    activebackground="#D7E7C4",
    bd=0,
    bg="#D7E7C4"
    
    
)
button_2.place(
    x=914.0,
    y=15.0,
    width=40.0,
    height=40.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat",
    activebackground="#D7E7C4",
    bd=0,
    bg="#D7E7C4"
)
button_3.place(
    x=860.0,
    y=15.0,
    width=40.0,
    height=40.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat",
    activebackground="#D7E7C4",
    bd=0,
    bg="#D7E7C4"
)
button_4.place(
    x=1024.0,
    y=15.0,
    width=33.0,
    height=36.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat",
    activebackground="#D7E7C4",
    bd=0,
    bg="#D7E7C4"
)
button_5.place(
    x=244.0,
    y=12.0,
    width=41.0,
    height=44.0
)

canvas.create_text(
    11.0,
    422.0,
    anchor="nw",
    text="Porcentagem da receita gasta",
    fill="#000000",
    font=("Montserrat", 12 * -1, "bold")
)
button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (clear_frame(main_frame),show_home_frame,on_button_click(6)),
    relief="flat",
    activebackground="#FAFDF7",
    bd=0,
    bg="#FAFDF7"
)

button_6.place(
    x=11.0,
    y=110.0,
    width=293.0,
    height=55.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))

button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (show_despesas_frame(),on_button_click(7)), # Exemplo de outro botão
    relief="flat",
    activebackground="#FAFDF7",
    bd=0,
    bg="#FAFDF7"
)

button_7.place(
    x=11.0,
    y=187.0,
    width=293.0,
    height=53.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))

button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (clear_frame(main_frame),on_button_click(8)),
    relief="flat",
    activebackground="#FAFDF7",
    bd=0,
    bg="#FAFDF7"
)
button_8.place(
    x=11.0,
    y=262.0,
    width=293.0,
    height=55.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))

button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (clear_frame(main_frame),on_button_click(9)),
    relief="flat",
    activebackground="#FAFDF7",
    bd=0,
    bg="#FAFDF7"
)
button_9.place(
    x=11.0,
    y=338.0,
    width=293.0,
    height=54.0
)

canvas.create_rectangle(
    9.0,
    417.9999999999999,
    304.0,
    420.0,
    fill="#C4BDBD",
    outline="")

canvas.create_rectangle(
    9.0,
    515.0,
    304.0,
    517.0,
    fill="#C4BDBD",
    outline="")

pressed_button = None
main_frame = Frame(window, bg="#FFFFFF")
main_frame.place(x=315, y=68, width=775, height=632)

show_home_frame()

window.mainloop()
