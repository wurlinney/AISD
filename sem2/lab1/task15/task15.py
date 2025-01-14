import tracemalloc
import time

tracemalloc.start()

def bracket_seq(s):
    n = len(s)

    if n < 2:
        return ""

    dp = [[0] * n for _ in range(n)]
    matching = {')': '(', ']': '[', '}': '{'}

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] in "([{":
                if s[j] in ")]}" and matching[s[j]] == s[i]:
                    dp[i][j] = dp[i + 1][j - 1] + 2

            for k in range(i, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k + 1][j])

    i, j = 0, n - 1
    result = []
    while i <= j:
        if s[i] in "([{":
            if s[j] in ")]}" and matching.get(s[j]) == s[i]:
                result.append(s[i])
                result.append(s[j])
                i += 1
                j -= 1
            else:
                if dp[i + 1][j] >= dp[i][j - 1]:
                    i += 1
                else:
                    j -= 1
        else:
            i += 1

    return ''.join(result)




with open ('input.txt', 'r') as file:
    s = file.readline().strip()

start_time = time.perf_counter()

results = bracket_seq(s)

current, peak = tracemalloc.get_traced_memory()
end_time = time.perf_counter()

with open ('output.txt', 'w') as file:
    file.write(results)

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")