class Node:  # Node class
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:  # LinkedList class
    def __init__(self):
        self.head = None

    def append(self, data):  # Append method
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):  # Prepend method
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):  # Delete method
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next

    def display(self):  # Display method
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)) if elements else "A lista está vazia.")

# Menu interativo
if __name__ == "__main__":  # Interactive menu
    linked_list = LinkedList()

    while True:
        print("\nEscolha uma operação:")
        print("1. Adicionar ao final")
        print("2. Adicionar ao início")
        print("3. Remover um elemento")
        print("4. Exibir a lista")
        print("5. Sair")
        
        choice = input("Digite o número da operação desejada: ")

        if choice == "1":
            data = input("Digite o valor a ser adicionado ao final: ")
            linked_list.append(data)
        elif choice == "2":
            data = input("Digite o valor a ser adicionado ao início: ")
            linked_list.prepend(data)
        elif choice == "3":
            data = input("Digite o valor a ser removido: ")
            linked_list.delete(data)
        elif choice == "4":
            print("Lista encadeada:")
            linked_list.display()
        elif choice == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
