import re

nome = "Teste.txt"
f = open("C:/Python/Aulas/Aula46/" + nome, "rt")

res = re.sub("\s", "-", f.readline())
f.close()

f = open("C:/Users/kaduk/PycharmProjects/Estudos/" + nome, "wt")
f.write(res)
f.close()

print(res)
