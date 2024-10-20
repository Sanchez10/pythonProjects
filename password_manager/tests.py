import tkinter as tk

def toggle_password() -> None:
    if show_password.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# Cria a janela principal
root = tk.Tk()
root.title("Exemplo de Senha")

# Variável para rastrear o estado da caixa de seleção
show_password = tk.BooleanVar()

# Rótulo e entrada para a senha
password_label = tk.Label(root, text="Senha:")
password_label.pack(pady=5)

password_entry = tk.Entry(root, show="*")  # O argumento 'show' oculta os caracteres da senha
password_entry.pack(pady=5)

# Caixa de seleção para mostrar a senha
show_password_checkbox = tk.Checkbutton(root, text="Mostrar Senha", variable=show_password, command=toggle_password)
show_password_checkbox.pack(pady=5)

# Botão de exemplo
submit_button = tk.Button(root, text="Enviar")
submit_button.pack(pady=10)

# Inicia o loop principal
root.mainloop()
