print('=' * 20)
print('Detector de Fatorial')
print('=' * 20)
v1 = int(input('Digite um número: '))
c = v1
f = 1
print('Calculando {}! = '.format(v1), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
