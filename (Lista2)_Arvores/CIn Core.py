class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.level = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        level = 0
        if self.root is None:
            self.root = node
            self.root.level = level
        else:
            current = self.root
            while True:
                level += 1
                if value < current.value:
                    if current.left is None:
                        current.left = node
                        node.parent = current
                        node.level = level
                        break
                    else:
                        current = current.left
                elif value > current.value:
                    if current.right is None:
                        current.right = node
                        node.parent = current
                        node.level = level
                        break
                    else:
                        current = current.right
        print(level)

    def search(self, value):
        if self.root is None:
            print("-1")
            return

        current = self.root
        level = -1
        while current is not None:
            level += 1
            if current.value == value:
                print(level)
                self._move_to_root(current)
                return
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        print("-1")

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        if new_root.left is not None:
            new_root.left.parent = node
        new_root.parent = node.parent
        if node.parent is None:
            self.root = new_root
        elif node == node.parent.left:
            node.parent.left = new_root
        else:
            node.parent.right = new_root
        new_root.left = node
        node.parent = new_root

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        if new_root.right is not None:
            new_root.right.parent = node
        new_root.parent = node.parent
        if node.parent is None:
            self.root = new_root
        elif node == node.parent.right:
            node.parent.right = new_root
        else:
            node.parent.left = new_root
        new_root.right = node
        node.parent = new_root

    def _move_to_root(self, node):
        stack = []
        while node.parent is not None:
            stack.append(node)
            node = node.parent

        while stack:
            node = stack.pop()
            if node == node.parent.left:
                self._rotate_right(node.parent)
            else:
                self._rotate_left(node.parent)

        self.root = node



ordem, data = ", "
arvore = BinarySearchTree()

while True:
    try:
        entrada = input()
    except EOFError:
        break    
    
    ordem, data = entrada.split()
        
    if ordem == "ADD":
        arvore.insert(int(data))
    elif ordem == "SCH":
        arvore.search(int(data))