import json

#{
#   "nome": "Bruno",
#   "time": "aviadores",
#   "energia":100,
#   "mochila": ["perdeneira", "corda", "linha", "arame"],
#   "aeronaves":[
#       {"tipo":"transporte", "habilidade":80},
#       {"tipo":"ataque", "habilidade":100}
#       {"tipo":"reconhecimento", "habilidade":50}
#
#   ]
#}

jogador_j='{"nome": "Bruno","time": "aviadores","vivo": "True","energia": 100,"mochila": ["pederneira", "corda", "linha", "arame"],"aeronaves": [{"tipo": "transporte", "habilidade": 80},{"tipo": "ataque", "habilidade": 100},{"tipo": "reconhecimento", "habilidade": 50}]}'

jogador = json.loads(jogador_j)

#chaves
for c in jogador:
    print(c)

#itens
for i in jogador.items():
    print(i)

#valores
for v in jogador.values():
    print(v)

#nome do jogador
print(jogador["time"])

#itens da mochila
for im in jogador["mochila"]:
    print(im)

#aeronaves
for a in jogador["aeronaves"]:
    print(a["tipo"] + " - " + str(a["habilidade"]))
