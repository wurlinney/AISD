import tracemalloc
import time

tracemalloc.start()

class HashSet:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key):
        index = self._hash(key)
        if key not in self.table[index]:
            self.table[index].append(key)

    def delete(self, key):
        index = self._hash(key)
        self.table[index] = [k for k in self.table[index] if k != key]

    def find(self, key):
        index = self._hash(key)
        return key in self.table[index]

def set_ops(operations):
    hash_set = HashSet(size=100003)
    result = []


    for operation in operations:
        parts = operation.split()
        command = parts[0]
        x = int(parts[1])

        if command == 'A':
            hash_set.add(x)
        elif command == 'D':
            hash_set.delete(x)
        elif command == '?':
            result.append('Y' if hash_set.find(x) else 'N')
    return result


with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    operations = [f.readline().strip() for _ in range(n)]

start_time = time.perf_counter()

results = set_ops(operations)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()


with open('output.txt', 'w') as f:
    f.write('\n'.join(results) + '\n')

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
