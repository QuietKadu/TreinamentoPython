class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    def buzinar(self):
        print("Buzina")
    
    def parar(self):
        print("Parando a bicicleta")
        
    def correr(self):
        print("Correndo")
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
        
b1 = Bicicleta("preta", "coloi", 2007, 5675)
print(b1)
b1.buzinar()
b1.parar()
b1.correr()