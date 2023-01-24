lista = []
for li in range(0, 6):
    lista.append(int(input(f'Digite um valor para posição {li}: ')))
print(f'Você digitou os valores {lista}')
print(f'o maior valor foi {max(lista)} e foi encontrado na posição {lista.index(max(lista))}')
print(f'O menor valor foi {min(lista)} e foi encontrado na posição {lista.index(min(lista))}')
