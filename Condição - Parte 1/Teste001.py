from random import randint
from time import sleep
pc = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5 Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero pensei: '))
print('PROCESSANDO RESULTADO...')
sleep(3)
if jogador == pc:
    print('Parabens! Você conseguiu me vencer!!!')
else:
    print('Ganhei!! Eu pensei no número {} e não no {}'.format(pc, jogador))
