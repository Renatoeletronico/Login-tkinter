import customtkinter as ctk
from bd.database import criar_usuario, usuario_existe

def abrir_tela_registro():
    reg_window = ctk.CTk()
    reg_window.title("Registro")
    reg_window.geometry("300x300")

    ctk.CTkLabel(reg_window, text="Novo Usuário:").pack(pady=5)
    entry_usuario = ctk.CTkEntry(reg_window)
    entry_usuario.pack(pady=5)

    ctk.CTkLabel(reg_window, text="Senha:").pack(pady=5)
    entry_senha = ctk.CTkEntry(reg_window, show="*")
    entry_senha.pack(pady=5)

    def registrar():
        usuario = entry_usuario.get()
        senha = entry_senha.get()
        if usuario_existe(usuario):
            ctk.CTkLabel(reg_window, text="Usuário já existe!", fg_color="red").pack(pady=5)
        else:
            criar_usuario(usuario, senha)
            ctk.CTkLabel(reg_window, text="Usuário registrado!", fg_color="green").pack(pady=5)

    ctk.CTkButton(reg_window, text="Registrar", command=registrar).pack(pady=10)

    reg_window.mainloop()
