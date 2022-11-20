n1 = str(input('Escreva uma frase ')).upper().strip()
print('A letra "A" aparece {} vezes'.format(n1.count('A')))
print('Ela aparece pela primeira vez no {} Caractere'.format(n1.find('A')))
print('Ela aparece pela ultima vez no {} Caractere'.format(n1.rfind('A')))
