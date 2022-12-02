pc = int(input('Digite um número inteiro: '))
bi = 1
oc = 2
he = 3
print('Escolha qual será base de conversão:')
print('Digite ( 1 ) para BINÁRIO')
print('Digite ( 2 ) para OCTAL')
print('Digite ( 3 ) para HEXADECIMAL')
user = int(input('Digite qual opção que você quer: '))
if user == 1:
    print('O {} convertido para BINÂRIO vai ser {}'.format(pc, bin(pc)[2:]))
elif user == 2:
    print('O {} convertido para OCTAL vai ser {}'.format(pc, oct(pc)[2:]))
elif user == 3:
    print('O {} convertido para HEXADECIMAL vai ser {}'.format(pc, hex(pc)[2:]))
else:
    print('Opção inválida. Tente de novo.')
