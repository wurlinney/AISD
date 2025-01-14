import tracemalloc
import time

tracemalloc.start()

def max_requests(requests):
    max_count = 0
    last_end_time = 0
    requests.sort(key=lambda x: x[1])
    for start, end in requests:
        if start >= last_end_time:
            max_count += 1
            last_end_time = end

    return max_count



with open ('input.txt', 'r') as file:
    n = int(file.readline())
    requests = []
    for i in range(n):
        start, end = map(int, file.readline().split())
        requests.append((start, end))

start_time = time.perf_counter()

result = max_requests(requests)

current, peak = tracemalloc.get_traced_memory()
end_time = time.perf_counter()

with open ('output.txt', 'w') as file:
    file.write(str(result))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")