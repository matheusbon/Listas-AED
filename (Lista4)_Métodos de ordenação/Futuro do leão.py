def Merge_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if(fim - inicio > 1):
        meio = (fim + inicio)//2
        Merge_sort(lista, inicio, meio)
        Merge_sort(lista, meio, fim)
        Merge(lista, inicio, meio, fim)

def Merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left = top_left + 1
        else:
            lista[k] = right[top_right]
            top_right = top_right + 1

entrada1 = input()
lista1 = [int(numero) for numero in entrada1.split()]

entrada2 = input()
lista2 = [int(numero) for numero in entrada2.split()]

lista3 = lista1 + lista2
tamanho_lista = len(lista3)

Merge_sort(lista3)

mediana = float(((lista3[int((tamanho_lista/2) - 1)] + lista3[int(tamanho_lista/2)]) / 2))

print("O salário sugerido por Juba na primeira negociação será de {:.2f}".format(mediana) + " mil reais.")