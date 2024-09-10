nome = input("Digite seu nome: ")
nota = float(input("Insira sua primeira nota: "))
nota2 = float(input("Insira sua segunda nota: "))
nota3 = float(input("Insira sua terceira nota: "))
soma = nota + nota2 + nota3
if soma / 3 >= 7:
    print(f"{nome} você passou")
elif soma / 3 >= 5 and nota / 3 <= 6:
    print(f"{nome} você está de recuperação")
else:
    print(f"{nome} você está reprovado")
