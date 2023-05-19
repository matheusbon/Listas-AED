def backtrack(n, temp, res):
    if n == 0:
        res.append(temp[:])
    else:
        for i in range(1, n+1):
            if not temp or i >= temp[-1]:
                temp.append(i)
                backtrack(n-i, temp, res)
                temp.pop()

def print_partitions(n):
    res = []
    backtrack(n, [], res)
    for partition in res:
        print(partition)

pessoas = int(input())

print(f'Uma sessão com {pessoas} pessoas pode ter sua audiência nos seguintes subgrupos:')
print_partitions(pessoas)