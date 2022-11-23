val = int(input('Digite o primeiro número: '))
val2 = int(input('Digite o segundo número: '))
val3 = int(input('Digite i terceiro número '))
if val < val2 and val < val3:
    men = val
if val2 < val3 and val2 < val:
    men = val2
if val3 < val and val3 < val2:
    men = val3
if val > val2 and val > val3:
    mai = val
if val2 > val3 and val2 > val:
    mai = val2
if val3 > val and val3 > val2:
    mai = val3
print('O maior valor foi {}'.format(mai))
print('O menor valor foi {}'.format(men))
