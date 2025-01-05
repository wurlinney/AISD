import tracemalloc
import time

tracemalloc.start()

def insertion_sort(array, n):
    indices = list(range(1, n + 1))
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        indices[i] = j + 2

    return array, indices


start_time = time.perf_counter()
with open('input_2.txt') as input_f:
    n = int(input_f.readline())
    a = [int(x) for x in input_f.readline().split()]

sorted_array, indices = insertion_sort(a, n)

with open('output_2.txt', 'w') as output_f:
    output_f.write(" ".join(map(str, indices)) + "\n")
    output_f.write(" ".join(map(str, sorted_array)) + "\n")

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()
print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")