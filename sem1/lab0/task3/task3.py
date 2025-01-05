import time
from memory_profiler import memory_usage
memory_usage_before = memory_usage()[0]
t_start = time.perf_counter()
with open('input_4.txt', 'r') as input_f:
    n = int(input_f.readline())
a, b = 0, 1
if n == 0:
    last_digit = a
else:
    for i in range(2, n + 1):
        a, b = b % 10, (a + b) % 10
    last_digit = b
with open('output_4.txt', 'w') as output_f:
    output_f.write(str(last_digit))

memory_usage_mb = (memory_usage()[0] - memory_usage_before) * 1.048576

print(f"Время выполнения {time.perf_counter() - t_start} секунд")
print(f"Объем использованной памяти {memory_usage_mb} Мб")