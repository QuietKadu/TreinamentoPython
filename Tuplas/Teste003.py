tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o ultimo número: ')))
print(f'Voce digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} Vez/Vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu  vezes {tupla.index(3)+1} posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ', end='')
for t in tupla:
    if t % 2 == 0:
        print(t, end=' ')
