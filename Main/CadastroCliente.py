from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from db_sqlite import *


windowCadastroCliente = Tk()

class FuncoesApp():
    def btn_limpar(self):
        self.entryCodigo.delete(0,END)
        self.entryNome.delete(0,END)
        self.entryEmail.delete(0,END)
        self.entryCelular.delete(0,END)
        self.entryFixo.delete(0,END)
        self.entryCEP.delete(0,END)
        self.entryEndereco.delete(0,END)
        self.entryNumero.delete(0,END)
        self.entryBairro.delete(0,END)
        self.entryCidade.delete(0,END)
        self.entryComplemento.delete(0,END)
        self.entryRG.delete(0,END)
        self.entryCPF.delete(0,END)

    def btn_novo(self):
       self.nome = str(self.entryNome.get())
       self.email = self.entryEmail.get()
       self.celular = self.entryCelular.get()
       self.telefone = self.entryFixo.get()
       self.cep = self.entryCEP.get()
       self.endereco = self.entryEndereco.get()
       self.numero = self.entryNumero.get()
       self.bairro = self.entryBairro.get()
       self.cidade = self.entryCidade.get()
       self.complemento = self.entryComplemento.get()
       self.rg = self.entryRG.get()
       self.cpf = self.entryCPF.get()
       self.estado ="PE"

       if (self.nome == "" or self.cpf == "" or self.rg == ""):
          messagebox.showinfo('Validação', 'Os Campos: Nome, Rg e CPF são obrigatórios.')
       else:            
           NovoCliente(self.nome, self.rg, self.cpf,self.email,self.telefone,self.celular,self.cep,self.endereco,self.numero,self.complemento,self.bairro, self.cidade, self.estado)
           self.btn_limpar()
   
    def Select_ListaCliente(self):
       ## self.lista.delete(self.lista.get_children)
        SelectCliente(self.lista)


class Application(FuncoesApp): ##Classe que irar inicializar a aplicação
    def __init__(self):
        self.windowCadastroCliente = windowCadastroCliente
        self.TelaConfig()
        BancoDeDados()
        self.FramesDeTela()
        self.LabelsEntry()
        self.listaClientes()
        self.Botoes()
        self.Select_ListaCliente()
        windowCadastroCliente.mainloop()

    def TelaConfig(self): ## Configuração de tela
         self.windowCadastroCliente.title("CADASTRO DE CLIENTES")
         self.windowCadastroCliente.configure(background= 'gray')
         self.windowCadastroCliente.resizable(True, True)
         self.windowCadastroCliente.geometry("1280x720")
         self.windowCadastroCliente.maxsize(width=1500, height=800)
         self.windowCadastroCliente.minsize(width=1280, height=720)

    def FramesDeTela(self):
        self.frame = Frame(self.windowCadastroCliente, border=80 )
        self.frame.place(relx=0.02,rely=0.20, relwidth=0.95, relheight=0.70)
        self.frame1 = Frame(self.windowCadastroCliente, background='blue')
        self.frame1.place(relx=0.02,rely=0.01, relwidth=0.95, relheight=0.17)
    
    def LabelsEntry(self):
        self.lbCodigo = Label(self.frame, text='Código:')
        self.lbCodigo.place(relx=-0.06, rely=-0.09)
        self.entryCodigo = Entry(self.frame)
        self.entryCodigo.place(relx=-0.01, rely=-0.08,relwidth=0.09, relheight=0.05 )

        self.lbNome = Label(self.frame, text='Nome:')
        self.lbNome.place(relx=-0.06, rely=-0.01)
        self.entryNome = Entry(self.frame)
        self.entryNome.place(relx=-0.01, rely=-0.00,relwidth=0.32, relheight=0.05 )
        
        self.lbEmail = Label(self.frame, text='Email:')
        self.lbEmail.place(relx=-0.06, rely=0.07)
        self.entryEmail = Entry(self.frame)
        self.entryEmail.place(relx=-0.01, rely=0.07,relwidth=0.20, relheight=0.05 )

        self.lbCelular = Label(self.frame, text='Celular:')
        self.lbCelular.place(relx=0.20, rely=0.07)
        self.entryCelular = Entry(self.frame)
        self.entryCelular.place(relx=0.25, rely=0.07,relwidth=0.15, relheight=0.05 )

        self.lbFixo = Label(self.frame, text='Fixo:')
        self.lbFixo.place(relx=0.41, rely=0.07)
        self.entryFixo = Entry(self.frame)
        self.entryFixo.place(relx=0.45, rely=0.07,relwidth=0.15, relheight=0.05 )

        self.lbEndereco = Label(self.frame, text='Endereço:')
        self.lbEndereco.place(relx=-0.07, rely=0.14)
        self.entryEndereco = Entry(self.frame)
        self.entryEndereco.place(relx=-0.01, rely=0.14,relwidth=0.34, relheight=0.05 )

        self.lbCEP = Label(self.frame, text='CEP:')
        self.lbCEP.place(relx=0.34, rely=0.14)
        self.entryCEP = Entry(self.frame)
        self.entryCEP.place(relx=0.37, rely=0.14,relwidth=0.15, relheight=0.05 )

        self.lbNumero = Label(self.frame, text='N:')
        self.lbNumero.place(relx=0.54, rely=0.14)
        self.entryNumero = Entry(self.frame)
        self.entryNumero.place(relx=0.56, rely=0.14,relwidth=0.04, relheight=0.05 )

        self.lbBairro = Label(self.frame, text='Bairro:')
        self.lbBairro.place(relx=-0.07, rely=0.21)
        self.entryBairro = Entry(self.frame)
        self.entryBairro.place(relx=-0.01, rely=0.21,relwidth=0.12, relheight=0.05 )

        self.lbCidade = Label(self.frame, text='Cidade:')
        self.lbCidade.place(relx=0.12, rely=0.21)
        self.entryCidade = Entry(self.frame)
        self.entryCidade.place(relx=0.17, rely=0.21,relwidth=0.14, relheight=0.05 )

        self.lbComplemento = Label(self.frame, text='Complemento:')
        self.lbComplemento.place(relx=0.32, rely=0.21)
        self.entryComplemento = Entry(self.frame)
        self.entryComplemento.place(relx=0.40, rely=0.22,relwidth=0.11, relheight=0.05 )

        self.lbUF = Label(self.frame,text="UF")
        self.lbUF.place(relx=0.57, rely=0.21)

        self.lbRG = Label(self.frame, text='RG:')
        self.lbRG.place(relx=-0.05, rely=0.28)
        self.entryRG = Entry(self.frame)
        self.entryRG.place(relx=-0.01, rely=0.28,relwidth=0.14, relheight=0.05 )

        self.lbCPF = Label(self.frame, text='CPF:')
        self.lbCPF.place(relx=0.16, rely=0.28)
        self.entryCPF = Entry(self.frame)
        self.entryCPF.place(relx=0.20, rely=0.28,relwidth=0.11, relheight=0.05 )

    def listaClientes(self):
        self.lista = ttk.Treeview(self.frame, height= 3, columns=("col0","col1","col2","col3","col4","col5","col6","col7","col8","col9","col10","col11","col2","col3"))
       ## self.lista.heading("#0", text="")
        self.lista.heading("#1", text="id")
        self.lista.heading("#2", text="Nome")
        self.lista.heading("#3", text="RG")
        self.lista.heading("#4", text="CPF")
        self.lista.heading("#5", text="Email")
        self.lista.heading("#6", text="Telefone")
        self.lista.heading("#7", text="Celular")
        self.lista.heading("#8", text="Cep")
        self.lista.heading("#9", text="Endereco")
        self.lista.heading("#10", text="Numero")
        self.lista.heading("#11", text="Complemento")
        self.lista.heading("#12", text="Bairro")
        self.lista.heading("#13", text="Cidade") 
        self.lista.heading("#14", text="estado")
  
        self.lista.column("#0", width=0)
        self.lista.column("#1", width=10)
        self.lista.column("#2", width=80)
        self.lista.column("#3", width=80)
        self.lista.column("#4", width=80)
        self.lista.column("#5", width=80)
        self.lista.column("#6", width=80)
        self.lista.column("#7", width=80)
        self.lista.column("#8", width=50)
        self.lista.column("#9", width=80)
        self.lista.column("#10", width=80)
        self.lista.column("#11", width=50)
        self.lista.column("#12", width=30)
        self.lista.column("#13", width=30)
        self.lista.column("#14", width=30)

        self.lista.place(relx=-0.01,rely=0.37, relwidth=1.05, relheight=0.70)

        self.scrool = Scrollbar(self.frame, orient='vertical')
        self.lista.configure(yscroll=self.scrool.set)
        self.scrool.place(relx=1.02, rely=0.42, relwidth=0.02,relheight=0.60 )

    def Botoes(self):

        self.btnNovo = Button(self.frame, text='+Novo', command=self.btn_novo)
        self.btnNovo.place(relx=0.62, rely=0.03, relwidth=0.1, relheight=0.2)

        self.btnSalvar = Button(self.frame, text='Salvar')
        self.btnSalvar.place(relx=0.73, rely=0.03, relwidth=0.1, relheight=0.2)

        self.btnExcluir = Button(self.frame, text='Excluir')
        self.btnExcluir.place(relx=0.84, rely=0.03, relwidth=0.1, relheight=0.2)
       
        self.btnLimpar = Button(self.frame, text="Limpar", command=self.btn_limpar)
        self.btnLimpar.place(relx=0.95, rely=0.03,relwidth=0.1, relheight=0.2 )

        self.btPesquisa = Button(self.frame, text='Pesquisa')
        self.btPesquisa.place(relx=0.33, rely=-0.04,relwidth=0.12, relheight=0.09 )

Application()

