import tracemalloc
import time
import sys

sys.set_int_max_str_digits(5000)

tracemalloc.start()

def is_fibonacci(n, fib_set):
    return n in fib_set

def generate_fibonacci_up_to_limit(limit):
    fib_set = set()
    a, b = 1, 1
    fib_set.add(a)
    fib_set.add(b)
    while b <= limit:
        a, b = b, a + b
        fib_set.add(b)
    return fib_set


with open('input.txt', 'r') as f:
    n = int(f.readline())
    numbers = [int(f.readline().strip()) for _ in range(n)]

start_time = time.perf_counter()

max_limit = 10 ** 5000
fib_set = generate_fibonacci_up_to_limit(max_limit)
result = ["Yes" if is_fibonacci(num, fib_set) else "No" for num in numbers]

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as f:
    f.write("\n".join(result))


print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")


