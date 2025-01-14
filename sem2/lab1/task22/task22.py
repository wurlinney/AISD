from itertools import product
from functools import reduce
import tracemalloc
import time

tracemalloc.start()

def generate_patterns(n):
    return list(product([False, True], repeat=n))

def is_compatible(a, b):
    for i in range(len(a) - 1):
        if a[i] == b[i] == a[i + 1] == b[i + 1]:
            return False
    return True

def build_compatibility_matrix(patterns):
    size = len(patterns)
    matrix = [[False] * size for _ in range(size)]
    for i in range(size):
        for j in range(i, size):
            compatible = is_compatible(patterns[i], patterns[j])
            matrix[i][j] = matrix[j][i] = compatible
    return matrix

def count_pretty_patterns(matrix, m):
    size = len(matrix)
    dp = [[0] * size for _ in range(m)]
    for i in range(size):
        dp[0][i] = 1

    for i in range(1, m):
        for j in range(size):
            for k in range(size):
                if matrix[k][j]:
                    dp[i][j] += dp[i - 1][k]

    return dp


with open('input.txt', 'r') as file:
    n, m = map(int, file.readline().strip().split())

start_time = time.perf_counter()

max_dim = max(n, m)
min_dim = min(n, m)


patterns = generate_patterns(min_dim)


compatibility_matrix = build_compatibility_matrix(patterns)


dp_table = count_pretty_patterns(compatibility_matrix, max_dim)


result = sum(dp_table[-1])

current, peak = tracemalloc.get_traced_memory()
end_time = time.perf_counter()


with open('output.txt', 'w') as file:
    file.write(str(result) + '\n')


print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
