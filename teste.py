import customtkinter as ctk
from tkinter import *
from tkinter import ttk

# Configuração inicial
ctk.set_appearance_mode("light")  # Modos: "System" (Padrão), "Dark", "Light"
ctk.set_default_color_theme("green")  # Cores: "blue" (Padrão), "green", "dark-blue"

# Função para adicionar transações (Exemplo)
def add_transaction(date, amount, account):
    transactions.insert("", "end", values=(date, amount, account))

# Função para deletar as transações selecionadas
def delete_selected_transactions():
    for item in transactions.selection():
        transactions.delete(item)  # Deleta a transação da Treeview

# Função para adicionar uma nova transação a partir dos campos de entrada
def add_transaction_from_input():
    date = entry_date.get()
    amount = entry_amount.get()
    account = entry_account.get()
    if not date or not amount or not account:
        return  # Não adiciona se algum campo estiver vazio

    add_transaction(date, amount, account)

    # Limpa os campos de entrada após adicionar a transação
    entry_date.delete(0, END)
    entry_amount.delete(0, END)
    entry_account.delete(0, END)

# Evento para selecionar uma transação ao clicar na Treeview
def select_transaction(event):
    pass  # Não precisamos fazer nada aqui para selecionar, a seleção múltipla já é suportada por padrão

# Formata a data automaticamente
def format_date(event):
    content = entry_date.get().replace("/", "")  # Remove qualquer / existente
    formatted = ""
    for i, char in enumerate(content):
        if i in (2, 4):
            formatted += "/"
        formatted += char
    entry_date.delete(0, END)
    entry_date.insert(0, formatted[:10])  # Limita a 10 caracteres incluindo os /

# Restringe a inserção de letras no campo de data
def validate_date(content):
    return content.isdigit() or content == ""

# Formata o campo de valor para adicionar "R$" automaticamente
def format_amount(event):
    content = entry_amount.get()
    if not content.startswith("R$"):
        entry_amount.delete(0, END)
        entry_amount.insert(0, "R$" + content)

# Layout da interface
app = ctk.CTk()
app.title("FinPlanner")
app.geometry("800x600")

# Widgets do frame direito
frame_right = ctk.CTkFrame(app)
frame_right.pack(side="right", fill="both", expand=True)

header_frame = ctk.CTkFrame(frame_right)
header_frame.pack(fill="x", pady=10)

label_header = ctk.CTkLabel(header_frame, text="Despesas", font=ctk.CTkFont(size=20, weight="bold"))
label_header.pack(side="left", padx=20)

button_delete = ctk.CTkButton(header_frame, text="Delete", command=delete_selected_transactions)
button_delete.pack(side="right", padx=10)

# Adiciona o frame para entrada de nova transação
entry_frame = ctk.CTkFrame(frame_right)
entry_frame.pack(fill="x", pady=10)

label_date = ctk.CTkLabel(entry_frame, text="Date")
label_date.pack(side="left", padx=5)

entry_date = ctk.CTkEntry(entry_frame, validate="key")
entry_date.pack(side="left", padx=5)
entry_date.bind("<KeyRelease>", format_date)  # Bind the formatting function to KeyRelease event

label_amount = ctk.CTkLabel(entry_frame, text="Amount")
label_amount.pack(side="left", padx=5)
entry_amount = ctk.CTkEntry(entry_frame)
entry_amount.pack(side="left", padx=5)
entry_amount.bind("<FocusOut>", format_amount)

label_account = ctk.CTkLabel(entry_frame, text="Account")
label_account.pack(side="left", padx=5)
entry_account = ctk.CTkEntry(entry_frame)
entry_account.pack(side="left", padx=5)

button_add = ctk.CTkButton(entry_frame, text="Add Transaction", command=add_transaction_from_input)
button_add.pack(side="left", padx=10)

# Tabela de transações
columns = ("Date", "Amount", "Account")
transactions = ttk.Treeview(frame_right, columns=columns, show="headings", height=20)

# Ajusta a largura das colunas para preencher toda a área da Treeview
for col in columns:
    transactions.heading(col, text=col)
    transactions.column(col, minwidth=0, width=200, stretch=YES)

# Estilo para a Treeview
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",
                background="#E5EFDB",
                foreground="black",
                rowheight=25,
                fieldbackground="#E5EFDB")
style.map('Treeview', background=[('selected', '#4CAF50')])

transactions.pack(fill="both", padx=20, pady=20, expand=True)

# Exemplo de transações
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

# Liga o evento ao clique do botão esquerdo do mouse na Treeview
transactions.bind("<ButtonRelease-1>", select_transaction)

# Iniciar a aplicação
app.mainloop()
