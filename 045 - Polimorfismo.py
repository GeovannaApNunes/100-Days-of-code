from math import pi   # Importa a constante pi do módulo math

class Forma:
    def calcular_area(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.") # Levanta uma exceção caso o método não seja implementado

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura # Calcula a área do retângulo

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio    # Inicializa o raio do círculo

    def calcular_area(self):
        return pi * (self.raio ** 2)  # Calcula a área do círculo

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura  # Inicializa a base e a altura do triângulo

    def calcular_area(self):
        return (self.base * self.altura) / 2  # Calcula a área do triângulo

# Exemplo de uso
formas = [  # Cria uma lista de formas
    Retangulo(5, 10),
    Circulo(7),
    Triangulo(6, 8)   
]

for forma in formas:
    print(f"A área da {forma.__class__.__name__} é: {forma.calcular_area():.2f}")  # Exibe a área de cada forma com duas casas decimais