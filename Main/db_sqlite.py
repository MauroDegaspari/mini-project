import sqlite3
from tkinter import END

conn = sqlite3.connect('banco/Script_BD_Vendas.db');
cursor = conn.cursor();
    
def desconectar_bd():
    conn.close()

def BancoDeDados():
    
    cursor.execute("CREATE TABLE IF NOT EXISTS tb_clientes (         "+
                                 "  id          INTEGER PRIMARY KEY AUTOINCREMENT  "+
                                 " ,nome        TEXT NOT NULL                      "+
                                 " ,rg          TEXT NOT NULL                      "+
                                 " ,cpf         TEXT NOT NULL                      "+
                                 " ,email       TEXT                               "+
                                 " ,telefone    TEXT                               "+
                                 " ,celular     TEXT                               "+
                                 " ,cep         TEXT                               "+
                                 " ,endereco    TEXT                               "+
                                 " ,numero      INTEGER                            "+
                                 " ,complemento TEXT                               "+
                                 " ,bairro      TEXT                               "+
                                 " ,cidade      TEXT                               "+
                                 " ,estado      TEXT )")
    
    print('Conexão com Bando de dados--> SUCESSO ');
    conn.commit();

def NovoCliente(nome, rg, cpf, email, telefone, celular, cep, endereco, numero, complemento, bairro, cidade, estado):
    conn = sqlite3.connect('banco/Script_BD_Vendas.db');
    conn.execute(""" INSERT INTO tb_clientes(nome, rg, cpf, email, telefone, celular, cep, endereco, numero, complemento, bairro, cidade, estado) VALUES(?, ?, ?) """,(nome, rg, cpf, email, telefone, celular, cep, endereco, numero, complemento, bairro, cidade, estado)); print('DADOS INSERIDO')
    conn.commit();
    desconectar_bd();
    SelectCliente();

def SelectCliente(lista):
    conn = sqlite3.connect('banco/Script_BD_Vendas.db');
    listaSQL = cursor.execute(""" SELECT id, nome, rg, cpf, email, telefone, celular, cep, endereco, numero, complemento, bairro, cidade, estado FROM tb_clientes ORDER BY nome ASC""")
    for i in listaSQL:
        lista.insert("",END ,  values=i)
    desconectar_bd();