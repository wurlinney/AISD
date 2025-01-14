import tracemalloc
import time
import heapq

tracemalloc.start()

def dijkstra(n, graph, start, end):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex == end:
            return current_distance

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return -1



with open('input.txt', 'r') as file:
    lines = file.readlines()
    n, m = map(int, lines[0].split())
    graph = {i: [] for i in range(1, n + 1)}
    for line in lines[1:m + 1]:
        u, v, w = map(int, line.split())
        graph[u].append((v, w))
    u, v = map(int, lines[m + 1].split())

start_time = time.perf_counter()

result = dijkstra(n, graph, u, v)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as file:
    file.write(str(result))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")