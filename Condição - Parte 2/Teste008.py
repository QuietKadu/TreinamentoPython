print('=' * 10, 'LOJA GAMER', '=' * 10)
preco = int(input('Preço das compras: R$ '))
print('Formas de Pagamento')
print('( 1 ) à vista dinheiro/cheque')
print('( 2 ) à vista cartão')
print('( 3 ) 2x no cartão')
print('( 4 ) 3x ou mais no cartão')
opc = int(input('Qual é a opção? '))
if opc == 1:
    total = preco - (preco * 10 / 100)
elif opc == 2:
    total = preco - (preco * 5 / 100)
elif opc == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} Sem juros'.format(parcela))
elif opc == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela= total / totalparc
    print('Sua compra de R${} vai custar R${:.2f} COM JUROS'.format(preco, parcela))
else:
    print('OPÇÃO INVALIDA. TENTE NOVAMENTE.')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
