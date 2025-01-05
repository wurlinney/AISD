import tracemalloc
import time

tracemalloc.start()

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    element = arr[0]
    less = [x for x in arr[1:] if x <= element]
    greater = [x for x in arr[1:] if x > element]

    return quick_sort(less) + [element] + quick_sort(greater)

with open("input.txt", "r") as file:
    n = int(file.readline().strip())
    arr = list(map(int, file.readline().strip().split()))

start_time = time.perf_counter()

sorted_arr = quick_sort(arr)

current, peak = tracemalloc.get_traced_memory()
end_time = time.perf_counter()

with open("output.txt", "w") as file:
    file.write(" ".join(map(str, sorted_arr)))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
