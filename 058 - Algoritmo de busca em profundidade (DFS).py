# Função para realizar a busca em profundidade (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
        
    # Marca o nó como visitado
    visited.add(start)
    
    # Imprime o nó
    print(start)
    
    # Recursivamente visita todos os vizinhos não visitados
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

# Representação do grafo usando um dicionário de adjacência
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Chamada da função DFS a partir do nó 'A'
visited_nodes = dfs(graph, 'A')
