def busca_binaria(arr, alvo):
    inicio = 0
    fim = len(arr) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2  # encontra o meio da lista
        if arr[meio] == alvo:  # se o meio for o alvo
            return meio
        elif arr[meio] < alvo:  # se o alvo for maior que o valor do meio
            inicio = meio + 1
        else:  # se o alvo for menor que o valor do meio
            fim = meio - 1
    
    return -1  # retorna -1 se o alvo não for encontrado
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
alvo = 7
resultado = busca_binaria(arr, alvo)
if resultado != -1:
    print(f"O alvo {alvo} foi encontrado na posição {resultado}.")
else:
    print(f"O alvo {alvo} não foi encontrado na lista.")
# O algoritmo de busca binária é um algoritmo eficiente para encontrar um elemento em uma lista ordenada.