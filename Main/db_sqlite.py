import sqlite3

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
                                 " ,estado TEXT )")
    
    print('Conexão com Bando de dados--> SUCESSO ');
    conn.commit();

def NovoCliente(nome,rg,cpf):
    conn = sqlite3.connect('banco/Script_BD_Vendas.db');
    conn.execute(""" INSERT INTO tb_clientes(nome,rg,cpf) VALUES(?, ?, ?) """,(nome,rg,cpf)); print('DADOS INSERIDO')
    conn.commit();
    desconectar_bd();