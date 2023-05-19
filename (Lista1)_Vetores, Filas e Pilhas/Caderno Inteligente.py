correto = True
capas = input()
lista_capas = list(capas) 
contagem_F = 0
contagem_V = 0

for i, capa in enumerate(lista_capas):    
    if capa == 'F':
        contagem_F = contagem_F + 1
    elif capa == 'V':
        contagem_V = contagem_V + 1 
    if contagem_V > contagem_F:
        correto = False
        posicao_falha = i + 1
        break

if contagem_F > contagem_V:
    correto = False
    
    count_F = 0
    for i , capa in enumerate(lista_capas):
        if capa == "F":
            count_F = count_F + 1
            if count_F > contagem_V:
                posicao_falha = i + 1
                break
    
if correto == False:
    print (f'Incorreto, devido a capa na posição {posicao_falha}.')

else:
    print ("Correto.")