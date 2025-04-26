def intersecao(lista1, lista2):
    return list(set(lista1) & set(lista2))

# Entrada do usuário
lista_a = list(map(int, input("Digite os elementos da primeira lista separados por espaço: ").split()))
lista_b = list(map(int, input("Digite os elementos da segunda lista separados por espaço: ").split()))

# Calculando a intersecção
resultado = intersecao(lista_a, lista_b)

# Exibindo o resultado
print("Interseção das listas:", resultado)