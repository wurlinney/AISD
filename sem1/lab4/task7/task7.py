import time
import tracemalloc
from collections import deque

tracemalloc.start()


def sliding_window_maximum(n, arr, m):
    dq = deque()
    result = []
    for i in range(n):
        if dq and dq[0] < i - m + 1:
            dq.popleft()
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        dq.append(i)
        if i >= m - 1:
            result.append(arr[dq[0]])

    return result

with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    arr = list(map(int, f.readline().strip().split()))
    m = int(f.readline().strip())

start_time = time.perf_counter()

result = sliding_window_maximum(n, arr, m)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as f:
    f.write(" ".join(map(str, result)))

print(f"Затраты памяти: {current / 10**6} MB; Пиковое использование: {peak / 10**6 } MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")