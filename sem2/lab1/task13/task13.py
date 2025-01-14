import tracemalloc
import time

tracemalloc.start()

def souvenirs(v):
    total_sum = sum(v)
    if total_sum % 3 != 0:
        return 0

    target_sum = total_sum // 3
    n = len(v)

    dp = [0] * (target_sum + 1)
    dp[0] = 1

    for i in v:
        for j in range(target_sum, i - 1, -1):
            if dp[j - i] > 0:
                dp[j] += 1

    return 1 if dp[target_sum] >= 3 else 0

with open('input.txt', 'r') as file:
    n = file.readline()
    v = list(map(int, file.readline().split()))

start_time = time.perf_counter()

result = souvenirs(v)

current, peak = tracemalloc.get_traced_memory()
end_time = time.perf_counter()

with open ('output.txt', 'w') as file:
    file.write(str(result))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")