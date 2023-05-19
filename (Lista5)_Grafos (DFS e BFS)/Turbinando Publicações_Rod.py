# =========== input ===============
n = int(input())  # Número de usuários na rede social
u = int(input())  # ID do usuário que fez a publicação
b = float(input())  # Valor investido em boost


# Criando a lista de adjacências
adj_list = [[] for _ in range(n)]
for _ in range(n):
    line = input().split(" : ")
    user_id = int(line[0])
    followers = list(map(int, line[1].split()))
    adj_list[user_id] = [f for f in followers]




def alcanca_usuarios(n, u, b, adj_list):
    # inicializa a lista de visitados e a fila para a busca em largura
    visitados = [False] * (n+1)
    fila = []
    # marca o usuário de origem como visitado e o adiciona na fila
    visitados[u] = True
    fila.append(u)
    # inicia a busca em largura
    usuarios_alcancados = []
    while fila:
        # retira o primeiro usuário da fila e verifica seus seguidores
        user = fila.pop(0)
        for seguidor in adj_list[user]:
            # se o seguidor ainda não foi visitado, marca como visitado e adiciona na fila
            if not visitados[seguidor]:
                visitados[seguidor] = True
                fila.append(seguidor)
                # se ainda há dinheiro disponível para investir e o seguidor não é seguidor direto do usuário de origem
                # adiciona o seguidor na lista de alcançados
                if b >= 5.25 and seguidor != u and seguidor not in adj_list[u]:
                    usuarios_alcancados.append(str(seguidor))
                    b -= 5.25
    # se a fila acabou e ainda há dinheiro disponível, adiciona os seguidores diretos do usuário de origem
    if b >= 5.25:
        usuarios_alcancados.extend(adj_list[u])
        b -= 5.25 * len(adj_list[u])
    
    # return adj_list[u] + usuarios_alcancados
    # junta a lista de seguidores diretos com a lista de seguidores alcançados pelo boost
    resultado = list(map(str, adj_list[u])) + usuarios_alcancados
    return resultado




list_seguis = alcanca_usuarios(n, u, b, adj_list)
print(list_seguis)