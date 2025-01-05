import time
import tracemalloc

tracemalloc.start()

def selection_sort(array, n):
    for i in range(n-1):
        x = array[i]
        position = i
        for j in range(i + 1, n):
            if array[j] < x:
                x = array[j]
                position = j
        if position != i:
            array[i], array[position] = swap(array[i], array[position])
    return array

def swap(x,y):
    temp = x
    x = y
    y = temp
    return x,y


with open('input.txt', 'r') as f:
    n = int(f.readline())
    a = [int(x) for x in f.readline().split()]

start_time = time.perf_counter()

sorted_array = selection_sort(a, n)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as f:
    f.write(" ".join(map(str, sorted_array)))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")