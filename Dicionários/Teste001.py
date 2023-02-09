dicio = {}
dicio['Nome'] = str(input('Nome: '))
dicio["Média"] = float(input(f'Média de {dicio["Nome"]}: '))
for k, v in dicio.items():
    print(f'{k} é igual a {v} ')
if dicio["Média"] >= 7:
    print('Situação é igual a Aprovado')
else:
    print('Situação é igual a Reprovado')
