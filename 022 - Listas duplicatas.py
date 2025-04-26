def remover_duplicatas(lista):
    lista_sem_duplicatas = []
    for item in lista:
        if item not in lista_sem_duplicatas:
            lista_sem_duplicatas.append(item)
    return lista_sem_duplicatas

# Exemplo de uso:
numeros = [1, 2, 2, 3, 4, 4, 5]
print(remover_duplicatas(numeros))  # [1, 2, 3, 4, 5]
