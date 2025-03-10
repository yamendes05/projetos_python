import customtkinter as ctk

# Configuração da aparência
ctk.set_appearance_mode("dark")

# Criação da janela principal
tela = ctk.CTk()
tela.title("Sistema de Login")
tela.geometry("400x300")

# Criação do campo Usuário
campo_usuario = ctk.CTkLabel(tela, text="Usuário:")
campo_usuario.pack(pady=10)

entrada_usuario = ctk.CTkEntry(tela, placeholder_text="Digite seu usuário")
entrada_usuario.pack(pady=5)

# Criação do campo Senha
campo_senha = ctk.CTkLabel(tela, text="Senha:")
campo_senha.pack(pady=10)

entrada_senha = ctk.CTkEntry(tela, placeholder_text="Digite sua senha", show="*")
entrada_senha.pack(pady=5)

# Função do botão de login
def login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    print(f"Usuário: {usuario}, Senha: {senha}")

# Botão de login
botao_login = ctk.CTkButton(tela, text="Login", command=login)
botao_login.pack(pady=20)

# Iniciar aplicação
tela.mainloop()
