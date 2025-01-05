import tracemalloc
import time

tracemalloc.start()


def radix_sort_vertical(n, m, k, strings):
    indices = list(range(n))
    for phase in range(k):
        current_position = m - 1 - phase
        indices.sort(key=lambda i: strings[current_position][i])
    return [i + 1 for i in indices]

with open("input.txt", "r") as file:
    n, m, k = map(int, file.readline().strip().split())
    strings = [file.readline().strip() for _ in range(m)]  # Читаем строки по вертикали

start_time = time.perf_counter()

result = radix_sort_vertical(n, m, k, strings)

current, peak = tracemalloc.get_traced_memory()
end_time = time.perf_counter()

with open("output.txt", "w") as file:
    file.write(" ".join(map(str, result)))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
