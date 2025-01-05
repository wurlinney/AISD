import time
import tracemalloc

tracemalloc.start()

OPEN = ('(', '[')
CLOSE = (')', ']')


def check_staples(staples_list):
    result = []
    for string in staples_list:
        string = string.strip()
        is_valid = True
        stack = []
        for s1 in string:
            if s1 in OPEN:
                stack.append(s1)
            elif s1 in CLOSE:
                if not stack:
                    is_valid = False
                    break
                s2 = stack.pop()
                if s2 == "(" and s1 != ")":
                    is_valid = False
                    break
                if s2 == "[" and s1 != "]":
                    is_valid = False
                    break
        if stack:
            is_valid = False
        result.append("YES" if is_valid else "NO")
    return result


with open('input.txt', 'r') as f:
    n = int(f.readline())
    staples_list = f.readlines()

start_time = time.perf_counter()

result = check_staples(staples_list)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as f:
    f.write("\n".join(str(element) for element in result))

print(f"Затраты памяти: {current / 10**6}MB; Пиковое использование: {peak / 10**6 }MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
