import math

# Classe base
class Forma:
    def area(self):
        raise NotImplementedError("Subclasses devem implementar o método area()")

# Subclasse Círculo
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio ** 2

# Subclasse Quadrado
class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

# Subclasse Triângulo
class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

# Menu para escolher a forma
print("Escolha uma forma para calcular a área:")
print("1 - Círculo")
print("2 - Quadrado")
print("3 - Triângulo")
opcao = input("Digite o número da opção desejada: ")

if opcao == "1":
    raio = float(input("Digite o raio do círculo: "))
    forma = Circulo(raio)
elif opcao == "2":
    lado = float(input("Digite o lado do quadrado: "))
    forma = Quadrado(lado)
elif opcao == "3":
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    forma = Triangulo(base, altura)
else:
    print("Opção inválida.")
    forma = None

if forma:
    print(f"A área do {forma.__class__.__name__} é {forma.area():.2f}")