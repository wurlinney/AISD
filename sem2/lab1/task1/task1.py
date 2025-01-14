import tracemalloc
import time

tracemalloc.start()


def find_max_cost(n, w, items):
    max_cost = 0
    remaining_capacity = w
    items.sort(key=lambda x: x[0] / x[1] if x[1] != 0 else 0, reverse=True)
    for cost, weight in items:
        if remaining_capacity >= weight:
            max_cost += cost
            remaining_capacity -= weight
        else:
            max_cost += cost * (remaining_capacity / weight)
            break

    return round(max_cost, 4)


with open ('input.txt', 'r') as file:
    n, с = map(int, file.readline().strip().split())
    items = []
    for _ in range(n):
        p, w = map(int, file.readline().split())
        items.append((p, w))


start_time = time.perf_counter()

result = find_max_cost(n, с, items)

current, peak = tracemalloc.get_traced_memory()
end_time = time.perf_counter()

with open ('output.txt', 'w') as file:
    file.write(f"{result:.4f}\n")

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")