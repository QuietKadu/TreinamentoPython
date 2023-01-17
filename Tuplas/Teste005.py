tupla = 'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', \
        'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', \
        'MERCADO', 'PROGRAMADOR', 'FUTURO'
for t in tupla:
    print(f'\nNa palavra {t} temos ', end='')
    for vogal in t:
        if vogal in 'AEIOU':
            print(vogal, end=' ')
