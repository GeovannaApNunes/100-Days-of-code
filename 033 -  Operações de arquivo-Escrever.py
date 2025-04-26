# Solicita informações ao usuário
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
profissao = input("Digite sua profissão: ")

# Abre (ou cria) um arquivo chamado "dados.txt" no modo de escrita
with open("dados.txt", "w") as arquivo:
    arquivo.write(f"Nome: {nome}\n")
    arquivo.write(f"Idade: {idade}\n")
    arquivo.write(f"Profissao: {profissao}\n")

print("Dados gravados com sucesso!")