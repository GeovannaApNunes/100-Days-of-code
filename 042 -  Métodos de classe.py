class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        # Inicializa a conta bancária com o titular e saldo inicial
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        # Deposita um valor na conta, se for positivo
        if valor > 0:
            self.saldo = round(self.saldo + valor, 2)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def retirar(self, valor):
        # Retira um valor da conta, se for positivo e menor ou igual ao saldo
        if 0 < valor <= self.saldo:
            self.saldo = round(self.saldo - valor, 2)
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        elif valor > self.saldo:
            print("Saldo insuficiente para a operação.")
        else:
            print("O valor do saque deve ser positivo.")

    def exibir_saldo(self):
        # Exibe o saldo atual da conta
        print(f"Saldo atual de {self.titular}: R$ {self.saldo:.2f}")


def obter_valor_float(mensagem):
    while True:
        try:
            return float(input(mensagem).strip())
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")


# Criando a conta com input do usuário
nome = input("Digite o nome do titular da conta: ").strip()
saldo_inicial = obter_valor_float("Digite o saldo inicial: ")

conta = ContaBancaria(nome, saldo_inicial)

# Menu interativo
while True:
    print("\n1. Depositar\n2. Retirar\n3. Exibir Saldo\n4. Sair")
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        valor = obter_valor_float("Digite o valor do depósito: ")
        conta.depositar(valor)
    elif opcao == "2":
        valor = obter_valor_float("Digite o valor do saque: ")
        conta.retirar(valor)
    elif opcao == "3":
        conta.exibir_saldo()
    elif opcao == "4":
        print("Operação finalizada.")
        break
    else:
        print("Opção inválida! Escolha novamente.")