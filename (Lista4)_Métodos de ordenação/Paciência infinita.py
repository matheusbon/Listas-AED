def bubble_sort(lista, parada = None):
    n = len(lista)
    trocas = 0  # variável que armazena o número de trocas realizadas
    comparacoes = 0  # variável que armazena o número de comparações realizadas
    
    # Percorre toda a lista
    for i in range(n):
        
        # A cada iteração, o maior elemento será movido para o final
        for j in range(0, n-i-1):
            
            # Incrementa a variável de comparações a cada vez que duas posições são comparadas
            comparacoes += 1
            if parada != None:
                if comparacoes + trocas == menos_acoes:
                    return comparacoes, trocas, lista #Tanto aqui como em todas as outras condições de parada foi trocado o break por return (para retornar o os valores que as variáveis chegaram até esse ponto)
            # Se o elemento atual for maior que o próximo, troca eles de lugar
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocas += 1  # incrementa a variável de trocas
                if parada != None:
                    if comparacoes + trocas == menos_acoes:
                        return comparacoes, trocas, lista
    
    return comparacoes, trocas, lista


def selection_sort(lista, parada = None):
    n = len(lista)
    trocas = 0  # variável que armazena o número de trocas realizadas
    comparacoes = 0  # variável que armazena o número de comparações realizadas
    
    # Percorre toda a lista
    for i in range(n):
        
        # Encontra o índice do menor elemento não ordenado
        min_index = i
        for j in range(i+1, n):
            
            # Incrementa a variável de comparações a cada vez que duas posições são comparadas
            comparacoes += 1
            if parada != None:
                if comparacoes + trocas == menos_acoes:
                    return comparacoes, trocas, lista
            
            if lista[j] < lista[min_index]:
                min_index = j
        
        # Verifica se o menor elemento não ordenado está em sua posição correta
        if min_index != i:
            # Troca o menor elemento não ordenado com o primeiro elemento não ordenado
            lista[i], lista[min_index] = lista[min_index], lista[i]
            trocas += 1  # incrementa a variável de trocas
            if parada != None:
                if comparacoes + trocas == menos_acoes:
                    return comparacoes, trocas, lista
    
    return comparacoes, trocas, lista


def insertion_sort(lista, parada = None): #Principais mudanças foram feitas aqui, para conseguir ajustar a contagem das trocas e comparações
    n = len(lista)
    trocas = 0  # variável que armazena o número de trocas realizadas
    comparacoes = 0  # variável que armazena o número de comparações realizadas
    
    for i in range(1, n):
        chave = lista[i]
        
        # Move todos os elementos maiores que chave para uma posição à frente
        j = i - 1
        while j >= 0 and lista[j] > chave:
            comparacoes += 1
            if parada != None:
                if comparacoes + trocas == menos_acoes:
                    return comparacoes, trocas, lista
            
            trocas += 1
            lista[j+1] = lista[j]
            j = j - 1
            if parada != None:
                if comparacoes + trocas == menos_acoes:
                    return comparacoes, trocas, lista
        if j>= 0:
            comparacoes += 1        
        
        lista[j+1] = chave
        if parada != None:
                if comparacoes + trocas == menos_acoes:
                    return comparacoes, trocas, lista
    
    return comparacoes, trocas, lista


def shell_sort(lista, parada = None):
    n = len(lista)
    gap = n // 2
    comparacoes = 0
    trocas = 0
    while gap > 0:
        for i in range(gap, n):
            temp = lista[i]
            j = i
            
            while j >= gap and lista[j - gap] > temp:
                trocas += 1
                if parada != None:
                    if comparacoes + trocas == menos_acoes:
                        return comparacoes, trocas, lista
                
                comparacoes += 1
                if parada != None:
                    if comparacoes + trocas == menos_acoes:
                        return comparacoes, trocas, lista
                lista[j] = lista[j - gap]
                j -= gap
            
            lista[j] = temp
            if j >= gap:
                comparacoes += 1
                if parada != None:
                    if comparacoes + trocas == menos_acoes:
                        return comparacoes, trocas, lista

        gap = gap // 2
        
    return comparacoes, trocas, lista


def quicksort(A, lo, hi, comparacoes=None, trocas=None):
    if comparacoes is None:
        comparacoes = [0]  # usando uma lista para passar o valor por referência
    if trocas is None:
        trocas = [0]
    if lo >= 0 and hi >= 0 and lo < hi:
        p = partition(A, lo, hi, comparacoes, trocas)
        quicksort(A, lo, p, comparacoes, trocas)
        quicksort(A, p + 1, hi, comparacoes, trocas)
    return comparacoes[0], trocas[0], A

def partition(A, lo, hi, comparacoes, trocas):
    pivot = A[(hi + lo) // 2]
    i = lo
    j = hi
    while True:
        if i >= j:
            return j
        while A[i] < pivot:
            comparacoes[0] += 1
            i += 1
        while A[j] > pivot:
            comparacoes[0] += 1
            j -= 1
        trocas[0] += 1
        A[i], A[j] = A[j], A[i]

entrada = input()
lista = [int(num) for num in entrada.split()]

lista1 = lista[:]
lista2 = lista[:]
lista3 = lista[:]
lista4 = lista[:]
lista5 = lista[:]
lista1_2 = lista[:]
lista2_2 = lista[:]
lista3_2 = lista[:]
lista4_2 = lista[:]
lista5_2 = lista[:]

n = len(lista5) - 1

comparacoes1, trocas1, sorted_lista = bubble_sort(lista1)
comparacoes2, trocas2, sorted_lista = selection_sort(lista2)
comparacoes3, trocas3, sorted_lista = insertion_sort(lista3)
comparacoes4, trocas4, sorted_lista = shell_sort(lista4)
comparacoes5, trocas5, sorted_lista = quicksort(lista5, 0, n)

acoes1 = comparacoes1 + trocas1
acoes2 = comparacoes2 + trocas2
acoes3 = comparacoes3 + trocas3
acoes4 = comparacoes4 + trocas4
acoes5 = comparacoes5 + trocas5
acoes_geral = []
acoes_geral.append(acoes1)
acoes_geral.append(acoes2)
acoes_geral.append(acoes3)
acoes_geral.append(acoes4)
acoes_geral.append(acoes5)

print(f'Caça-Rato ordena a lista com {comparacoes1} comparações e {trocas1} trocas.')
print(f'Grafite ordena a lista com {comparacoes2} comparações e {trocas2} trocas.')
print(f'Lacraia ordena a lista com {comparacoes3} comparações e {trocas3} trocas.')
print(f'Rivaldo ordena a lista com {comparacoes4} comparações e {trocas4} trocas.')
print(f'Toninho ordena a lista com {comparacoes5} comparações e {trocas5} trocas.')

print('-VENCEDOR DA RODADA-')

menos_acoes = acoes1
for i in range (len(acoes_geral)):
    if menos_acoes > acoes_geral[i]:
        menos_acoes = acoes_geral[i]

vencedor = None
if menos_acoes == acoes1:
    vencedor = 'Caça-Rato'
if menos_acoes == acoes2:
    vencedor = 'Grafite'
if menos_acoes == acoes3:
    vencedor = 'Lacraia'
if menos_acoes == acoes4:
    vencedor = 'Rivaldo'
if menos_acoes == acoes5:
    vencedor = 'Toninho'

print(f'O vencedor da rodada é {vencedor}, com {menos_acoes} ações.')    

print('-Toninho está a dormir...-')

print('Os outros estagiários retornam as seguintes listas com essa quantidade de ações:')

parada = menos_acoes

comparacoes1, trocas1, sorted_lista1 = bubble_sort(lista1_2, parada) #Aqui eu tinha esquecido de passar o segundo parâmetro pras funções (que é o parâmetro de parada)
comparacoes2, trocas2, sorted_lista2 = selection_sort(lista2_2, parada)
comparacoes3, trocas3, sorted_lista3 = insertion_sort(lista3_2, parada)
comparacoes4, trocas4, sorted_lista4 = shell_sort(lista4_2, parada)

#Aqui nessa parte era uns erros besta de lógica 
pessoas = ['Caça-Rato', 'Grafite', 'Lacraia', 'Rivaldo'] #Aqui já fiz a lista sem Toninho já que ele não participa dessa fase
if vencedor != 'Toninho':
    pessoas.remove(vencedor) #Só removo o vencedor da lista se ele não for Toninho (pq Toninho nem está na lista)
    print(f'Com {menos_acoes} ações, {pessoas[0]} ordena a lista assim: {sorted_lista1}')
    print(f'Com {menos_acoes} ações, {pessoas[1]} ordena a lista assim: {sorted_lista2}')
    print(f'Com {menos_acoes} ações, {pessoas[2]} ordena a lista assim: {sorted_lista3}')

else:
    print(f'Com {menos_acoes} ações, {pessoas[0]} ordena a lista assim: {sorted_lista1}')
    print(f'Com {menos_acoes} ações, {pessoas[1]} ordena a lista assim: {sorted_lista2}')
    print(f'Com {menos_acoes} ações, {pessoas[2]} ordena a lista assim: {sorted_lista3}')
    print(f'Com {menos_acoes} ações, {pessoas[3]} ordena a lista assim: {sorted_lista4}')


