def max_independent_set(num_setores, lista):
    if num_setores == 0:
        return 0
    if num_setores == 1:
        return lista[0]
    mis = [0] * num_setores
    mis[0] = lista[0]
    mis[1] = max(lista[0], lista[1])
    for i in range(2, num_setores):
        mis[i] = max(mis[i-1], mis[i-2] + lista[i])
    return mis[-1]

num_setores = int(input())
lista = input().split(' ')
lista = list(map(int, lista))

num_torcedores = max_independent_set(num_setores, lista)

print (f'{num_torcedores} torcedores podem ser fotografados.')