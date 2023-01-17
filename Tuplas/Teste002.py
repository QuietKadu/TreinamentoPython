from random import randint
tupla = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print(f'Os valores sorteados foram: ', end='')
for t in tupla:
    print(f'{t} ', end='')
print(f'\nO maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')
