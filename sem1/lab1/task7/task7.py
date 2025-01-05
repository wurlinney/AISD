import time
import tracemalloc

tracemalloc.start()


def bubble_sort(array, n):
    for i in range(0, n-1):
        for j in range(0, n-1-i):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
    return array


with open('input.txt', 'r') as f:
    n = int(f.readline())
    a = [float(x) for x in f.readline().split()]

start_time = time.perf_counter()

sorted_array = bubble_sort(array=a.copy(), n=n)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as f:
    f.write(f"{a.index(sorted_array[0]) + 1} {a.index(sorted_array[n // 2]) + 1} {a.index(sorted_array[-1]) + 1}")

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")



