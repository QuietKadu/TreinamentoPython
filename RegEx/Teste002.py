import re #RegEx

texto = "Curso de Python do CFB Cursos, canal do Youtube"

res = re.search("canal", texto)
#\AC

if res != None:
    pi = res.start()
    pf = res.end()
    tam = pf - pi
    print(res.start())
    print(res.end())
    print(tam)
else:
    print("Não encontrado")
