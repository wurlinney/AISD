import time
import tracemalloc

tracemalloc.start()


def postfix(equation):
    elements = equation.split()
    stack = []
    for element in elements:
        if element == '+':
            summ = stack.pop() + stack.pop()
            stack.append(summ)
        elif element == '*':
            product = stack.pop() * stack.pop()
            stack.append(product)
        elif element == '-':
            diff = (stack.pop() - stack.pop()) * -1
            stack.append(diff)
        else:
            stack.append(int(element))
    return stack.pop()


with open('input.txt', 'r') as f:
    n = int(f.readline())
    equation = f.readline().strip()

start_time = time.perf_counter()

result = postfix(equation)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

with open('output.txt', 'w') as f:
    f.write(str(result))

print(f"Затраты памяти: {current / 10**6} MB; Пиковое использование: {peak / 10**6 } MB")
print(f"Время выполнения программы: {end_time - start_time:.6f} секунд")
