c = 0
while True:
    t = int(input('Digite um Número: '))
    if t < 0:
        break
    print('=' * 30)
    for c in range(1, 11):
        print(f'{t} x {c} = {t*c}')
    print('=' * 30)
print('Fim')