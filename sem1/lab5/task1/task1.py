import tracemalloc
import time

tracemalloc.start()


def check_heap(n, array):
    for i in range(1, n):
        if 2 * i < n and array[i - 1] > array[2 * i - 1]:
            return "NO"
        if 2 * i + 1 < n and array[i - 1] > array[2 * i]:
            return "NO"
    return "YES"


with open('input.txt', 'r') as f:
    n = int(f.readline())
    array = [int(x) for x in f.readline().split()]

start_time = time.perf_counter()

result = check_heap(n, array)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as f:
    f.write(result)


print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")

