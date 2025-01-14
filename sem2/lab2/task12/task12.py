import time
import tracemalloc

tracemalloc.start()

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def build_tree(nodes_data):
    nodes = {i: Node(key) for i, (key, left, right) in nodes_data.items()}

    for i, (key, left, right) in nodes_data.items():
        if left != 0:
            nodes[i].left = nodes[left]
        if right != 0:
            nodes[i].right = nodes[right]

    return nodes[1], nodes

def tree_balance(node, balances, node_id_map):

    if not node:
        return 0

    left_height = tree_balance(node.left, balances, node_id_map)
    right_height = tree_balance(node.right, balances, node_id_map)
    current_height = 1 + max(left_height, right_height)
    balance = right_height - left_height
    balances[node_id_map[node]] = balance

    return current_height


with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    data = {}
    for i in range(1, n + 1):
        k, l, r = map(int, file.readline().strip().split())
        data[i] = (k, l, r)

start_time = time.perf_counter()

root, nodes = build_tree(data)

node_id_map = {node: node_id for node_id, node in nodes.items()}

balances = {}

tree_balance(root, balances, node_id_map)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as file:
    for i in range(1, n + 1):
        file.write(f"{balances[i]}\n")



print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")