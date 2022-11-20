from math import sin, cos, tan, radians
n1 = float(input('Digite o angulo que voce deseja '))
n2 = sin(radians(n1))
n3 = cos(radians(n1))
n4 = tan(radians(n1))
print('O valor em Seno vai ser {:.2f}'.format(n2))
print('O valor em Cosseno vai ser {:.2f}'.format(n3))
print('O valor em Tangente vai ser {:.2f}'.format(n4))
