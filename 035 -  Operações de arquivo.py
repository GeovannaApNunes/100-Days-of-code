def calcular_media():
    try:
        numeros = input("Digite os números separados por espaço: ").strip().split()

        # Converte os valores para float
        numeros = [float(num) for num in numeros]

        if not numeros:
            raise ValueError("Nenhum número válido foi inserido.")

        media = sum(numeros) / len(numeros)

        with open("saida.txt", 'w') as file:
            file.write(f'Média: {media:.2f}\n')

        print(f"Média calculada: {media:.2f}")
        print("Resultado salvo em 'saida.txt'.")

    except ValueError as e:
        print(f"Erro: {e}")

# Executa a função
calcular_media()