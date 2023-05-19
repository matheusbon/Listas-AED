root = "root"

class node:
	def __init__(self, value=None):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = 1


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

        print(f"{name} INSERIDO")

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left == None:
                cur_node.left = node(value)
                cur_node.left.parent = cur_node
                self._check_insertion(cur_node.left)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right == None:
                cur_node.right = node(value)
                cur_node.right.parent = cur_node
                self._check_insertion(cur_node.right)
            else:
                self._insert(value, cur_node.right)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node == None: return cur_height
        left_height = self._height(cur_node.left, cur_height+1)
        right_height = self._height(cur_node.right, cur_height+1)
        return max(left_height, right_height)

    def print_inorder(self, root):
        if self.root != None:
            self._print_inorder(self.root)

    def _print_inorder(self, cur_node):
        if cur_node != None:
            self._print_inorder(cur_node.left)
            maior = tree.max()
            if cur_node.value != maior:
                print(str(cur_node.value), end=" ")
                self._print_inorder(cur_node.right)
            else:
                print(str(cur_node.value), end="\n")
    
    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left != None:
            return self._find(value, cur_node.left)
        elif value > cur_node.value and cur_node.right != None:
            return self._find(value, cur_node.right)

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):

        if node == None or self.find(node.value) == None:
            return None

        def min_value_node(n):
            current = n
            while current.left != None:
                current = current.left
            return current

        def qtd_children(n):
            qtd_children = 0
            if n.left != None: qtd_children += 1
            if n.right != None: qtd_children += 1
            return qtd_children

        node_parent = node.parent

        node_children = qtd_children(node)

        if node_children == 0:
            if node_parent != None:
                if node_parent.left == node:
                    node_parent.left = None
                else:
                    node_parent.right = None
            else:
                self.root = None

        if node_children == 1:
            if node.left != None:
                child = node.left
            else:
                child = node.right

            if node_parent != None:
                if node_parent.left == node:
                    node_parent.left = child
                else:
                    node_parent.right = child
            else:
                self.root = child
            child.parent = node_parent

        if node_children == 2:
            successor = min_value_node(node.right)
            node.value = successor.value
            self.delete_node(successor)
            return

        if node_parent != None:

            node_parent.height = 1 + \
                max(self.get_height(node_parent.left),
                    self.get_height(node_parent.right))

            self._check_deletion(node_parent)

    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left != None:
            return self._search(value, cur_node.left)
        elif value > cur_node.value and cur_node.right != None:
            return self._search(value, cur_node.right)
        return False

    def _check_insertion(self, cur_node, path=[]):
        if cur_node.parent == None: return
        path = [cur_node]+path

        left_height = self.get_height(cur_node.parent.left)
        right_height = self.get_height(cur_node.parent.right)

        if abs(left_height-right_height) > 1:
            path = [cur_node.parent]+path
            self._rebalance_node(path[0], path[1], path[2])
            return

        new_height = 1+cur_node.height
        if new_height > cur_node.parent.height:
            cur_node.parent.height = new_height

        self._check_insertion(cur_node.parent, path)

    def _check_deletion(self, cur_node):
        if cur_node == None: return

        left_height = self.get_height(cur_node.left)
        right_height = self.get_height(cur_node.right)

        if abs(left_height-right_height) > 1:
            y = self.taller_child(cur_node)
            x = self.taller_child(y)
            self._rebalance_node(cur_node, y, x)

        self._check_deletion(cur_node.parent)

    def _rebalance_node(self, z, y, x):
        if y == z.left and x == y.left:
            self._right_rotate(z)
        elif y == z.left and x == y.right:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y == z.right and x == y.right:
            self._left_rotate(z)
        elif y == z.right and x == y.left:
            self._right_rotate(y)
            self._left_rotate(z)

    def _right_rotate(self, z):
        sub_root = z.parent
        y = z.left
        t3 = y.right
        y.right = z
        z.parent = y
        z.left = t3
        if t3 != None: t3.parent = z
        y.parent = sub_root
        if y.parent == None:
                self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y
        z.height = 1+max(self.get_height(z.left),
            self.get_height(z.right))
        y.height = 1+max(self.get_height(y.left),
            self.get_height(y.right))

    def _left_rotate(self, z):
        sub_root = z.parent
        y = z.right
        t2 = y.left
        y.left = z
        z.parent = y
        z.right = t2
        if t2 != None: t2.parent = z
        y.parent = sub_root
        if y.parent == None:
            self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y
        z.height = 1+max(self.get_height(z.left),
            self.get_height(z.right))
        y.height = 1+max(self.get_height(y.left),
            self.get_height(y.right))

    def get_height(self, cur_node):
        if cur_node == None: return 0
        return cur_node.height

    def taller_child(self, cur_node):
        left_height = self.get_height(cur_node.left)
        right_height = self.get_height(cur_node.right)
        if left_height >= right_height:
            return cur_node.left
        else:
            return cur_node.right

    def min(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            return self.min(node.left)
        else:
            return node.value

    def max(self, node=root):
        if node == root:
            node = self.root
        while node.right:
            node = node.right
        return node.value


command, name = ", "
tree = BinarySearchTree()


while command != "FIM":
    entrada = input()

    if " " in entrada:
        command, name = entrada.split()

    else:
        command = entrada

    if command == "INSERIR":
        if tree.search(name):
            print(f"{name} JA EXISTE")
        else:
            tree.insert(name)

    elif command == "DELETAR":
        if not tree.search(name):
            print(f"{name} NAO ENCONTRADO")
        else:
            tree.delete_value(name)
            print(f"{name} DELETADO")
    elif command == "MAXIMO":
        if tree.root is None:
            print("ARVORE VAZIA")
        else:
            maior = tree.max()
            print(f"MAIOR: {maior}")

    elif command == "MINIMO":
        if tree.root is None:
            print("ARVORE VAZIA")
        else:
            menor = tree.min()
            print(f"MENOR: {menor}")

    elif command == "ALTURA":
        altura = tree.height()
        print(f"ALTURA: {altura}")

    elif command == "FIM":
        if tree.root is None:
            print("ARVORE VAZIA")
        else:
            tree.print_inorder(root)