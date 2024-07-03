from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import sqlite3

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



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\mathe\Documents\Programação\build2\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("1090x700")
window.configure(bg = "#FFFFFF")

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

canvas.create_rectangle(
    0.0,
    68.0,
    315.0,
    700.0,
    fill="#FAFDF7",
    outline="")

canvas.create_rectangle(
    348.0,
    154.0,
    727.0,
    382.0,
    fill="#FAFDF7",
    outline="")

canvas.create_rectangle(
    348.0,
    399.0,
    801.0,
    678.0,
    fill="#FAFDF7",
    outline="")

canvas.create_rectangle(
    741.0,
    154.0,
    1071.0,
    382.0,
    fill="#FAFDF7",
    outline="")

canvas.create_rectangle(
    816.0,
    399.0,
    1071.0,
    678.0,
    fill="#FAFDF7",
    outline="")

canvas.create_text(
    348.0,
    87.0,
    anchor="nw",
    text="Bem Vindo!",
    fill="#000000",
    font=("Montserrat", 26 * -1, "bold")
)

canvas.create_text(
    375.0,
    175.0,
    anchor="nw",
    text="Minha Receita",
    fill="#000000",
    font=("Montserrat", 14 * -1, "bold")
)

canvas.create_text(
    375.0,
    420.0,
    anchor="nw",
    text="Distribuição das Despesas",
    fill="#000000",
    font=("MontserratRoman Bold", 14 * -1, "bold")
)

canvas.create_text(
    771.0,
    172.0,
    anchor="nw",
    text="Despesas Recentes",
    fill="#000000",
    font=("Montserrat", 14 * -1, "bold")
)

canvas.create_text(
    848.0,
    423.0,
    anchor="nw",
    text="Top Despesas",
    fill="#000000",
    font=("Montserrat", 14 * -1, "bold")
)

canvas.create_text(
    375.0,
    229.0,
    anchor="nw",
    text="Valor em Banco",
    fill="#000000",
    font=("Montserrat", 11 * -1, "bold")
)

canvas.create_text(
    601.0,
    229.0,
    anchor="nw",
    text="R$ 4.531,00",
    fill="#000000",
    font=("Montserrat", 14 * -1, "bold")
)

canvas.create_text(
    601.0,
    323.0,
    anchor="nw",
    text="R$ 2.210,00",
    fill="#000000",
    font=("Montserrat", 14 * -1, "bold")
)

canvas.create_text(
    601.0,
    275.0,
    anchor="nw",
    text="R$ 2.321,00",
    fill="#000000",
    font=("Montserrat", 14 * -1, "bold")
)

canvas.create_text(
    375.0,
    323.0,
    anchor="nw",
    text="Total Caixa",
    fill="#000000",
    font=("Montserrat", 11 * -1, "bold")
)

canvas.create_text(
    375.0,
    275.0,
    anchor="nw",
    text="Despesas",
    fill="#000000",
    font=("Montserrat", 11 * -1, "bold")
)

canvas.create_text(
    11.0,
    678.0,
    anchor="nw",
    text="All rights reserved © - P.O.B.R.E ",
    fill="#000000",
    font=("Montserrat", 12 * -1, "bold")
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
    command=lambda: on_button_click(6),
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
    command=lambda: on_button_click(7),
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
    command=lambda: on_button_click(8),
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
    command=lambda: on_button_click(9),
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

window.resizable(False, False)
window.mainloop()
