import time
import tracemalloc

tracemalloc.start()

def stack_operations(commands):
    stack = []
    deleted_elements = []
    for command in commands:
        command = command.strip()
        if command == '-':
            if stack:
                deleted_elements.append(stack.pop())
        elif command.startswith('+'):
            try:
                stack.append(int(command.split()[1]))
            except (IndexError, ValueError):
                print(f"Ошибка: некорректная команда {command}")
                continue
    return deleted_elements


with open('input.txt', 'r') as file:
    lines = file.readlines()
    commands = lines[1:]

start_time = time.perf_counter()

result = stack_operations(commands)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()


with open('output.txt', 'w') as file:
    for element in result:
        file.write(str(element) + '\n')

print(f"Затраты памяти: {current / 10**6}MB; Пиковое использование: {peak / 10**6 }MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
