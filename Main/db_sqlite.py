import sqlite3

conn = sqlite3.connect('banco/Script_BD_Vendas.db')
cursor = conn.cursor()

def BancoDeDados():
    cursor.execute("DROP TABLE IF EXISTS tb_clientes")
    cursor.execute("CREATE TABLE tb_clientes (                         "+
               "  id          INTEGER PRIMARY KEY AUTOINCREMENT    "+
               " ,nome        TEXT NOT NULL                        "+
               " ,rg          TEXT NOT NULL                        "+
               " ,cpf         TEXT NOT NULL                        "+
               " ,email       TEXT                                 "+
               " ,telefone    TEXT                                 "+
               " ,celular     TEXT                                 "+
               " ,cep         TEXT                                 "+
               " ,endereco    TEXT                                 "+
               " ,numero      INTEGER                              "+
               " ,complemento TEXT                                 "+
               " ,bairro      TEXT                                 "+
               " ,cidade      TEXT                                 "+
               " ,estado TEXT )")
    
    print('CRIADO TABELA CLIENTES --> SUCESSO ')
   