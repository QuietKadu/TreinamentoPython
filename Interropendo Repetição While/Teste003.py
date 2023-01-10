from random import randint
n = 0
print('=-' * 15)
print('Vamos Jogar Par ou Ímpar')
print('=-' * 15)
while True:
    bot = randint(0, 11)
    v = int(input('Diga um valor: '))
    soma = v + bot
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {v} e o computador {bot}. Total de {soma} deu ',  end='')
    print('Deu Par' if soma % 2 == 0 else 'Deu impar')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você venceu')
            n += 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você venceu')
            n += 1
        else:
            print('Você perdeu')
            break
    print('Vamos jogar novamente')
print('Fim')