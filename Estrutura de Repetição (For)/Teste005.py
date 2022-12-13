soma = 0
media = 0
idadehomem = 0
nomevelho = 0
totmulher = 0
for c in range(1, 4 + 1):
    print('===== {} Pessoa ====='.format(c))
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: '))
    soma += idade
    if c == 1 and sexo in 'Mm':
        idadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > idadehomem:
        idadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
media = soma / 4
print('A media de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(idadehomem, nomevelho))
print('E tem {} mulher/mulheres de 20 anos'.format(totmulher))
