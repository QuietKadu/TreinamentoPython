import re #RegEx

texto = "Curso de Python do CFB Cursos, canal do Youtube"

res = re.split("\s", texto)

print(res)
print(res[2])
for t in res:
    print(t)