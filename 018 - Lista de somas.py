def soma_lista():
    numeros = input("Digite os números separados por espaço: ").split()
    numeros = [float(num) for num in numeros]  # Converte os valores para números
    return sum(numeros)

# Exemplo de uso:
resultado = soma_lista()
print("Soma dos números:", resultado)