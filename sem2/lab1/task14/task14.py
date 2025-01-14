import tracemalloc
import time

tracemalloc.start()

def max_expr_value(expr):
    n = (len(expr) + 1) // 2

    max_val = [[0] * n for _ in range(n)]
    min_val = [[0] * n for _ in range(n)]

    for i in range(n):
        max_val[i][i] = int(expr[2*i])
        min_val[i][i] = int(expr[2 * i])

    for length in range(1, n):
        for i in range(n - length):
            j = i + length
            max_val[i][j] = float('-inf')
            min_val[i][j] = float('inf')

            for k in range(i, j):
                a, b = max_val[i][k], max_val[k + 1][j]
                c, d = min_val[i][k], min_val[k + 1][j]
                operation = expr[2 * k + 1]

                if operation == '+':
                    max_val[i][j] = max(max_val[i][j], a + b)
                    min_val[i][j] = min(min_val[i][j], c + d)
                elif operation == '-':
                    max_val[i][j] = max(max_val[i][j], a - d)
                    min_val[i][j] = min(min_val[i][j], c - b)
                elif operation == '*':
                    max_val[i][j] = max(max_val[i][j], a * b, a * d, c * b, c * d)
                    min_val[i][j] = min(min_val[i][j], a * b, a * d, c * b, c * d)

    return max_val[0][-1]

with open ('input.txt', 'r') as file:
    expr = file.readline().strip()

start_time = time.perf_counter()

result = max_expr_value(expr)

current, peak = tracemalloc.get_traced_memory()
end_time = time.perf_counter()

with open ('output.txt', 'w') as file:
    file.write(str(result))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")