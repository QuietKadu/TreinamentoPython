Mochila = ["Armadura", "Espada", "Escudo", "Poções", "Manopolas", "Botas", "Besta", "Comidas", "Bandagem", "Mapas"]
print(Mochila[1])
print(Mochila[5]) # irá mostrar os respectivos termos na tela
print(Mochila[9])
item = input(print("Digite mais um item para essa lista: "))
Mochila.append(item) # Irá pedir para o usuario digitar um item e ira adicionar na lista
print(Mochila)