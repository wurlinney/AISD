import tracemalloc
import time

tracemalloc.start()

def count_almost_palindromes(s, n, k):
    dp = [[0] * n for _ in range(n)]
    count = 0

    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if i == j:
                dp[i][j] = 0
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] if i + 1 <= j - 1 else 0
            else:
                dp[i][j] = (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0) + 1

            if dp[i][j] <= k:
                count += 1

    return count


with open ('input.txt', 'r') as file:
    n, k = map(int, file.readline().strip().split())
    s = file.readline()

start_time = time.perf_counter()

result = count_almost_palindromes(s, n, k)

current, peak = tracemalloc.get_traced_memory()
end_time = time.perf_counter()

with open ('output.txt', 'w') as file:
    file.write(str(result))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")