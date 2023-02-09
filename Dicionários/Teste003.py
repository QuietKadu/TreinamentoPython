from datetime import datetime
dici = {}
dici['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dici['idade'] = datetime.now().year - nasc
dici['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dici['ctps'] == 0:
    for k, v in dici.items():
        print(f'{k} tem o valor de {v}')
else:
    dici['contratação'] = int(input('Ano de contratação: '))
    dici['salario'] = float(input('Salário: R$'))
    dici['aposentadoria'] = dici['idade'] + ((dici['contratação'] + 35) - datetime.now().year)
print('-=' * 25)
for k, v, in dici.items():
    print(f'{k} tem o valor {v} ')
