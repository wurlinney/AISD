import time
import tracemalloc

tracemalloc.start()

def compute_z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z

def z_search(p, t):
    s = p + '$' + t
    z = compute_z_function(s)
    len_p = len(p)
    occurrences = []
    for i in range(len_p + 1, len(s)):
        if z[i] == len_p:
            occurrences.append(i - len_p)
    return occurrences


with open('input.txt', 'r') as file:
    p = file.readline().strip()
    t = file.readline().strip()

start_time = time.perf_counter()

result = z_search(p, t)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()


with open('output.txt', 'w') as file:
    file.write(f"{len(result)}\n")
    if result:
        file.write(" ".join(map(str, result)) + "\n")

print(f"Затраты памяти: {current / 10**6}MB; Пиковое использование: {peak / 10**6 } MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
