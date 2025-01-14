import tracemalloc
import time

tracemalloc.start()

def knight_number(n):
    dp = [[0] * 10 for i in range(n + 1)]

    for digit in range(10):
        if digit != 0 and digit != 8:
            dp[1][digit] = 1

    for length in range(2, n + 1):
        for digit in range(10):
            dp[length][digit] = sum(dp[length - 1][prev] for prev in moves[digit]) % MOD

    result = sum(dp[n][digit] for digit in range(10)) % MOD
    return result


MOD = 10**9

moves = {
    0: [4, 6],
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [0, 3, 9],
    5: [],
    6: [0, 1, 7],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4]
}

with open ('input.txt', 'r') as file:
    n = int(file.readline())

start_time = time.perf_counter()

result = knight_number(n)

current, peak = tracemalloc.get_traced_memory()
end_time = time.perf_counter()

with open ('output.txt', 'w') as file:
    file.write(str(result))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")