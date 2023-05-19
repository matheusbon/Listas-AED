def find_reachable_users(num_users, source_user, boost_value, adjacency_list):
    visited = [False] * (num_users + 1)
    queue = []
    front = 0  # Variável para rastrear o índice do próximo elemento a ser removido da fila
    visited[source_user] = True
    queue.append(source_user)
    reachable_users = []
    while front < len(queue):  # Alteração: Usando a variável 'front' para controlar a fila
        user = queue[front]
        front += 1
        for follower in adjacency_list[user]:
            if not visited[follower]:
                visited[follower] = True
                queue.append(follower)
                if boost_value >= 5.25 and follower != source_user and follower not in adjacency_list[source_user]:
                    reachable_users.append(str(follower))
                    boost_value -= 5.25
    if boost_value >= 5.25:
        reachable_users.extend([str(follower) for follower in adjacency_list[source_user] if str(follower) not in reachable_users])
        boost_value -= 5.25 * len(adjacency_list[source_user])

    result = [str(follower) for follower in adjacency_list[source_user]] + reachable_users
    return result

num_users = int(input())
source_user = int(input())
boost_value = float(input())

adjacency_list = [[] for _ in range(num_users)]
for i in range(num_users):
    line = input().split(" : ")
    user_id = int(line[0])
    followers = list(map(int, line[1].split()))
    adjacency_list[user_id] = followers

reachable_users_list = find_reachable_users(num_users, source_user, boost_value, adjacency_list)
print(reachable_users_list)
