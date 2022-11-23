car = float(input('Em qual velocidade você estava com o carro? '))
val = (car-80) * 7
if car > 80:
    print('Multado!! Você ultrapassou o limite de velocidade permitida que é de 80Km/h')
    print('O valor da multa que você devera pagar é {:.2f}'.format(val))
print('Dirija com cuidado tenha um bom dia!')
