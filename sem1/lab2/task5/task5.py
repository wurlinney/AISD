import time
import tracemalloc

tracemalloc.start()


def majority(arr):
    n = len(arr)
    if n == 1:
        return 1, arr[0]
    mid = n // 2
    left_result, left_majority = majority(arr[:mid])
    right_result, right_majority = majority(arr[mid:])
    if left_result == 0 and right_result == 0:
        return 0, None
    if left_majority == right_majority:
        return 1, left_majority
    left_count = sum(1 for element in arr if element == left_majority)
    right_count = sum(1 for element in arr if element == right_majority)
    if left_count > n // 2:
        return 1, left_majority
    if right_count > n // 2:
        return 1, right_majority
    return 0, None

with open('input.txt', 'r') as f:
    n = int(f.readline())
    a = [int(x) for x in f.readline().split()]

start_time = time.perf_counter()

result, _ = majority(a)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as f:
    f.write(f"{result}\n")

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
