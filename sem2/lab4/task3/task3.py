import time
import tracemalloc

tracemalloc.start()

def rabin_karp(pattern, text):
    pattern_len = len(pattern)
    text_len = len(text)
    if text_len < pattern_len:
        return []
    result = []
    pattern_hash = hash(pattern)
    for i in range(0, text_len - pattern_len + 1):
        subtext = text[i:i + pattern_len]
        if hash(subtext) == pattern_hash and subtext == pattern:
            result.append(i + 1)
    return result


with open('input.txt', 'r') as f:
    pattern = f.readline().strip()
    s = f.readline().strip()

start_time = time.perf_counter()

result = rabin_karp(pattern, s)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as f:
    f.write(str(len(result)) + '\n')
    f.write(' '.join(map(str, result)))

print(f"Затраты памяти: {current / 10**6}MB; Пиковое использование: {peak / 10**6 } MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")