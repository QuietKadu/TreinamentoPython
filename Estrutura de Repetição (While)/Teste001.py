from time import sleep
v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
opc = 0
while opc != 5:
    print('Oque você que fazer com eles:')
    print('( 1 ) Somar')
    print('( 2 ) Multiplicar')
    print('( 3 ) Maior')
    print('( 4 ) Novos Números')
    print('( 5 ) Sair do Programa')
    opc = int(input('Digite sua Escolha: '))
    if opc == 1:
        print('A somatoria desses numeros é {}'.format(v1 + v2))
    elif opc == 2:
        print('A multiplicação desses números é {}'.format(v1 * v2))
    elif opc == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('O maior valor é {}'.format(maior))
    elif opc == 4:
        print('Coloque os numeros novamente:')
        v1 = int(input('Digite um valor: '))
        v2 = int(input('Digite outro valor: '))
    elif opc == 5:
        print('Finalizando programa...')
        sleep(3)
        print('Programa finalizado com sucesso!!')
    else:
        print('Algo deu errado. Tente de Novo')
    print('=' * 20)
    sleep(2)
print('Fim do Programa')
