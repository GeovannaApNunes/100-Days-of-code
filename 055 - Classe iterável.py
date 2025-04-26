class RangePersonalizado:
    def __init__(self, inicio, fim, passo=1):
        self.inicio = inicio
        self.fim = fim
        self.passo = passo
    
    def __iter__(self):
        self.atual = self.inicio
        return self
    
    def __next__(self):
        if (self.passo > 0 and self.atual >= self.fim) or (self.passo < 0 and self.atual <= self.fim):
            raise StopIteration
        valor = self.atual
        self.atual += self.passo
        return valor

# Exemplo de uso
teste = RangePersonalizado(1, 10, 2)
for num in teste:
    print(num)
