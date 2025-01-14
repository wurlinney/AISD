import heapq
import tracemalloc
import time

tracemalloc.start()

def dijkstra(n, d, v, buses):
    arrival_time = [float('inf')] * (n + 1)
    arrival_time[d] = 0
    queue = [(0, d)]

    while queue:
        current_time, current_village = heapq.heappop(queue)

        if current_village == v:
            return current_time

        if current_time > arrival_time[current_village]:
            continue

        for bus in buses[current_village]:
            departure, destination, arrival = bus
            if current_time <= departure and arrival < arrival_time[destination]:
                arrival_time[destination] = arrival
                heapq.heappush(queue, (arrival, destination))

    return -1


with open('input.txt', 'r') as file:
    lines = file.readlines()
    n = int(lines[0].strip())
    d, v = map(int, lines[1].strip().split())
    r = int(lines[2].strip())
    buses = [[] for _ in range(n + 1)]
    for i in range(3, 3 + r):
        departure_village, departure_time, destination_village, arrival_time = map(int, lines[i].strip().split())
        buses[departure_village].append((departure_time, destination_village, arrival_time))

start_time = time.perf_counter()

result = dijkstra(n, d, v, buses)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as file:
    file.write(str(result))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")