import tracemalloc
import time

tracemalloc.start()

class HashMap:
    def __init__(self, size=100003):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.order = []

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        table = self.table[index]
        for i, (k, v) in enumerate(table):
            if k == key:
                table[i] = (key, value)
                return
        table.append((key, value))
        self.order.append(key)

    def get(self, key):
        index = self._hash(key)
        table = self.table[index]
        for k, v in table:
            if k == key:
                return v
        return "<none>"

    def delete(self, key):
        index = self._hash(key)
        table = self.table[index]
        for i, (k, v) in enumerate(table):
            if k == key:
                del table[i]
                self.order.remove(key)
                return

    def prev(self, key):
        if key not in self.order:
            return "<none>"
        index = self.order.index(key)
        if index > 0:
            prev_key = self.order[index - 1]
            return self.get(prev_key)
        return "<none>"

    def next(self, key):
        if key not in self.order:
            return "<none>"
        index = self.order.index(key)
        if index < len(self.order) - 1:
            next_key = self.order[index + 1]
            return self.get(next_key)
        return "<none>"


def op_manager(operations):
    result = []
    hash_map = HashMap()
    for operation in operations:
        parts = operation.strip().split()
        command = parts[0]

        if command == "put":
            key, value = parts[1], parts[2]
            hash_map.put(key, value)
        elif command == "get":
            key = parts[1]
            result.append(hash_map.get(key))
        elif command == "delete":
            key = parts[1]
            hash_map.delete(key)
        elif command == "prev":
            key = parts[1]
            result.append(hash_map.prev(key))
        elif command == "next":
            key = parts[1]
            result.append(hash_map.next(key))

    return result

with open('input.txt', 'r') as f:
    n = int(f.readline())
    operations = [f.readline().strip() for _ in range(n)]

start_time = time.perf_counter()

result = op_manager(operations)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()


with open('output.txt', 'w') as f:
    f.write('\n'.join(result) + '\n')

print(f"Затраты памяти: {current / 10 ** 6:.6f} MB; Пиковое использование: {peak / 10 ** 6:.6f} MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")