import tracemalloc
import time

tracemalloc.start()

def max_ad(a, b):
    a.sort(reverse = True)
    b.sort(reverse=True)
    max_profit = 0
    for i in range(len(a)):
        max_profit += a[i] * b[i]
    return max_profit

with open ('input.txt', 'r') as file:
    n = int(file.readline())
    a = list(map(int, file.readline().strip().split()))
    b = list(map(int, file.readline().strip().split()))


start_time = time.perf_counter()

result = max_ad(a, b)

current, peak = tracemalloc.get_traced_memory()
end_time = time.perf_counter()

with open ('output.txt', 'w') as file:
    file.write(str(result))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")