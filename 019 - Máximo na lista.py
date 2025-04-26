def encontrar_maximo(lista):
    if not lista:
        return None  # Retorna None se a lista estiver vazia
    maximo = lista[0]
    for elemento in lista:
        if elemento > maximo:
            maximo = elemento
    return maximo

# Entrada do usuário
entrada = input("Digite os números separados por espaço: ") #Digite os números separados por espaço: 3 7 2 9 5
numeros = list(map(int, entrada.split()))  # Converte a entrada em uma lista de inteiros

# Exibe o maior número
print("O maior número é:", encontrar_maximo(numeros))