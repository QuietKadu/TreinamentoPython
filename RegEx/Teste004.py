import re #RegEx

texto = "Curso de Python do CFB Cursos, canal do Youtube"

res = re.sub("\s", "-", texto)
res = re.sub(",", ".", res)

print(res)
