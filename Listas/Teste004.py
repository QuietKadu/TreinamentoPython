lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    sn = str(input('Quer continuar? [S/N] '))
    if sn in 'Nn':
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números')
print(f'Os valores em ordem decrescete são {lista}')
if 5 not in lista:
    print('Não foi encontrado nenhum número 5')
else:
    print('O valor 5 foi encontrado')
