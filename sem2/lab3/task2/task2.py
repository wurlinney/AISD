import tracemalloc
import time
import sys
sys.setrecursionlimit(10**6)

tracemalloc.start()

def dfs(graph, visited, vertex):
    visited[vertex] = True
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)


def count_connected_components(graph):
    n = len(graph)
    visited = [False] * n
    count = 0
    for vertex in range(n):
        if not visited[vertex]:
            count += 1
            dfs(graph, visited, vertex)
    return count


with open('input.txt', 'r') as file:
    n, m = map(int, file.readline().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, file.readline().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)


start_time = time.perf_counter()

component_count = count_connected_components(graph)


end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as file:
    file.write(str(component_count))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
