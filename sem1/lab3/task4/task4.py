import tracemalloc
import time

tracemalloc.start()

def points_counter(p, sections, points):
    section_info = []
    counter = 0
    result = [0] * p
    for section in sections:
        section_info.append([section[0], "start"])
        section_info.append([section[1], "end"])
    for i, point in enumerate(points):
        section_info.append([point, "point", i])
    section_info.sort(key=lambda x: (x[0], x[1] == "end", x[1] == "point"))
    for element in section_info:
        if element[1] == 'start':
            counter += 1
        elif element[1] == 'end':
            counter -= 1
        else:
            result[element[2]] = counter
    return result

with open("input.txt", "r") as file:
    s, p = map(int, file.readline().split())
    sections = [list(map(int, file.readline().split())) for i in range(s)]
    points = list(map(int, file.readline().split()))


start_time = time.perf_counter()

result = points_counter(p, sections, points)

current, peak = tracemalloc.get_traced_memory()
end_time = time.perf_counter()

with open("output.txt", "w") as file:
    file.write(" ".join(map(str, result)))

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
