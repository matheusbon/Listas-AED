class Node: #Criando o nó

    def __init__(self, data):
        self.data = data  
        self.prev = None  
        self.next = None   

class DoublyLinkedList: #Criando classe da lista

    def __init__(self):
        self.head = None  
        self.size = 0
        
    #Função que adiciona o nó a primeira posição da lista
    def append(self, data):
        new__node = Node(data)
        if self.head == None:
            self.head = new__node
        else:
            new__node.next = self.head
            self.head.prev = new__node
            self.head = new__node
        self.size += 1


    #Função que remove um nó
    def remove(self, value):
        if self.head == None:
            return
        if self.head.data == value: #Caso em que o valor a ser removido é o primeiro da lista
            self.head = self.head.next #Indicando que agora o segundo nó passou a ser o primeiro
            if self.head != None:
                self.head.prev = None
            return
        current__node = self.head

        while current__node != None:
            if current__node.data == value:            
                current__node.prev.next = current__node.next
                if current__node.next != None:
                    current__node.next.prev = current__node.prev
                return
            current__node = current__node.next

    def print__list(self): #Função para mostrar a lista
        current__node = self.head
        while current__node != None:
            print(current__node.data)
            current__node = current__node.next

    #Função para encontrar um elemeto e passa-lo para a cabeça (head)
    def find(self, data):
        self.remove(data)
        self.append(data)


ordem, dado = ", " #Inicializando variáveis
lista = DoublyLinkedList()

while True:
    resp = input()

    try:
        ordem, data = resp.split() #Separando as variáveis que vieram na mesma entrada (ordem e dado)
    except:
        ordem = resp

    if ordem == 'ADD':
        lista.append(data)

    elif ordem == 'REM':
        lista.remove(data)

    elif ordem == 'EXIB':
        lista.print__list()
        
    elif ordem == 'FIND':
        lista.find(data)

    elif ordem == 'END':
        break
        
    else:
        continue