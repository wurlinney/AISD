import tracemalloc
import time

tracemalloc.start()

def long_subsequence(n, A, m, B):
    table = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    return table[n][m]


with open('input.txt', 'r') as file:
    n = int(file.readline())
    A = list(map(int, file.readline().strip().split()))
    m = int(file.readline())
    B = list(map(int, file.readline().strip().split()))

start_time = time.perf_counter()

result = long_subsequence(n, A, m, B)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as file:
    file.write(str(result))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
