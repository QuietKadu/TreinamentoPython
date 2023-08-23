import re #RegEx

texto = "Curso de Python do CFB Cursos, canal do Youtube"

pesq = input("Pesquisar: ")

res = re.findall(pesq, texto)

qtde = len(res)
print(res)

print("Qtde: " + str(qtde))

for t in res:
    print(t)