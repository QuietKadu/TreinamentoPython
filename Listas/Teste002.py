lista = []
while True:
    vl = int(input('Digite um valor: '))
    if vl not in lista:
        lista.append(vl)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    sn = str(input('Quer continuar? [S/N] '))
    if sn in 'Nn':
        break
lista.sort()
print(f'Você digitou os valores {lista}')
