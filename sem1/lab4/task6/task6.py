import time
import tracemalloc
from collections import deque

tracemalloc.start()


def queue_with_min(commands):
    queue = deque()
    min_queue = deque()
    result = []
    for command in commands:
        if command.startswith('+'):
            x = command.split()[1]
            queue.append(x)
            while min_queue and min_queue[-1] > x:
                min_queue.pop()
            min_queue.append(command.split()[1])
        elif command.startswith('-'):
            if queue:
                removed = queue.popleft()
                if removed == min_queue[0]:
                    min_queue.popleft()

        elif command.startswith('?'):
            if min_queue:
                result.append(min_queue[0])
            else:
                result.append(None)
    return result


with open('input.txt', 'r') as f:
    n = int(f.readline())
    commands = f.readlines()

start_time = time.perf_counter()

result = queue_with_min(commands)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as f:
    f.write("\n".join(str(element) for element in result))

print(f"Затраты памяти: {current / 10**6}MB; Пиковое использование: {peak / 10**6 }MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
