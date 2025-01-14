import time
import tracemalloc

tracemalloc.start()


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.size = 1

def update_size(node):
    if node:
        node.size = 1 + (node.left.size if node.left else 0) + (node.right.size if node.right else 0)

def insert(root, value):
    if not root:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    update_size(root)
    return root

def find_k(root, k):
    if not root:
        return None
    left_size = root.left.size if root.left else 0
    if k <= left_size:
        return find_k(root.left, k)
    elif k == left_size + 1:
        return root.value
    else:
        return find_k(root.right, k - left_size - 1)


with open('input.txt', 'r') as f:
    queries = [line.strip() for line in f.readlines()]

start_time = time.perf_counter()
root = None
results = []

for query in queries:
        if query.startswith("+"):
            x = int(query[2:])
            root = insert(root, x)
        elif query.startswith("?"):
            k = int(query[2:])
            result = find_k(root, k)
            results.append(str(result))


end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as f:
    f.write("\n".join(results))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
