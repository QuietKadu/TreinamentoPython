casa = float(input('Por favor digite o valor da casa: R$'))
salario = float(input('Por favor digite o salario do comprador: R$'))
anos = int(input('Por favor digite quantos anos você quer financiar?: '))
v1 = casa / (anos * 12)
v2 = 0.30 * salario
print('Para pagar essa casa em {} anos a prestação será de {:.2f}'.format(anos, v1))
if v1 <= v2:
    print('O emprestimo PODE ser feito')
else:
    print('O emprestimo NÃO pode ser feito')
