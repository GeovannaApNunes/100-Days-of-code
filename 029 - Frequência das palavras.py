# Inicializa um dicionário vazio para armazenar as frequências
frequencia_palavras = {}

while True:
    texto = input("Digite um texto (ou 'sair' para encerrar): ").strip().lower()
    
    if texto == "sair":
        break  # Sai do loop se o usuário digitar "sair"

    palavras = texto.split()  # Divide o texto em palavras
    
    for palavra in palavras:
        if palavra in frequencia_palavras:
            frequencia_palavras[palavra] += 1  # Se a palavra já existe, incrementa
        else:
            frequencia_palavras[palavra] = 1  # Se for nova, adiciona com valor 1
    
    print("\nFrequência atualizada das palavras:")
    for palavra, freq in frequencia_palavras.items():
        print(f"{palavra}: {freq}")  # Exibe palavra e frequência
    print("-" * 40)