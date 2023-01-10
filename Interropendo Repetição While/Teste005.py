total = maxmil = bara = conta = 0
menor = ''
while True:
    prod = str(input('Nome do Produto: '))
    pre = float(input('Preço: R$'))
    conta += 1
    total += pre
    if pre > 1000:
        maxmil += 1
    if conta == 1:
        bara = pre
        menor = prod
    else:
        if pre < bara:
            bara = pre
            menor = prod
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'O total da compra foi R${total}')
print(f'Temos {maxmil} produtos custndo mais de R$1000.00')
print(f'O produto mais barato foi {menor} que custa R${bara:.2f}')
print('Fim do Programa')
