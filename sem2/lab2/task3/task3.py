import time
import tracemalloc

tracemalloc.start()

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        node = self.root
        while True:
            if key < node.key:
                if node.left is None:
                    node.left = Node(key)
                    return
                node = node.left
            elif key > node.key:
                if node.right is None:
                    node.right = Node(key)
                    return
                node = node.right
            else:
                return

    def find_min_gt(self, key):
        node = self.root
        min_gt = 0
        while node is not None:
            if node.key > key:
                min_gt = node.key
                node = node.left
            else:
                node = node.right
        return min_gt



with open('input.txt', 'r') as f:
    queries = [line.strip() for line in f.readlines()]

start_time = time.perf_counter()

bst = BST()
results = []

for query in queries:
    if query.startswith("+"):
        x = int(query[1:])
        bst.insert(x)
    elif query.startswith(">"):
        x = int(query[1:])
        min_gt = bst.find_min_gt(x)
        results.append(str(min_gt))

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as f:
    f.write("\n".join(results))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
