pe = float(input('Qual é seu peso?: '))
al = float(input('Qual é sua altura?: '))
imc = pe / (al ** 2)
if imc < 18.5:
    print('Abaixo do Peso')
elif 18.5 <= imc < 25:
    print('Peso Ideal')
elif 25 >= imc < 30:
    print('Sobrepeso')
elif 30 >= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade mórbida')
