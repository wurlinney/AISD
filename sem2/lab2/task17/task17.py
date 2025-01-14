import time
import tracemalloc
from collections import deque

tracemalloc.start()

class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
    def __str__(self):
        return f'{self.value}({self.parent}) -> [{self.left}, {self.right}]'

class Splay:
    def __init__(self, root=None):
        self.root = root
        self.x = 0
        self.M = 1000000001
        self.sum = []

    def splay(self, node):
        while node.parent != None:
            if node.parent.parent == None:
                if node == node.parent.left:
                    self.right_turn(node.parent)
                else:
                    self.left_turn(node.parent)
            elif node == node.parent.left and node.parent == node.parent.parent.left:
                self.right_turn(node.parent.parent)
                self.right_turn(node.parent)
            elif node == node.parent.right and node.parent == node.parent.parent.right:
                self.left_turn(node.parent.parent)
                self.left_turn(node.parent)
            elif node == node.parent.right and node.parent == node.parent.parent.left:
                self.left_turn(node.parent)
                self.right_turn(node.parent)
            else:
                self.right_turn(node.parent)
                self.left_turn(node.parent)

    def join(self, lt, rt):
        if lt == None:
            return rt
        if rt == None:
            return lt

        x = self.mx(lt)
        self.splay(x)
        x.right = rt
        rt.parent = x
        return x

    def mx(self, tree):
        while tree.right != None:
            tree = tree.right
        return tree

    def left_turn(self, node):
        y = node.right
        node.right = y.left
        if y.left != None:
            y.left.parent = node

        y.parent = node.parent
        if node.parent == None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y

        y.left = node
        node.parent = y

    def right_turn(self, node):
        y = node.left
        node.left = y.right
        if y.right != None:
            y.right.parent = node

        y.parent = node.parent
        if node.parent == None:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y

        y.right = node
        node.parent = y

    def add(self, value):
        value = (value + self.x) % self.M
        if self.find_h(self.root, value) != None:
            return

        node = Node(value)
        y = None
        x = self.root
        while x != None:
            y = x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == None:
            self.root = node
        elif node.value < y.value:
            y.left = node
        else:
            y.right = node

        self.splay(node)

    def find_h(self, node, value):
        if node == None or value == node.value:
            return node
        elif value < node.value:
            return self.find_h(node.left, value)
        else:
            return self.find_h(node.right, value)

    def find(self, value):
        value = (value + self.x) % self.M
        el = self.find_h(self.root, value)
        if el != None:
            self.splay(el)
            return 'Found'
        return 'Not found'

    def delete(self, value):
        value = (value + self.x) % self.M
        node = self.root
        necessary_element = None
        lt = None
        rt = None

        while node != None:
            if node.value == value:
                necessary_element = node

            if node.value < value:
                node = node.right
            else:
                node = node.left

        if necessary_element == None:
            return 'Not found'

        self.splay(necessary_element)
        if necessary_element.right != None:
            rt = necessary_element.right
            rt.parent = None
        else:
            rt = None
        lt = necessary_element
        lt.right = None
        necessary_element = None

        if lt.left != None:
            lt.left.parent = None

        self.root = self.join(lt.left, rt)
        lt = None

    def summa(self, l, r):
        if self.root == None:
            return 0
        l = (l + self.x) % self.M
        r = (r + self.x) % self.M
        que = deque([])
        current = self.root
        que.append(current)
        s = 0
        while que:
            el = que.popleft()
            if l <= el.value <= r:
                s += el.value
            if current.left != None and current.left.value >= l:
                que.append(current.left)
            if current.right != None and current.right.value >= r:
                que.append(current.right)

            if len(que) > 0:
                current = que[0]
            else:
                self.x = s
                return s

with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    operations = [line.strip() for line in file]


start_time = time.perf_counter()

Splay_Tree = Splay()
p = open('output.txt', 'w')
for op in operations:
    if op.startswith('+'):
        _, x = op.split()
        result = Splay_Tree.add(int(x))
    elif op.startswith('-'):
        _, x = op.split()
        result = Splay_Tree.delete(int(x))
    elif op.startswith('?'):
        _, x = op.split()
        p.write(Splay_Tree.find(int(x)) + '\n')
    elif op.startswith('s'):
        _, l, r = op.split()
        p.write(str(Splay_Tree.summa(int(l), int(r))) + '\n')
p.close()

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
