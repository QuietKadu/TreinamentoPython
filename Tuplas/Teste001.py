nu = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', \
     'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',\
     'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',\
     'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',\
     'Dezenove', 'Vinte'
while True:
    dig = int(input('Digite um número entre 0 e 20: '))
    if 0 <= dig <= 20:
        break
    print('Tente novamente. Digite um número entre 0 e 20:')
print(f'Você digitou o número {nu[dig]}')
