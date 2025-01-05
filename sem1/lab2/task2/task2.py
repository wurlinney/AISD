import time
import tracemalloc

merge_steps = []


def split_and_merge(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = split_and_merge(left)
    right = split_and_merge(right)

    return merge(left, right)


def merge(a, b):
    global merge_steps
    result = []
    i = 0
    j = 0
    I_f = 1
    I_l = I_f + len(a) + len(b)

    V_f = a[0] if a else b[0]
    V_l = b[-1] if b else a[-1]

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result += a[i:] + b[j:]

    merge_steps.append((I_f, I_l, V_f, V_l))
    return result


with open('input.txt', 'r') as f:
    n = int(f.readline())
    a = [int(x) for x in f.readline().split()]

start_time = time.perf_counter()
tracemalloc.start()

sorted_list = split_and_merge(a)

current, peak = tracemalloc.get_traced_memory()
end_time = time.perf_counter()

with open('output.txt', 'w') as f:
    for step in merge_steps:
        f.write(f"{step[0]} {step[1]} {step[2]} {step[3]}\n")
    f.write(" ".join(map(str, sorted_list)))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
