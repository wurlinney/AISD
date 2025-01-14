import time
import tracemalloc

tracemalloc.start()

import sys

sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def build_tree(tree, index):
    if index == -1:
        return None
    key, left_idx, right_idx = tree[index]
    node = Node(key)
    node.left = build_tree(tree, left_idx)
    node.right = build_tree(tree, right_idx)
    return node


def is_bst(node, min_val, max_val):
    if node is None:
        return True
    if not (min_val < node.key <= max_val):
        return False
    return is_bst(node.left, min_val, node.key - 1) and is_bst(node.right, node.key, max_val)

with open('input.txt', 'r') as f:
    n = int(f.readline())
    tree = []
    for _ in range(n):
        K, L, R = map(int, f.readline().split())
        tree.append((K, L, R))

start_time = time.perf_counter()

if n == 0:
    with open('output.txt', 'w') as f:
        f.write("CORRECT")

else:
    root = build_tree(tree, 0)
    if is_bst(root, -2 ** 31 - 1, 2 ** 31):
        with open('output.txt', 'w') as f:
            f.write("CORRECT")
    else:
        with open('output.txt', 'w') as f:
            f.write("INCORRECT")

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")