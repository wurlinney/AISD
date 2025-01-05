import time
from memory_profiler import memory_usage

t_start = time.perf_counter()
memory_usage_before = memory_usage()[0]
with open('input_1.txt', 'r') as input_f:
    a, b = map(int, input_f.readline().split())

with open('output_1.txt', 'w') as output_f:
    output_f.write(str(a+b))

memory_usage_mb = (memory_usage()[0] - memory_usage_before) * 1.048576

print(f"Время выполнения {time.perf_counter() - t_start} секунд")
print(f"Объем использованной памяти {memory_usage_mb} Мб")