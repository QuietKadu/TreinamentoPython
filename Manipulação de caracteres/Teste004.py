n1 = str(input('Qual é seu nome? ')).strip()
n2 = n1.split()
print('''Seu primeiro nome é {}
e seu ultimo nome é {}'''.format(n2[0], n2[len(n2)-1]))
