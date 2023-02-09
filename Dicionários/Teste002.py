from random import randint
from operator import itemgetter
dici = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
lista = []
print('Valores soreteados: ')
for j, d in dici.items():
    print(f'O {j} tirou {d}')
lista = sorted(dici.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores')
for n, k in enumerate(lista):
    print(f'{n+1} lugar: {k[0]} com {k[1]}')



