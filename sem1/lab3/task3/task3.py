import tracemalloc
import time

tracemalloc.start()

def scarecrow_sort(n, k, sizes):
    groups = [[] for _ in range(k)]
    for i in range(n):
        groups[i % k].append(sizes[i])
    for group in groups:
        group.sort()
    sorted_sizes = []
    for i in range(n):
        sorted_sizes.append(groups[i % k][i // k])
    return "ДА" if sorted_sizes == sorted(sizes) else "НЕТ"


with open("input.txt", "r", encoding="utf-8") as file:
    n, k = map(int, file.readline().split())
    sizes = list(map(int, file.readline().split()))

start_time = time.perf_counter()

result = scarecrow_sort(n, k, sizes)

current, peak = tracemalloc.get_traced_memory()
end_time = time.perf_counter()

with open("output.txt", "w", encoding="utf-8") as file:
    file.write(str(result))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
