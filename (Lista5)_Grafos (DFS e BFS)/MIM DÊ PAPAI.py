def dfs(u, graph, visited):
    visited[u] = True
    count = 1
    for v in graph[u]:
        if not visited[v]:
            count += dfs(v, graph, visited)
    return count

n, m = map(int, input().split())

# Cria um grafo vazio com N vértices numerados de 1 a N
graph = {i: [] for i in range(1, n+1)}

# Lê as M conexões de amizade e adiciona ao grafo
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Percorre o grafo a partir de cada vértice e armazena os resultados
results = []
for i in range(1, n+1):
    visited = {j: False for j in range(1, n+1)}
    results.append(str(dfs(i, graph, visited)))

# Imprime os resultados separados por espaço em branco
print(" ".join(results), end="")
