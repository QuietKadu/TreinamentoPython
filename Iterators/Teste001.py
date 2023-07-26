carros = ["HRV", "Polo", "Jetta", "Cruze", "Fusion", "Focus", "Onyx", "Fit"]
itCarros = iter(carros)


while itCarros:
    try:
        print(next(itCarros))
    except StopIteration:
        print("Fim da lista")
        break



