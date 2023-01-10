max18 = maxm = maxf20 = 0
while True:
    print('=' * 25)
    print('CADASTRE UMA PESSOA')
    print('=' * 25)
    ida = int(input('Idade: '))
    se = ' '
    cont = ' '
    while se not in 'MF':
        se = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if ida >= 18:
        max18 += 1
    if se == 'M':
        maxm += 1
    if se == 'F' and ida < 20:
        maxf20 += 1
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
    print('=' * 25)
print(f'Total de pessoa com mais de 18 anos: {max18}')
print(f'Ao todo temos {maxm} homens cadastrado')
print(f'Tem {maxf20} mulher/mulheres com menos de 20 anos')
print('Fim')
