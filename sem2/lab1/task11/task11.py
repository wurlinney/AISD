import tracemalloc
import time

tracemalloc.start()

def max_gold(w, weights):
    dp = [0] * (w + 1)

    for weight in weights:
        for j in range(w, weight - 1, -1):
            dp[j] = max(dp[j], dp[j - weight] + weight)

    return dp[w]


with open('input.txt', 'r') as file:
    w, n = map(int, file.readline().split())
    weights = list(map(int, file.readline().split()))

start_time = time.perf_counter()

result = max_gold(w, weights)

current, peak = tracemalloc.get_traced_memory()
end_time = time.perf_counter()

with open ('output.txt', 'w') as file:
    file.write(str(result))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")