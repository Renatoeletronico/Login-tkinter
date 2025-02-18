import customtkinter as ctk
from bd.database import autenticar_usuario
from telas.registro import abrir_tela_registro

def abrir_tela_login():
    root = ctk.CTk()
    root.title("Login")
    root.geometry("300x300")

    ctk.CTkLabel(root, text="Usuário:").pack(pady=5)
    entry_usuario = ctk.CTkEntry(root)
    entry_usuario.pack(pady=5)

    ctk.CTkLabel(root, text="Senha:").pack(pady=5)
    entry_senha = ctk.CTkEntry(root, show="*")
    entry_senha.pack(pady=5)

    def tentar_login():
        usuario = entry_usuario.get()
        senha = entry_senha.get()
        if autenticar_usuario(usuario, senha):
            ctk.CTkLabel(root, text="Login bem-sucedido!", fg_color="green").pack(pady=5)
        else:
            ctk.CTkLabel(root, text="Usuário ou senha incorretos!", fg_color="red").pack(pady=5)

    ctk.CTkButton(root, text="Login", command=tentar_login).pack(pady=10)
    ctk.CTkButton(root, text="Registrar", command=abrir_tela_registro).pack(pady=10)

    root.mainloop()
