import heapq
import time
import tracemalloc

tracemalloc.start()

def task_scheduler(n, task_times):
    thread_heap = [(0, i) for i in range(n)]
    heapq.heapify(thread_heap)
    result = []

    for task_time in task_times:
        current_time, thread_index = heapq.heappop(thread_heap)
        result.append((thread_index, current_time))
        heapq.heappush(thread_heap, (current_time + task_time, thread_index))

    return result



with open('input.txt', 'r') as f:
    n, m = map(int, f.readline().strip().split())
    task_times = list(map(int, f.readline().strip().split()))

start_time = time.perf_counter()

result = task_scheduler(n, task_times)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as f:
    for thread_index, pr_start_time in result:
        f.write(f"{thread_index} {pr_start_time}\n")

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
