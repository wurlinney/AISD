import tracemalloc
import time
import sys

sys.setrecursionlimit(10 ** 6)
tracemalloc.start()

def dfs(node, visited, graph, stack):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph, stack)
    stack.append(node)


def reverse_graph(graph, n):
    reversed_graph = {i: [] for i in range(1, n + 1)}
    for u in graph:
        for v in graph[u]:
            reversed_graph[v].append(u)
    return reversed_graph


def count_scc(graph, n):
    visited = {i: False for i in range(1, n + 1)}
    stack = []
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, visited, graph, stack)
    reversed_graph = reverse_graph(graph, n)
    visited = {i: False for i in range(1, n + 1)}
    count = 0
    while stack:
        node = stack.pop()
        if not visited[node]:
            dfs(node, visited, reversed_graph, [])
            count += 1

    return count

with open('input.txt', 'r') as file:
    n, m = map(int, file.readline().split())
    graph = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        u, v = map(int, file.readline().split())
        graph[u].append(v)

start_time = time.perf_counter()

result = count_scc(graph, n)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as file:
    file.write(str(result))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")