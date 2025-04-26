def decorador_de_classe(cls):
    cls.saudacao = lambda self: print(f"Bem-vindo(a), {self.nome}!")
    return cls

@decorador_de_classe
class MinhaClasse:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

# Exemplo de uso com input
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
obj = MinhaClasse(nome, idade)
obj.apresentar()
obj.saudacao()
