class Caixa:
    def __init__(self):
        self.fila = []
        self.total_arrecadado = 0
    
    def inserir_cliente(self, nome, valor):
        self.fila.append((nome, valor))
        print(f"{nome} entrou na fila {self.fila_id}")
    
    def proximo_cliente(self):
        if not self.fila:
            return
        nome, valor = self.fila.pop(0)
        self.total_arrecadado += valor
        print(f"{nome} foi chamado para o caixa {self.fila_id}")
    
    def realocar_fila(self, outra_fila):
        if not self.fila:
            return
        posicao_inicial = len(self.fila) // 2
        fila_realocada = self.fila[posicao_inicial:][::-1]
        outra_fila.fila = fila_realocada + outra_fila.fila
        self.fila = self.fila[:posicao_inicial]
    
    def __str__(self):
        return f"Caixa {self.fila_id}: R$ {self.total_arrecadado:.2f}"

caixa1 = Caixa()
caixa1.fila_id = 1
caixa2 = Caixa()
caixa2.fila_id = 2

while True:
    try:
        linha = input().strip()
    except EOFError:
        break
    
    if linha == "FIM":
        break
    
    comando, *parametros = linha.split()
    
    if comando == "ENTROU:":
        nome, fila_id, valor = parametros
        valor = float(valor)
        if fila_id == "1":
            caixa1.inserir_cliente(nome, valor)
            if not caixa2.fila:
                caixa1.realocar_fila(caixa2)
        elif fila_id == "2":
            caixa2.inserir_cliente(nome, valor)
            if not caixa1.fila:
                caixa2.realocar_fila(caixa1)
    
    elif comando == "PROXIMO:":
        fila_id = int(parametros[0])
        if fila_id == 1:
            caixa1.proximo_cliente()
            if not caixa2.fila:
                caixa1.realocar_fila(caixa2)
        elif fila_id == 2:
            caixa2.proximo_cliente()
            if not caixa1.fila:
                caixa2.realocar_fila(caixa1)

print(str(caixa1) + ", " + str(caixa2))
