import tkinter as tk
from tkinter import ttk

def salvar_fornecedor():
    # Seu código de processamento dos dados aqui
    pass

# Configurar a janela principal
root = tk.Tk()
root.title("Cadastro de Fornecedores - Sistema de Supermercados")

# Criar um quadro para organização
frame = ttk.Frame(root)
frame.grid(row=4, column=5, padx=20, pady=20)

# Adicionar estilo
style = ttk.Style()
style.configure("TButton", foreground="black", background="blue", font=('Helvetica', 12))
style.configure("TLabel", foreground="blue", font=('Helvetica', 12))
style.configure("Treeview", font=('Helvetica', 10))

# Função para centralizar os widgets horizontalmente na célula da grade
def centralizar_horizontal(widget):
    widget.grid_configure(sticky="ew")

# Criar rótulos e campos de entrada para os dados do fornecedor

label_ID = ttk.Label(frame, text="ID")
label_ID.grid(row=0, column=0, padx=5, pady=5)
entry_ID = ttk.Entry(frame)
entry_ID.grid(row=1, column=1, padx=5, pady=5)
centralizar_horizontal(entry_ID)

label_nome = ttk.Label(frame, text="Nome do Fornecedor")
label_nome.grid(row=0, column=0, padx=5, pady=5)
entry_nome = ttk.Entry(frame)
entry_nome.grid(row=0, column=1, padx=5, pady=5)
centralizar_horizontal(entry_nome)

label_cnpj = ttk.Label(frame, text="CNPJ do Fornecedor")
label_cnpj.grid(row=1, column=0, padx=5, pady=5)
entry_cnpj = ttk.Entry(frame)
entry_cnpj.grid(row=1, column=1, padx=5, pady=5)
centralizar_horizontal(entry_cnpj)

label_endereco = ttk.Label(frame, text="Endereço do Fornecedor")
label_endereco.grid(row=2, column=0, padx=5, pady=5)
entry_endereco = ttk.Entry(frame)
entry_endereco.grid(row=2, column=1, padx=5, pady=5)
centralizar_horizontal(entry_endereco)

label_email = ttk.Label(frame, text="Email do Fornecedor")
label_email.grid(row=3, column=0, padx=5, pady=5)
entry_email = ttk.Entry(frame)
entry_email.grid(row=3, column=1, padx=5, pady=5)
centralizar_horizontal(entry_email)

label_telefone = ttk.Label(frame, text="Telefone do Fornecedor")
label_telefone.grid(row=4, column=0, padx=5, pady=5)
entry_telefone = ttk.Entry(frame)
entry_telefone.grid(row=4, column=1, padx=5, pady=5)
centralizar_horizontal(entry_telefone)

label_produtos = ttk.Label(frame, text="Produtos Fornecidos")
label_produtos.grid(row=5, column=0, padx=5, pady=5)
entry_produtos = tk.Text(frame, height=5, width=30)
entry_produtos.grid(row=5, column=1, padx=5, pady=5, columnspan=2)
centralizar_horizontal(entry_produtos)

# Botão para salvar fornecedor
btn_salvar = ttk.Button(frame, text="Salvar Fornecedor", command=salvar_fornecedor)
btn_salvar.grid(row=6, column=0, columnspan=2, padx=5, pady=10)
centralizar_horizontal(btn_salvar)

# Iniciar o loop principal
root.mainloop()
