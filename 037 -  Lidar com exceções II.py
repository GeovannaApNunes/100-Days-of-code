try:
    # Tente abrir o arquivo em modo de leitura
    with open('arquivo.txt', 'r') as file:
        conteúdo = file.read()
        print(conteúdo)
except FileNotFoundError:
    # Se o arquivo não for encontrado, exibe uma mensagem de erro
    print("Erro: O arquivo não foi encontrado.")