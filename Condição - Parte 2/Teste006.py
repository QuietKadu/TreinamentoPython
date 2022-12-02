print('-=-' * 15)
print('Analisador De Triângulos')
print('-=-' * 15)
seg1 = float(input('Coloque o Primeiro segmento: '))
seg2 = float(input('Agora coloque o segundo: '))
seg3 = float(input('E agora o terceiro: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos digitados podem formar um triângulo', end=' ')
    if seg1 == seg2 == seg3:
        print('Equilátero')
    elif seg1 != seg2 != seg3 != seg1:
        print('Escaleno')
    else:
        print('Isóceles')
else:
    print('Os segmentos digitados não podem formar um triângulo')
