n1 = float(input('Sua nota em Portugues: '))
n2 = float(input('Sua nota em Matematica: '))
media = (n1 + n2) / 2
print('Sua média foi {}'.format(media))
if media < 5.0:
    print('REPROVADO')
elif 6.9 > media >= 5.0:
    print('RECUPERAÇÃO')
elif media >= 7.0:
    print('APROVADO')
