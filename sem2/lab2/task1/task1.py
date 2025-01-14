import time
import tracemalloc
import sys
sys.setrecursionlimit(200000)


tracemalloc.start()

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def inorder(root, result):
    if root is None:
        return
    inorder(root.left, result)
    result.append(str(root.key))
    inorder(root.right, result)


def preorder(root, result):
    if root is None:
        return
    result.append(str(root.key))
    preorder(root.left, result)
    preorder(root.right, result)


def postorder(root, result):
    if root is None:
        return
    postorder(root.left, result)
    postorder(root.right, result)
    result.append(str(root.key))


with open('input.txt', 'r') as infile:
    n = int(infile.readline().strip())
    node_data = [list(map(int, line.split())) for line in infile.readlines()]

start_time = time.perf_counter()

nodes = [Node(key) for key, _, _ in node_data]

for i, (key, left_index, right_index) in enumerate(node_data):
    if left_index != -1:
        nodes[i].left = nodes[left_index]
    if right_index != -1:
        nodes[i].right = nodes[right_index]

inorder_result = []
preorder_result = []
postorder_result = []

inorder(nodes[0], inorder_result)
preorder(nodes[0], preorder_result)
postorder(nodes[0], postorder_result)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()


with open('output.txt', 'w') as outfile:
    outfile.write(' '.join(inorder_result) + '\n')
    outfile.write(' '.join(preorder_result) + '\n')
    outfile.write(' '.join(postorder_result) + '\n')

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")