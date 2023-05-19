def pilhaImaculada(pilha):
    pilha_ordenada = sorted(pilha)
    if pilha != pilha_ordenada:
        return False
    else:
        return True

def novaLocacao(pilha, codigo):
    pilha.append(codigo)
    pilha.sort()
    print(pilha)

entrada = input()
pilha = entrada.split(",")

codigo = input()

pilhaImaculada(pilha)
if pilhaImaculada(pilha):
    novaLocacao(pilha, codigo)

else:
    print("A pilha está um caos.")

