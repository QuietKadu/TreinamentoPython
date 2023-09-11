import sqlite3
from sqlite3 import Error

########## Criar Conexão


def ConexaoBanco():
    caminho = "C:\\Users\\kaduk\\PycharmProjects\\Estudos\\Banco\\agenda"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con


vcon = ConexaoBanco()

#inserir


def inserir(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()

        print("Registro inserido")
    except Error as ex:
        print(ex)




#nome = input("Digite o nome: ")
#telefone = input("Digite o telefone: ")
#email = input("Digite o email: ")
#vsql = "INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO)VALUES('" + nome + "', '"\
       #+ telefone + "', '" + email + "')"
#inserir(vcon, vsql)


#deletar


def deletar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Registro removido")


vsql = "DELETE FROM tb_contatos WHERE N_IDCONTATO = 3"
deletar(vcon, vsql)

