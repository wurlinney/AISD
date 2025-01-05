import tracemalloc
import time

tracemalloc.start()

def tree_height(n, parents):
    tree = [[] for _ in range(n)]
    root = -1
    for child, parent in enumerate(parents):
        if parent == -1:
            root = child
        else:
            tree[parent].append(child)
    if root == -1:
        return 0
    queue = [(root, 1)]
    max_height = 0
    while queue:
        node, depth = queue.pop(0)
        max_height = max(max_height, depth)
        for child in tree[node]:
            queue.append((child, depth + 1))

    return max_height


with open('input.txt', 'r') as f:
    n = int(f.readline())
    array = [int(x) for x in f.readline().split()]

start_time = time.perf_counter()

result = tree_height(n, array)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as f:
    f.write(str(result))


print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")