import tracemalloc
import time

tracemalloc.start()

def bellman_ford(n, edges, start):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0

    for _ in range(n - 1):
        for u, v, w in edges:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    negative_cycle = [False] * (n + 1)
    for _ in range(n - 1):
        for u, v, w in edges:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                negative_cycle[v] = True

    result = []
    for i in range(1, n + 1):
        if distances[i] == float('inf'):
            result.append("*")
        elif negative_cycle[i]:
            result.append("-")
        else:
            result.append(str(distances[i]))

    return result

with open('input.txt', 'r') as file:
    lines = file.readlines()
    n, m = map(int, lines[0].split())
    edges = []
    for line in lines[1:m + 1]:
        u, v, w = map(int, line.split())
        edges.append((u, v, w))
    s = int(lines[m + 1])

start_time = time.perf_counter()

result = bellman_ford(n, edges, s)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as file:
    for res in result:
        file.write(res + "\n")


print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")