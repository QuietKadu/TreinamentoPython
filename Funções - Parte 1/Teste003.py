def contador(inicio, fim, passo):
    print('-=' * 20)
    print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}')

    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            cont += passo
        print('Fim')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            cont -= passo
        print('Fim')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem')
ini = int(input('Início: '))
fim = int(input('Fim     '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)


