lista = []
lista1 = []
lista2 = []
while True:
    vl = int(input('Digite um número: '))
    lista.append(vl)
    sn = str(input('Quer continuar? [S/N] '))
    if sn in 'Nn':
        break
    if vl % 2 == 0:
        lista1.append(vl)
    elif vl % 2 == 1:
        lista2.append(vl)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {lista1}')
print(f'A lista de ímpares é {lista2}')
