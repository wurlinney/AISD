import time
import tracemalloc
from collections import deque

tracemalloc.start()


def queue(commands):
    q = deque()
    result = []
    for command in commands:
        if command.startswith('+'):
            x = command.split()[1]
            q.append(x)
        elif command.startswith('-'):
            if q:
                result.append(q.popleft())
    return result


with open('input.txt', 'r') as f:
    n = int(f.readline())
    commands = f.readlines()

start_time = time.perf_counter()

result = queue(commands)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as f:
    f.write("\n".join(str(element) for element in result))

print(f"Затраты памяти: {current / 10**6}MB; Пиковое использование: {peak / 10**6 }MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
