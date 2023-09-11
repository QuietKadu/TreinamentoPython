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
#deletar(vcon, vsql)

def atualizar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Registro atualizado")


vsql = "UPDATE tb_contatos SET T_NOMECONTATO = 'Bruno', T_TELEFONECONTATO = '(31)9999 - 9999', T_EMAILCONTATO" \
       " = 'bruno@gmail.com.br' WHERE N_IDCONTATO = 1"

#atualizar(vcon, vsql)


def consulta(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    return resultado

vsql = "SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%no'"
res = consulta(vcon, vsql)
for r in res:
    print(r)
