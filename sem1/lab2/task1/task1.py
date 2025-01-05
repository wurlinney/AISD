import time
import tracemalloc

tracemalloc.start()


def split_and_merge(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    if len(left) > 1:
        left = split_and_merge(left)
    if len(right) > 1:
        right = split_and_merge(right)
    return merge(left, right)

def merge(a, b):
    result = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result += a[i:] + b[j:]
    return result


with open('input.txt', 'r') as f:
    n = int(f.readline())
    a = [int(x) for x in f.readline().split()]

start_time = time.perf_counter()

sorted_list = split_and_merge(arr=a)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as f:
    f.write(str(sorted_list))

print(f"Затраты памяти: {current / 10**6}MB; Пиковое использование: {peak / 10**6 }MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
