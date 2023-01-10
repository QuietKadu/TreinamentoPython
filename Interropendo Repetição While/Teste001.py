s = c = 0
while True:
    n = int(input('Digite um Número: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'foi registrado {c} números e a soma vale {s}')

