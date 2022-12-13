pri = int(input('Primeiro termo: '))
raz = int(input('Razao: '))
dec = pri + (10 - 1) * raz
for c in range(pri, dec + raz, raz):
    print(c, end=' -> ')
print('Fim')
