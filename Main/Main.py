from tkinter import *

index = Tk()

class Application():
    def __init__(self):
        self.index = index
        self.TelaConfig()
        self.Frames()
        self.LabelsEntry()
        self.Botoes()
        self.index.mainloop()

    def TelaConfig(self):
        self.index.title("VENDAS")
        self.index.configure(background= '#DCDCDC')
        self.index.resizable(True, True)
        self.index.geometry("1280x720")
        self.index.maxsize(width=1500, height=800)
        self.index.minsize(width=1280, height=720)

    def Botoes(self):
            ## INDEX
        self.btnClientes = Button(self.index,text='CLIENTES', command=self.TelaCadastroCliente)
        self.btnClientes.place(relx=0.88, rely=0.13, relwidth=0.1, relheight=0.2)

        self.btnFornecedor = Button(self.index,text='Fornecedores')
        self.btnFornecedor.place(relx=0.88, rely=0.34, relwidth=0.1, relheight=0.2)

        self.btnProduto = Button(self.index,text='PRODUTOS')
        self.btnProduto.place(relx=0.88, rely=0.55, relwidth=0.1, relheight=0.2)

        self.btnFuncionarios = Button(self.index,text='PRODUTOS')
        self.btnFuncionarios.place(relx=0.88, rely=0.76, relwidth=0.1, relheight=0.2)

        self.btnPagamento = Button(self.index,text='PAGAMENTO', background='#00FF7F')
        self.btnPagamento.place(relx=0.60, rely=0.85, relwidth=0.12, relheight=0.09)

        self.btnCancelar = Button(self.index,text='CANELAR VENDA', background='#DC143C')
        self.btnCancelar.place(relx=0.74, rely=0.85, relwidth=0.12, relheight=0.09)

            ## FRAME1
        self.btnPesquisaCliente = Button(self.frame1,text='Pesquisar Cliente')
        self.btnPesquisaCliente.place(relx=0.70, rely=0.1,relwidth=0.30, relheight=-2)

            ## FRAME2
        self.btnPesquisaProduto = Button(self.frame2,text='Pesquisar Produto')
        self.btnPesquisaProduto.place(relx=0.48, rely=-0.1,relwidth=0.30, relheight=0.1)

        self.btnAdicionar = Button(self.frame2,text='Adicionar Item',background= '#DCDCDC')
        self.btnAdicionar.place(relx=0.15, rely=0.7,relwidth=0.60, relheight=0.2)

             ## FRAME3

    def LabelsEntry(self):
            ## FRAME1   
       self.lbCPF = Label(self.frame1, text='CPF:' ,background="#A9A9A9", font="3")
       self.lbCPF.place(relx=-0.12, rely=3.0)
       self.entryCPF = Entry(self.frame1)
       self.entryCPF.place(relx=-0.02, rely=3.3,relwidth=0.5, relheight=-2 )

       self.lbDataVenda = Label(self.frame1, text='Data da Venda:' ,background="#A9A9A9", font="3")
       self.lbDataVenda.place(relx=0.55, rely=3.0)
       self.entryDataVenda = Entry(self.frame1)
       self.entryDataVenda.place(relx=0.78, rely=3.3,relwidth=0.19, relheight=-2 )

       self.lbNome = Label(self.frame1, text='Nome Cliente:' ,background="#A9A9A9", font="3")
       self.lbNome.place(relx=-0.12, rely=-0.1)
       self.entryNome = Entry(self.frame1)
       self.entryNome.place(relx=0.08, rely=0.1,relwidth=0.60, relheight=-2 )

           ## FRAME2

       self.lbCodigo = Label(self.frame2, text='Código:', font="3")
       self.lbCodigo.place(relx=-0.12, rely=-0.1)
       self.entryCodigo = Entry(self.frame2)
       self.entryCodigo.place(relx=0.01, rely=-0.1,relwidth=0.45, relheight=0.1 )  

       self.lbProduto= Label(self.frame2, text='Produto:', font="3")
       self.lbProduto.place(relx=-0.12, rely=0.1)
       self.entryProduto = Entry(self.frame2)
       self.entryProduto.place(relx=0.01, rely=0.1,relwidth=0.75, relheight=0.1 ) 

       self.lbQtd= Label(self.frame2, text='Qtd:', font="5")
       self.lbQtd.place(relx=-0.07, rely=0.25)
       self.entryQtd = Entry(self.frame2)
       self.entryQtd.place(relx=0.01, rely=0.25,relwidth=0.10, relheight=0.1 )

       self.lbPreco= Label(self.frame2, text='PREÇO:', font="5")
       self.lbPreco.place(relx=0.18, rely=0.25)
       self.entryPreco = Entry(self.frame2)
       self.entryPreco.place(relx=0.30, rely=0.25,relwidth=0.20, relheight=0.1 )  

            ## FRAME3
       self.lbTotal = Label(self.frame3, text='TOTAL:' ,background="#D2B48C", font="3")
       self.lbTotal.place(relx=-0.2, rely=0.7)
       self.entryTotal = Entry(self.frame3)
       self.entryTotal.place(relx=0.2, rely=0.7,relwidth=0.9, relheight=-0.5 )

    def Frames(self):
        self.frame = Frame(self.index,border=80, )
        self.frame.place(relx=0.59,rely=0.13, relwidth=0.28, relheight=0.52)

        self.frame1 = Frame(self.index,border=80,background="#A9A9A9")
        self.frame1.place(relx=0.01,rely=0.13, relwidth=0.57, relheight=0.20)

        self.frame2 = Frame(self.index,border=80)
        self.frame2.place(relx=0.01,rely=0.35, relwidth=0.57, relheight=0.60)

        self.frame3 = Frame(self.index,border=80, background= '#D2B48C')
        self.frame3.place(relx=0.59,rely=0.67, relwidth=0.28, relheight=0.13)

    def TelaCadastroCliente(self):
            from CadastroCliente import Application
            self.janela = Toplevel(Application)
            self.janela.focus_force()
            self.janela.grab_set()
            
        

Application()    