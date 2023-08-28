import re
import os

nome = "Teste.txt"
caminho = "C:/Python/Aulas/Aula46/"

if os.path.exists(caminho + nome):
    print("Arquivo existente")
else:
    f = open(caminho + nome, "x")
    f.close()
    print("Arquivo criado")

if os.path.exists(caminho + nome):
    os.remove(caminho + nome)
    print("Arquivo removido")
else:
    print("Arquivo inexistente")
