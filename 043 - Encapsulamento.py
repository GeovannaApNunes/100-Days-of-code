class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def ver_saldo(self):
        print(f"Saldo atual de {self.__titular}: R${self.__saldo:.2f}")


# Exemplo de uso
if __name__ == "__main__":
    nome = input("Digite o nome do titular da conta: ")
    conta = ContaBancaria(nome)

    while True:
        print("\n1. Depositar")
        print("2. Ver Saldo")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor para depositar: "))
            conta.depositar(valor)
        elif opcao == "2":
            conta.ver_saldo()
        elif opcao == "3":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")