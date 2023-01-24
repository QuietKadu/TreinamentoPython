lista = []
for l in range(0, 6):
    vl = int(input(f'Digite o valor {l}: '))
    if l == 0 or vl > lista[-1]:
        lista.append(vl)
    else:
        pos = 0
        while pos < len(lista):
            if vl <= lista[pos]:
                lista.insert(pos, vl)
                break
            pos += 1
lista.sort()
print(lista)
