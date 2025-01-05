import tracemalloc
import time

tracemalloc.start()

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return int(key) % self.size

    def add(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def delete(self, key):
        index = self._hash(key)
        self.table[index] = [(k, v) for k, v in self.table[index] if k != key]

    def find(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return "not found"

def phone_manager(operations):
    hash_table = HashTable(size=100003)
    result = []
    for operation in operations:
        parts = operation.split()
        command = parts[0]
        number = int(parts[1])

        if command == "add":
            name = parts[2]
            hash_table.add(number, name)
        if command == "del":
            hash_table.delete(number)
        if command == "find":
            name = hash_table.find(number)
            result.append(name)
    return result

with open('input.txt', 'r') as f:
    n = int(f.readline())
    operations = [f.readline().strip() for _ in range(n)]

start_time = time.perf_counter()

result = phone_manager(operations)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()


with open('output.txt', 'w') as f:
    f.write('\n'.join(result) + '\n')

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")



