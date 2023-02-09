dici = {}
lista = []
dici["nome"] = str(input('Nome do Jogador: '))
vl = int(input(f'Quantas partidas {dici["nome"]} jogou? '))
for g in range(vl):
    lista.append(int(input(f'Quantos gols na partida {g} ')))
    dici["gols"] = lista[:]
    dici["total"] = sum(lista)
print('-=' * 25)
for k, v in dici.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 25)
print(f'O jogador {dici["nome"]} jogou {vl} partidas.')
for v, g in enumerate(dici["gols"]):
    print(f'=> Na partida {v}, fez {g} ')
print(f'foi um total de {dici["total"]} gols')
