from collections import deque
import time
import tracemalloc

tracemalloc.start()

class Node:
    def __init__(self):
        self.key = None
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0
        self.balance = 0

class BinTree:
    def __init__(self):
        self.root = None
        self.nodes = {}

    def set_height(self, node):
        node.height = 1
        while node.parent:
            parent = node.parent
            if parent.height <= node.height:
                parent.height = node.height + 1
            else:
                break
            node = parent

    def set_balance(self):
        for i in range(1, n + 1):
            node = self.nodes[i]
            if node.left:
                if node.right:
                    node.balance = node.right.height - node.left.height
                else:
                    node.balance = -node.left.height
            else:
                if node.right:
                    node.balance = node.right.height
                else:
                    node.balance = 0

    def left_turn(self, A):
        B = A.right
        if B.balance == -1:
            C = B.left
            X = C.left
            Y = C.right
            if X:
                X.parent = A
            A.right = X
            if Y:
                Y.parent = B
            B.left = Y
            if A.key != self.root.key:
                C.parent = A.parent
                if A.parent.left == A:
                    A.parent.left = C
                else:
                    A.parent.right = C
            else:
                self.root = C
            A.parent = C
            C.left = A
            B.parent = C
            C.right = B
        else:
            Y = B.left
            if Y:
                Y.parent = A
            A.right = Y
            if A != self.root:
                B.parent = A.parent
                if A.parent.left == A:
                    A.parent.left = B
                else:
                    A.parent.right = B
            else:
                self.root = B
            A.parent = B
            B.left = A

def tree_output(tree, n):
    q = deque()
    q.append(tree.root)
    i = 1
    with open('output.txt', 'w') as d:
        d.write(str(n) + '\n')
        while len(q) != 0:
            node = q.popleft()
            d.write(str(node.key))
            if node.left:
                i += 1
                d.write(' ' + str(i))
                q.append(node.left)
            else:
                d.write(' 0')
            if node.right:
                i += 1
                d.write(' ' + str(i) + '\n')
                q.append(node.right)
            else:
                d.write(' 0\n')


with open('input.txt', 'r') as file:
    n = int(file.readline())
    tree = BinTree()
    data = []
    leaves = []
    for i in range(1, n + 1):
        data.append(list(map(int, file.readline().split())))
        tree.nodes[i] = Node()
        tree.nodes[i].key = data[i - 1][0]
        if data[i - 1][1] == 0 and data[i - 1][2] == 0:
            leaves.append(i)

start_time = time.perf_counter()

for i in range(1, n + 1):
    if data[i - 1][1] != 0:
        tree.nodes[i].left = tree.nodes[data[i - 1][1]]
        tree.nodes[data[i - 1][1]].parent = tree.nodes[i]
    if data[i - 1][2] != 0:
        tree.nodes[i].right = tree.nodes[data[i - 1][2]]
        tree.nodes[data[i - 1][2]].parent = tree.nodes[i]
    if i == 1:
        tree.root = tree.nodes[i]

for i in leaves:
    tree.set_height(tree.nodes[i])

tree.set_balance()
tree.left_turn(tree.root)
tree_output(tree, n)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()


print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")