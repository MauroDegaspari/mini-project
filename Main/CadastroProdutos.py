from tkinter import *
from tkinter import ttk

windowCadastroProduto = Tk()

class Application():
    def __init__(self):
        self.windowCadastroProduto = windowCadastroProduto
        self.ConfigTela()
        self.Frames()
        self.Abas()
        self.LabelEEntry()
        self.Botoes()
        self.windowCadastroProduto.mainloop()

    def ConfigTela(self):
         self.windowCadastroProduto.title("CADASTRO DE PRODUTOS")
         self.windowCadastroProduto.configure(background= 'gray')
         self.windowCadastroProduto.resizable(True, True)
         self.windowCadastroProduto.geometry("800x500")
         self.windowCadastroProduto.maxsize(width=800, height=500)
         self.windowCadastroProduto.minsize(width=350, height=400)

    def Frames(self):
        self.frameTOP = Frame(self.windowCadastroProduto, border=80 )
        self.frameTOP.place(relx=0.01,rely=0.03, relwidth=0.98, relheight=0.15)

    def Abas(self):
        self.abas = ttk.Notebook(self.windowCadastroProduto)
        
        self.aba1 = Frame(self.abas)
        self.aba1.configure(background="#C0C0C0")
        self.abas.add(self.aba1, text="Cadastros")
        
        self.aba2 = Frame(self.abas)
        self.aba2.configure(background="pink")
        self.abas.add(self.aba2, text="Custo/preço de venda")

        self.abas.place(relx=0.01,rely=0.20, relwidth=0.98, relheight=0.70)

    def LabelEEntry(self):
        
        self.lbDescricao = Label(self.aba1, text='Descrição:')
        self.lbDescricao.place(relx=0.01, rely=0.01)
        self.entryDescricao = Entry(self.aba1)
        self.entryDescricao.place(relx=0.12, rely=0.03,relwidth=0.30, relheight=0.10 )

        self.lbDescricao = Label(self.aba1, text='Preço:')
        self.lbDescricao.place(relx=0.04, rely=0.13)
        self.entryDescricao = Entry(self.aba1)
        self.entryDescricao.place(relx=0.12, rely=0.15,relwidth=0.10, relheight=0.10 )

        self.lbDescricao = Label(self.aba1, text='Quantidade:')
        self.lbDescricao.place(relx=0.00, rely=0.26)
        self.entryDescricao = Entry(self.aba1)
        self.entryDescricao.place(relx=0.12, rely=0.27,relwidth=0.10, relheight=0.10 )


    def Botoes(self):
        self.btnNovo = Button(self.windowCadastroProduto, text='Incluir Produto')
        self.btnNovo.place(relx=0.01, rely=0.92, relwidth=0.2, relheight=0.07)

        self.btnLocalizar = Button(self.windowCadastroProduto, text='Localizar Produto')
        self.btnLocalizar.place(relx=0.23, rely=0.92, relwidth=0.2, relheight=0.07)

        self.btnLocalizar = Button(self.windowCadastroProduto, text='Exluir Produto')
        self.btnLocalizar.place(relx=0.45, rely=0.92, relwidth=0.2, relheight=0.07)

        self.btnSair = Button(self.windowCadastroProduto, text='SAIR')
        self.btnSair.place(relx=0.79, rely=0.92, relwidth=0.2, relheight=0.07)

Application()