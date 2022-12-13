from datetime import date
atual = date.today().year
maior = 0
menor = 0
print('=' * 25)
print('Detector de Maioridade')
print('=' * 25)
for c in range(1, 8):
    ano = int(input('Em que ano a {} pessoa nasceu: '.format(c)))
    idade = atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Tem {} maior de idade'.format(maior))
print('Tem {} menor de idade'.format(menor))
