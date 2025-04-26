# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Filtrando números pares
pares = [num for num in numeros if num % 2 == 0]
print("Números pares:", pares)

# 2. Elevando ao quadrado cada número da lista
quadrados = [num ** 2 for num in numeros]
print("Quadrados:", quadrados)

# 3. Dobro apenas dos números ímpares
dobro_impares = [num * 2 for num in numeros if num % 2 != 0]
print("Dobro dos números ímpares:", dobro_impares)

# 4. Trabalhando com strings - Converter palavras para maiúsculas se começarem com vogal
palavras = ["apple", "banana", "orange", "umbrella", "grape"]
vogais = "aeiou"
maiusculas = [palavra.upper() for palavra in palavras if palavra[0] in vogais]
print("Palavras que começam com vogal em maiúsculas:", maiusculas)

# 5. Criando pares ordenados (x, y) onde x e y são números entre 1 e 3
pares_ordenados = [(x, y) for x in range(1, 4) for y in range(1, 4)]
print("Pares ordenados:", pares_ordenados)
