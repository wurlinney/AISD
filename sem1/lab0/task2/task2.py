import time
from memory_profiler import memory_usage
memory_usage_before = memory_usage()[0]
t_start = time.perf_counter()
with open('input_3.txt', 'r') as input_f:
    n = int(input_f.readline())
    a, b = 0, 1
    i = 0
    while i < n:
        a, b = b, a + b
        i += 1

with open('output_3.txt', 'w') as output_f:
    output_f.write(str(a))
memory_usage_mb = (memory_usage()[0] - memory_usage_before) * 1.048576

print(f"Время выполнения {time.perf_counter() - t_start} секунд")
print(f"Объем использованной памяти {memory_usage_mb} Мб")