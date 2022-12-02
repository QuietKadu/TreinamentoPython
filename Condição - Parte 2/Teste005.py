from datetime import date
print('=' * 15)
print('Confederação Nacional de Natação')
print('=' * 15)
atual = date.today().year
ano = int(input('Em que ano você nasceu: '))
idade = atual - ano
print('Você tem {} anos então você está na categoria:'.format(idade))
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Sênior')
else:
    print('Master')
