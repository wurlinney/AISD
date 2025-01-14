import time
import tracemalloc

tracemalloc.start()

def palindromics_count(message):
    message = message.replace(' ', '')
    n = len(message)
    prefix_count = [0] * 26
    suffix_count = [0] * 26
    for char in message:
        suffix_count[ord(char) - ord('a')] += 1
    total_triplets = 0
    for i in range(n):
        current_char = message[i]
        suffix_count[ord(current_char) - ord('a')] -= 1

        if i > 0:
            for j in range(26):
                total_triplets += prefix_count[j] * suffix_count[j]

        prefix_count[ord(current_char) - ord('a')] += 1
    return total_triplets



with open('input.txt', 'r') as file:
    message = file.readline().strip()

start_time = time.perf_counter()

result = palindromics_count(message)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as file:
    file.write(str(result))

print(f"Затраты памяти: {current / 10**6}MB; Пиковое использование: {peak / 10**6 } MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
