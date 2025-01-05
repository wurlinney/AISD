import tracemalloc
import time

tracemalloc.start()

def find_v(array, v):
    v_nums = []
    for i in range(0, len(array)):
        if array[i] == v:
            v_nums.append(i)
    if not v_nums:
        return -1
    return f'{len(v_nums)}\n{','.join(map(str, v_nums))}'

start_time = time.perf_counter()

with open ('input_3.txt', 'r') as input_f:
    array = [int(x) for x in input_f.readline().split()]
    v = int(input_f.readline())

with open('output_3.txt', 'w') as output_f:
    output_f.write(str(find_v(array, v)))

end_time = time.perf_counter()

current, peak = tracemalloc.get_traced_memory()
print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
















