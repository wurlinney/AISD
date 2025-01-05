import time
import tracemalloc

tracemalloc.start()

def binary_search(arr, item):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (right + left) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > item:
            right = mid - 1
        else:
            left = mid + 1
    return -1


with open('input.txt', 'r') as f:
    n = int(f.readline())
    a = [int(x) for x in f.readline().split()]
    k = int(f.readline())
    b = [int(x) for x in f.readline().split()]

start_time = time.perf_counter()

result = [binary_search(arr=a, item=item) for item in b]

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as f:
    f.write(' '.join(map(str, result)))

print(f"Затраты памяти: {current / 10**6}MB; Пиковое использование: {peak / 10**6 }MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")


