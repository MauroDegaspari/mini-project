from tkinter import *

windowCadastroCliente = Tk()

class Application(): ##Classe que irar inicializar a aplicação
    def __init__(self):
        self.windowCadastroCliente = windowCadastroCliente
        self.TelaConfig()
        self.FramesDeTela()
        self.LabelsEntry()
        self.Botoes()
        windowCadastroCliente.mainloop()

    def TelaConfig(self): ## Configuração de tela
         self.windowCadastroCliente.title("CADASTRO DE CLIENTES")
         self.windowCadastroCliente.configure(background= 'gray')
         self.windowCadastroCliente.resizable(True, True)
         self.windowCadastroCliente.geometry("1280x720")
         self.windowCadastroCliente.maxsize(width=1500, height=800)
         self.windowCadastroCliente.minsize(width=1280, height=720)

    def FramesDeTela(self):
        self.frame1 = Frame(self.windowCadastroCliente, border=80, )
        self.frame1.place(relx=0.02,rely=0.20, relwidth=0.95, relheight=0.70)
    
    def LabelsEntry(self):
        self.lbCodigo = Label(self.frame1, text='Código:')
        self.lbCodigo.place(relx=-0.06, rely=-0.09)
        self.entryCodigo = Entry(self.frame1)
        self.entryCodigo.place(relx=-0.01, rely=-0.08,relwidth=0.09, relheight=0.05 )

        self.lbNome = Label(self.frame1, text='Nome:')
        self.lbNome.place(relx=-0.06, rely=-0.01)
        self.entryNome = Entry(self.frame1)
        self.entryNome.place(relx=-0.01, rely=-0.00,relwidth=0.32, relheight=0.05 )
        
        self.lbEmail = Label(self.frame1, text='Email:')
        self.lbEmail.place(relx=-0.06, rely=0.07)
        self.entryEmail = Entry(self.frame1)
        self.entryEmail.place(relx=-0.01, rely=0.07,relwidth=0.20, relheight=0.05 )

        self.lbCelular = Label(self.frame1, text='Celular:')
        self.lbCelular.place(relx=0.20, rely=0.07)
        self.entryCelular = Entry(self.frame1)
        self.entryCelular.place(relx=0.25, rely=0.07,relwidth=0.15, relheight=0.05 )

        self.lbFixo = Label(self.frame1, text='Fixo:')
        self.lbFixo.place(relx=0.41, rely=0.07)
        self.entryFixo = Entry(self.frame1)
        self.entryFixo.place(relx=0.45, rely=0.07,relwidth=0.15, relheight=0.05 )

        self.lbEndereco = Label(self.frame1, text='Endereço:')
        self.lbEndereco.place(relx=-0.07, rely=0.14)
        self.entryEndereco = Entry(self.frame1)
        self.entryEndereco.place(relx=-0.01, rely=0.14,relwidth=0.34, relheight=0.05 )

        self.lbCEP = Label(self.frame1, text='CEP:')
        self.lbCEP.place(relx=0.34, rely=0.14)
        self.entryCEP = Entry(self.frame1)
        self.entryCEP.place(relx=0.37, rely=0.14,relwidth=0.15, relheight=0.05 )

        self.lbNumero = Label(self.frame1, text='N:')
        self.lbNumero.place(relx=0.54, rely=0.14)
        self.entryNumero = Entry(self.frame1)
        self.entryNumero.place(relx=0.56, rely=0.14,relwidth=0.04, relheight=0.05 )

        self.lbBairro = Label(self.frame1, text='Bairro:')
        self.lbBairro.place(relx=-0.07, rely=0.21)
        self.entryBairro = Entry(self.frame1)
        self.entryBairro.place(relx=-0.01, rely=0.21,relwidth=0.12, relheight=0.05 )

        self.lbCidade = Label(self.frame1, text='Cidade:')
        self.lbCidade.place(relx=0.12, rely=0.21)
        self.entryCidade = Entry(self.frame1)
        self.entryCidade.place(relx=0.17, rely=0.21,relwidth=0.14, relheight=0.05 )

        self.lbComplemento = Label(self.frame1, text='Complemento:')
        self.lbComplemento.place(relx=0.32, rely=0.21)
        self.entryComplemento = Entry(self.frame1)
        self.entryComplemento.place(relx=0.40, rely=0.22,relwidth=0.11, relheight=0.05 )

        self.lbUF = Label(self.frame1,text="UF")
        self.lbUF.place(relx=0.57, rely=0.21)

        self.lbRG = Label(self.frame1, text='RG:')
        self.lbRG.place(relx=-0.05, rely=0.28)
        self.entryRG = Entry(self.frame1)
        self.entryRG.place(relx=-0.01, rely=0.28,relwidth=0.14, relheight=0.05 )

        self.lbCPF = Label(self.frame1, text='CPF:')
        self.lbCPF.place(relx=0.16, rely=0.28)
        self.entryCPF = Entry(self.frame1)
        self.entryCPF.place(relx=0.20, rely=0.28,relwidth=0.11, relheight=0.05 )

    def Botoes(self):
        self.btLimpar = Button(self.frame1, text="Limpar")
        self.btLimpar.place(relx=0.90, rely=0.01,relwidth=0.1, relheight=0.2 )

        self.btPesquisa = Button(self.frame1, text='Pesquisa')
        self.btPesquisa.place(relx=0.33, rely=-0.04,relwidth=0.12, relheight=0.09 )

Application()

