def generate_input_file(filename, n):
    with open(filename, 'w') as f:
        f.write(f"{n}\n")  # Количество вершин
        for i in range(1, n + 1):
            key = i  # Уникальные ключи от 1 до n
            left_child = 0  # Левого ребенка нет
            right_child = i + 1 if i < n else 0  # Правый ребенок — следующая вершина
            f.write(f"{key} {left_child} {right_child}\n")

# Максимальное количество вершин
n = 2 * 10**5

# Генерация файла
generate_input_file('input.txt', n)

print(f"Файл 'input.txt' с {n} вершинами успешно создан.")