maior = 0
menor = 0
for c in range(1, 5):
    peso = float(input('Digite o {} peso: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}Kg'.format(maior))
print('O menor peso é {}Kg'.format(menor))
