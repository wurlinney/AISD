import tracemalloc
import time

tracemalloc.start()

def min_refills(d, m, stops):
    stops = [0] + stops + [d]
    num_refills = 0
    current_refill = 0

    while current_refill < len(stops) - 1:
        last_refill = current_refill

        while current_refill < len(stops) - 1 and (stops[current_refill + 1] - stops[last_refill] <= m):
            current_refill += 1
        if current_refill == last_refill:
            return -1
        if current_refill < len(stops) - 1:
            num_refills += 1

    return num_refills


with open ('input.txt', 'r') as file:
    d = int(file.readline())
    m = int(file.readline())
    n = int(file.readline())
    stops = list(map(int, file.readline().split()))


start_time = time.perf_counter()

result = min_refills(d, m, stops)

current, peak = tracemalloc.get_traced_memory()
end_time = time.perf_counter()

with open ('output.txt', 'w') as file:
    file.write(str(result))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")