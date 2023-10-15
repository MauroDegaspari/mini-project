from tkinter import *
from subprocess import run

index = Tk()

class Application():
    def __init__(self,*args,**argvs):
        self.index = index
        self.TelaConfig()
        self.Frames()
        self.Botoes()
        self.index.mainloop()

    def TelaConfig(self):
        self.index.title("VENDAS")
        self.index.configure(background= 'gray')
        self.index.resizable(True, True)
        self.index.geometry("1280x720")
        self.index.maxsize(width=1500, height=800)
        self.index.minsize(width=1280, height=720)

    def Botoes(self):
        self.btnClientes = Button(self.index,text='CLIENTES', command=self.TelaCadastroCliente)
        self.btnClientes.place(relx=0.88, rely=0.13, relwidth=0.1, relheight=0.2)

        self.btnFornecedor = Button(self.index,text='Fornecedores')
        self.btnFornecedor.place(relx=0.88, rely=0.34, relwidth=0.1, relheight=0.2)

        self.btnProduto = Button(self.index,text='PRODUTOS')
        self.btnProduto.place(relx=0.88, rely=0.55, relwidth=0.1, relheight=0.2)

        self.btnFuncionarios = Button(self.index,text='PRODUTOS')
        self.btnFuncionarios.place(relx=0.88, rely=0.76, relwidth=0.1, relheight=0.2)

    def Frames(self):
        self.frame = Frame(self.index,border=80)
        self.frame.place(relx=0.59,rely=0.13, relwidth=0.28, relheight=0.82)

        self.frame1 = Frame(self.index,border=80)
        self.frame1.place(relx=0.01,rely=0.13, relwidth=0.57, relheight=0.20)

        self.frame2 = Frame(self.index,border=80)
        self.frame2.place(relx=0.01,rely=0.35, relwidth=0.57, relheight=0.60)

    def TelaCadastroCliente(self):
            from CadastroCliente import Application
            self.janela = Toplevel(Application)
            self.janela.focus_force()
            self.janela.grab_set()
            
        

Application()    