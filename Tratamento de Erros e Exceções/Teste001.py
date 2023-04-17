def leiaint(msg):
    while True:
        try:
            vli = int(input('Digite um Inteiro: '))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um Número Inteiro Válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return vli


def leiafloat(msg):
    while True:
        try:
            vlf = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número real valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return vlf


num = leiaint('Digite um valor Inteiro: ')
num2 = leiafloat('Digite um valor Real:')
print(f'O valor Inteiro digitado foi {num} e o valor Real foi {num2}')
