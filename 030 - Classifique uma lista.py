numeros = input(f"Digite os números separados por espaço: ").split()
numeros = [int(numero) for numero in numeros]
numeros_ordenados = sorted(numeros)

print(numeros_ordenados)