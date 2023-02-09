dici = {}
lista = []
soma = media = 0
while True:
    dici.clear()
    dici["nome"] = str(input('Nome: '))
    while True:
        dici["sexo"] = str(input('Sexo: [M/F] ')).upper()[0]
        if dici["sexo"] in 'MF':
            break
        print('Erro por favor, digite apenas M ou F.')
        dici["idade"] = int(input('Idade: '))
        soma += dici["idade"]
        lista.append(dici.copy())
    while True:
        sn = str(input('Quer continuar? [S/N] ')).upper()[0]
        if sn in 'SN':
            break
        print('Erro responda apenas S ou N.')
    if sn == 'N':
        break
print('-=' * 25)
print(f'O grupo tem {len(lista)} pessoas')
media = soma / len(lista)
print(f'A média de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('Lista de pessoa acima da média')
for p in lista:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('Acabou')
