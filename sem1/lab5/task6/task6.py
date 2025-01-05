import heapq
import tracemalloc
import time

tracemalloc.start()

def queue_plus(operations):
    min_heap = []
    added_elements = {}
    element_indices = {}
    results = []

    for i, operation in enumerate(operations):
        operation_parts = operation.strip().split()
        command = operation_parts[0]

        if command == 'A':
            x = int(operation_parts[1])
            heapq.heappush(min_heap, x)
            added_elements[i + 1] = x
            if x not in element_indices:
                element_indices[x] = []
            element_indices[x].append(i + 1)

        elif command == 'X':
            if min_heap:
                min_el = heapq.heappop(min_heap)
                results.append(str(min_el))
                if min_el in element_indices:
                    element_indices[min_el].pop(0)
                    if not element_indices[min_el]:
                        del element_indices[min_el]
            else:
                results.append('*')

        elif command == 'D':
            x = int(operation_parts[1])
            y = int(operation_parts[2])

            if x in added_elements:
                prev_value = added_elements[x]
                if prev_value in min_heap:
                    min_heap.remove(prev_value)
                    heapq.heapify(min_heap)
                    heapq.heappush(min_heap, y)

                    added_elements[x] = y
                    if prev_value in element_indices:
                        element_indices[prev_value].remove(x)
                        if not element_indices[prev_value]:
                            del element_indices[prev_value]
                    if y not in element_indices:
                        element_indices[y] = []
                    element_indices[y].append(x)

    return results


with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    operations = [f.readline().strip() for _ in range(n)]

start_time = time.perf_counter()


result = queue_plus(operations)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()


with open('output.txt', 'w') as f:
    f.write("\n".join(result))


print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
