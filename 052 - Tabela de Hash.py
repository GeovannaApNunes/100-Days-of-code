class TabelaHash:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def hash_func(self, chave):
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self.hash_func(chave)
        for par in self.tabela[indice]:
            if par[0] == chave:
                par[1] = valor
                return
        self.tabela[indice].append([chave, valor])

    def buscar(self, chave):
        indice = self.hash_func(chave)
        for par in self.tabela[indice]:
            if par[0] == chave:
                return par[1]
        return None  # Retorna None se a chave não existir

    def remover(self, chave):
        indice = self.hash_func(chave)
        for i, par in enumerate(self.tabela[indice]):
            if par[0] == chave:
                del self.tabela[indice][i]
                return True
        return False  # Retorna False se a chave não for encontrada

    def exibir(self):
        for i, lista in enumerate(self.tabela):
            print(f"Índice {i}: {lista}")

# Exemplo de uso:
tabela = TabelaHash(5)
tabela.inserir("nome", "Geovanna")
tabela.inserir("idade", 18)
tabela.inserir("cidade", "Minas Gerais")
tabela.exibir()

print("Buscando 'idade':", tabela.buscar("idade"))
tabela.remover("cidade")
tabela.exibir()
