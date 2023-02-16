def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m.')


print(' Controle de Terrenos ')
print('-' * 20)
la = float(input('Largura (m): '))
co = float(input('Comprimento (m): '))
area(la, co)
