import time
import tracemalloc


tracemalloc.start()


def insertion_sort_reverse(array):
    for i in range(1, n):
        x = array[i]
        j = i
        while j > 0 and array[j - 1] < x:
            array[j], array[j-1] = swap(array[j], array[j-1])
            j -= 1
        array[j] = x
    return array

def swap(x, y):
    temp = x
    x = y
    y = temp
    return x, y

with open('input.txt', 'r') as f:
    n = int(f.readline())
    a = [int(x) for x in f.readline().split()]

start_time = time.perf_counter()

sorted_array = insertion_sort_reverse(array=a)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as f:
    f.write(" ".join(map(str, sorted_array)))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")

