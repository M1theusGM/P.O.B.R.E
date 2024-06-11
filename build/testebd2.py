import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

# Função para criar o banco de dados de um novo usuário
def create_user_db(username):
    conn = sqlite3.connect(f'{username}.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS data (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      info TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Função para registrar um novo usuário
def register():
    username = entry_username.get()
    password = entry_password.get()
    
    if username and password:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)')
        
        cursor.execute('SELECT * FROM users WHERE username=?', (username,))
        if cursor.fetchone():
            messagebox.showerror("Erro", "Usuário já existe!")
        else:
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            create_user_db(username)
            messagebox.showinfo("Sucesso", "Usuário registrado com sucesso!")
        
        conn.close()
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

# Função para fazer login de um usuário existente
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    
    if cursor.fetchone():
        messagebox.showinfo("Sucesso", "Login bem-sucedido!")
        load_user_db(username)
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

# Interface Tkinter
root = tk.Tk()
root.title("Login")

tk.Label(root, text="Usuário").pack()
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Senha").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="Registrar", command=register).pack()
tk.Button(root, text="Login", command=login).pack()

root.mainloop()
