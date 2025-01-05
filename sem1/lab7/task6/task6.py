import tracemalloc
import time

tracemalloc.start()

def max_increasing_seq(n, A):
    table = [1] * n
    parent = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if A[i] > A[j] and table[i] < table[j] + 1:
                table[i] = table[j] + 1
                parent[i] = j
    max_length = max(table)
    max_index = table.index(max_length)
    result = []
    while max_index != -1:
        result.append(A[max_index])
        max_index = parent[max_index]
    result.reverse()
    return max_length, result


with open('input.txt', 'r') as file:
    n = int(file.readline())
    A = list(map(int, file.readline().strip().split()))

start_time = time.perf_counter()

length, max_sequence = max_increasing_seq(n, A)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()



with open('output.txt', 'w') as file:
    file.write(str(length) + '\n')
    file.write(' '.join(map(str, max_sequence)))


print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
