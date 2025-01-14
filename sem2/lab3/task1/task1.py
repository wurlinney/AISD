import tracemalloc
import time
import sys
sys.setrecursionlimit(10**6)

tracemalloc.start()

def dfs(graph, start, end, visited):
    if start == end:
        return True
    visited[start] = True
    for neighbor in graph[start]:
        if not visited[neighbor]:
            if dfs(graph, neighbor, end, visited):
                return True
    return False


with open('input.txt', 'r') as file:
    n, m = map(int, file.readline().split())
    graph = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        u, v = map(int, file.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    u, v = map(int, file.readline().split())

start_time = time.perf_counter()

visited = {i: False for i in range(1, n + 1)}
result = 1 if dfs(graph, u, v, visited) else 0

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()


with open('output.txt', 'w') as file:
    file.write(str(result))


print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")