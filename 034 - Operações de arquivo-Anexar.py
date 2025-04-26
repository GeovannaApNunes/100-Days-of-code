# Solicita informações ao usuário
novo_dado = input("Digite a informação que deseja adicionar ao arquivo: ")

# Abre o arquivo "dados.txt" no modo de adição ("a")
with open("dados.txt", "a") as arquivo:
    arquivo.write(f"{novo_dado}\n")

print("Dados adicionados com sucesso!")