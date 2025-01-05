import tracemalloc
import time

tracemalloc.start()

def insertion_sort(array):
    for i in range(1, n):
        x = array[i]
        j = i

        while j > 0 and array[j - 1] > x:
            array[j] = array[j - 1]
            j -= 1

        array[j] = x

    return array
start_time = time.perf_counter()
with open('input_1.txt') as input_f:
    n = int(input_f.readline())
    a = [int(x) for x in input_f.readline().split()]

sorted_array = insertion_sort(a)
with open('output_1.txt', 'w') as output_f:
    output_f.write(" ".join(map(str, sorted_array)))

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()
print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
