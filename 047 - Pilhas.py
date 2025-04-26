class Pilha:    # Implementação de uma pilha
    def __init__(self):
        self.itens = []

    def empilhar(self, item):  # Adiciona um item à pilha
        self.itens.append(item)

    def desempilhar(self):  # Remove e retorna o item no topo da pilha
        if not self.esta_vazia():
            return self.itens.pop()
        raise IndexError("A pilha está vazia")

    def topo(self):             # Retorna o item no topo da pilha
        if not self.esta_vazia():
            return self.itens[-1]
        raise IndexError("A pilha está vazia")

    def esta_vazia(self):     # Verifica se a pilha está vazia
        return len(self.itens) == 0

    def tamanho(self):      # Retorna o número de itens na
        return len(self.itens)

# Exemplo de uso
if __name__ == "__main__":  # Executa o código somente se este arquivo for o principal
    pilha = Pilha()
    while True:
        print("\nMenu:")
        print("1. Empilhar")
        print("2. Desempilhar")
        print("3. Ver topo")
        print("4. Ver tamanho")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            item = input("Digite o item para empilhar: ")
            pilha.empilhar(item)
            print(f"Item '{item}' empilhado.")
        elif opcao == "2":
            try:
                print(f"Item desempilhado: {pilha.desempilhar()}")
            except IndexError as e:
                print(e)
        elif opcao == "3":
            try:
                print(f"Topo da pilha: {pilha.topo()}")
            except IndexError as e:
                print(e)
        elif opcao == "4":
            print(f"Tamanho da pilha: {pilha.tamanho()}")
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")