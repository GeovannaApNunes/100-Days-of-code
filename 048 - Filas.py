class Fila:
    def __init__(self):
        self.itens = []

    def enfileirar(self, item):
        self.itens.append(item)

    def desenfileirar(self):
        if not self.esta_vazia():
            return self.itens.pop(0)
        raise IndexError("A fila está vazia.")

    def esta_vazia(self):
        return len(self.itens) == 0

    def tamanho(self):
        return len(self.itens)

    def frente(self):
        if not self.esta_vazia():
            return self.itens[0]
        raise IndexError("A fila está vazia.")


# Exemplo de uso com interação do usuário
if __name__ == "__main__":
    fila = Fila()

    while True:
        print("\nMenu:")
        print("1. Enfileirar")
        print("2. Desenfileirar")
        print("3. Ver frente da fila")
        print("4. Ver tamanho da fila")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            item = input("Digite o item para enfileirar: ")
            fila.enfileirar(item)
            print(f"Item '{item}' enfileirado.")
        elif opcao == "2":
            try:
                item = fila.desenfileirar()
                print(f"Item '{item}' desenfileirado.")
            except IndexError as e:
                print(e)
        elif opcao == "3":
            try:
                print("Frente da fila:", fila.frente())
            except IndexError as e:
                print(e)
        elif opcao == "4":
            print("Tamanho da fila:", fila.tamanho())
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")