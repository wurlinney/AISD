import tracemalloc
import time

tracemalloc.start()

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def add(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, v + value)
                return
        self.table[index].append((key, value))

    def get_all(self):
        candidates = {}
        for chain in self.table:
            for k, v in chain:
                candidates[k] = v
        return candidates


def elections(lines):
    hash_table = HashTable(size=100003)
    for line in lines:
        parts = line.strip().split()
        candidate = parts[0]
        votes = int(parts[1])
        hash_table.add(candidate, votes)
    result = hash_table.get_all()
    final_result = sorted(result.items())
    return final_result

with open('input.txt', 'r') as file:
    lines = file.readlines()

start_time = time.perf_counter()

result = elections(lines)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as file:
    for candidate, votes in result:
        file.write(f"{candidate} {votes}\n")

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")