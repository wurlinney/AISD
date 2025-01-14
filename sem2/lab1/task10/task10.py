import tracemalloc
import time

tracemalloc.start()

def apples_count(n, s, apples):
    eaten_apples = []
    for i in range(n):
        for j in range(n):
            if s > 0 and apples[j][0] <= s:
                eaten_apples.append(j + 1)
                s -= apples[j][0]
                s += apples[j][1]
                apples[j] = (float('inf'), float('inf'))
                break
        else:
            return -1
    return eaten_apples


with open ('input.txt', 'r') as file:
    n, s = map(int, file.readline().split())
    apples = [tuple(map(int, line.split())) for line in file]


start_time = time.perf_counter()

result = apples_count(n, s, apples)

current, peak = tracemalloc.get_traced_memory()
end_time = time.perf_counter()

with open ('output.txt', 'w') as file:
    if result == -1:
        file.write(str(result))
    else:
        file.write(' '.join(map(str, result)))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")