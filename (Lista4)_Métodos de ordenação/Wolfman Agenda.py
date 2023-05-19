class Heap_Max:
    def __init__(self):
        self.nodes = 0 #Quantidade de nós
        self.heap = []

    def add(self, value):
        self.heap.append(value) #Verificar se o append ta eficiente!!!
        self.nodes = self.nodes + 1
        child = self.nodes
        while True:
            if child == 1:
                break
            parent = child // 2 #Verifica quem é o pai ("//" para pegar apenas a parte inteira)
            
            if self.heap[parent - 1] >= self.heap[child - 1]: #"<=" caso quisesse o heap minimo
                break
            else:
                self.heap[parent - 1], self.heap[child - 1] = self.heap[child - 1], self.heap[parent - 1] #Troca a posição do filho com o pai
                child = parent

    def view_heap(self):
        print(self.heap)

    def remove(self):
        old_root = self.heap[0]
        self.heap[0] = self.heap[self.nodes - 1] #Passa o valor do último nó pra raiz
        self.heap.pop() #Remove o espaço que o último nó estava ocupando
        self.nodes = self.nodes - 1
        position = 1 
        parent = 1
        
        while True:
            child = 2 * parent
            if child > self.nodes: #Se o filho a esquerda for maior que a quantidade de nós é pq ele não existe, se ele não existe, também não irá existir filho a direita
                break
            
            if child + 1 <= self.nodes:
                if self.heap[child + 1 - 1] > self.heap[child - 1]: #"child" é o filho da esquerda e "child + 1" é o filho da direita. (o "-1" é pq em python o índice inicia em 0) ("<" caso quisesse heap mínimo)
                    child = child + 1
            if self.heap[parent - 1] >= self.heap[child - 1]:
                break
            else:
                self.heap[child - 1], self.heap[parent - 1] = self.heap[parent - 1], self.heap[child - 1]
                parent = child

        return old_root

    def find_min(self):
        if self.nodes == 0:
            return None
        min_value = self.heap[(self.nodes - 1) // 2] # Inicializa min_value com a primeira folha do heap
        for i in range((self.nodes - 1) // 2 + 1 , self.nodes):
            if self.heap[i] < min_value:
                min_value = self.heap[i]
        return min_value

    
    def find_max(self):
        if self.nodes != 0:
            max_value = int(self.heap[0])
            return max_value
            


h = Heap_Max()

entrada = input()
sequence = [int(numero) for numero in entrada.split()]

constant = int(input())

i = 0
for i in range(len(sequence)):
    h.add(int(sequence[i]))
    i = i + 1
    

rodadas = 0
while h.heap != []:
    max_value = h.find_max()
    min_value = h.find_min()
    
    k = max_value - abs(min_value * constant)  
    
    if k > 0:
        h.add(k)
    
    h.remove()
    rodadas = rodadas + 1


print(f"{rodadas} rodadas, partindo para a próxima!") 
