import time
import tracemalloc

tracemalloc.start()

def decomposition(s):
    n = len(s)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    parts = [''] * (n + 1)

    for i in range(n + 1):
        if dp[i] == float('inf'):
            continue
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            length = j - i
            count = 1
            k = j
            while k + length <= n and s[k:k+length] == substring:
                k += length
                count += 1
            representation = f"{substring}*{count}" if count > 1 else substring
            if dp[i] + len(representation) < dp[k]:
                dp[k] = dp[i] + len(representation)
                parts[k] = (parts[i] + ('+' if parts[i] else '') + representation) if parts[i] else representation

    return parts[n]

with open('input.txt', 'r') as file:
    s = file.readline().strip()

start_time = time.perf_counter()

result = decomposition(s)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as file:
    file.write(result)


print(f"Затраты памяти: {current / 10**6}MB; Пиковое использование: {peak / 10**6 } MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")