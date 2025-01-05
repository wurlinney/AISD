import tracemalloc
import time

tracemalloc.start()

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    element = arr[0]
    less = [x for x in arr[1:] if x < element]
    equal = [x for x in arr if x == element]
    greater = [x for x in arr[1:] if x > element]

    return quick_sort(less) + equal + quick_sort(greater)

def h_index(citations):
    n = len(citations)
    sorted_citations = quick_sort(citations)
    index_h = 0
    for i in range (n-1, -1, -1):
        if sorted_citations[i] >= index_h + 1:
            index_h += 1
            continue
        break
    return index_h

with open ('input.txt', 'r') as file:
    citations = list(map(int, file.read().strip().replace(',', ' ').split()))

start_time = time.perf_counter()

result = h_index(citations)

current, peak = tracemalloc.get_traced_memory()
end_time = time.perf_counter()

with open ('output.txt', 'w') as file:
    file.write(str(result))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")