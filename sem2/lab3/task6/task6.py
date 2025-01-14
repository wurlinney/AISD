import tracemalloc
import time
from collections import deque

tracemalloc.start()

def bfs_shortest_path(n, graph, start, end):
    if start == end:
        return 0
    visited = [False] * (n + 1)
    queue = deque()
    queue.append((start, 0))
    visited[start] = True
    while queue:
        current, distance = queue.popleft()
        for neighbor in graph[current]:
            if neighbor == end:
                return distance + 1
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, distance + 1))
    return -1


with open('input.txt', 'r') as file:
    lines = file.readlines()
    n, m = map(int, lines[0].split())
    graph = {i: [] for i in range(1, n + 1)}
    for line in lines[1:m + 1]:
        u, v = map(int, line.split())
        graph[u].append(v)
        graph[v].append(u)
    u, v = map(int, lines[m + 1].split())

start_time = time.perf_counter()


result = bfs_shortest_path(n, graph, u, v)


end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as file:
    file.write(str(result))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")

