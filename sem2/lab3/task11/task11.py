import tracemalloc
import time
from collections import deque

tracemalloc.start()

def bfs(start, end, graph):
    queue = deque([(start, 0)])
    visited = set()

    while queue:
        current, steps = queue.popleft()
        if current == end:
            return steps
        if current in visited:
            continue

        visited.add(current)

        if current in graph:
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, steps + 1))

    return -1

with open('input.txt', 'r') as file:
    lines = file.readlines()
    m = int(lines[0])
    graph = {}
    for i in range(1, m + 1):
        reaction = lines[i].strip().split(' -> ')
        if len(reaction) == 2:
            src, dest = reaction
            if src not in graph:
                graph[src] = []
            graph[src].append(dest)
    start = lines[m + 1].strip()
    end = lines[m + 2].strip()

start_time = time.perf_counter()

result = bfs(start, end, graph)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as file:
    file.write(str(result))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")