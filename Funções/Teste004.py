from random import randint

def sorteia(lista):
    print(f'Sorteando 5 valores da lista: {numeros} Pronto!')
    for c in range(0, 5):
        lista.append(randint(1, 10))


def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {numeros}, temos {soma}')


numeros = []
sorteia(numeros)
somapar(numeros)
