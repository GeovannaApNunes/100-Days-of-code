from collections import deque

def bfs(grafo, inicio):
    visitados = set()           # Conjunto para rastrear os nós visitados
    fila = deque([inicio])      # Fila para controlar a ordem de visita
    ordem_visita = []           # Lista para armazenar a ordem de visita

    while fila:
        no_atual = fila.popleft()  # Remove o primeiro elemento da fila

        if no_atual not in visitados:
            visitados.add(no_atual)
            ordem_visita.append(no_atual)
            fila.extend(grafo[no_atual])  # Adiciona os vizinhos à fila

    return ordem_visita

# Exemplo de uso:
grafo_exemplo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

resultado = bfs(grafo_exemplo, 'A')
print("Ordem de visita (BFS):", resultado)
