class Hash_Table:
    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(size)]
        
    def hash(self, data_code):
        return data_code % self.size


    def add(self, data_code):
        i = self.hash(data_code)
        if self.table[i] == []:
          self.table[i].append(data_code)
          print(f"E: {i}")
        else:
          self.add(i+1)

    def search(self, data_code):
        i = self.hash(data_code)
        if data_code in self.table[i]:
            print(f"E: {i}")
        else:
            print("NE")

    def cap(self, i):
        if len(self.table[i]) == 0:
            print("D")
        else:
            for element in self.table[i]:
                print(f"A: {element}")

size = int(input())
num_entradas = int(input())
hash_table = Hash_Table(size)

for i in range (num_entradas):
    entrada = input()
    command, value = entrada.split()
    value = int(value)

    if command == "ADD":
        hash_table.add(value)

    elif command == "CAP":
        hash_table.cap(value)

    elif command == "SCH":
        hash_table.search(value)
