import tracemalloc
import time
import sys

sys.setrecursionlimit(10**6)

tracemalloc.start()

def dfs(v, visited, rec_stack, graph):
    visited[v] = True
    rec_stack[v] = True

    for neighbor in graph.get(v, []):
        if not visited[neighbor]:
            if dfs(neighbor, visited, rec_stack, graph):
                return True
        elif rec_stack[neighbor]:
            return True

    rec_stack[v] = False
    return False

def is_cyclic(graph, n):
    visited = {v: False for v in range(1, n + 1)}
    rec_stack = {v: False for v in range(1, n + 1)}
    for node in range(1, n + 1):
        if not visited[node]:
            if dfs(node, visited, rec_stack, graph):
                return 1
    return 0


with open('input.txt', 'r') as file:
    lines = file.readlines()
    n, m = map(int, lines[0].split())
    graph = {}
    for line in lines[1:m + 1]:
        u, v = map(int, line.split())
        if u not in graph:
            graph[u] = []
        graph[u].append(v)

start_time = time.perf_counter()

result = is_cyclic(graph, n)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as file:
    file.write(str(result))


print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")