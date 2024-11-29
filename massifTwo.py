# Розмір масиву
size = 7

# Створюємо масив 7x7, заповнений нулями
array = [[0 for _ in range(size)] for _ in range(size)]

# Заповнюємо масив згідно з умовою
for i in range(size):
    for j in range(size - i):
        array[i][j + i] = size - j

# Виводимо масив у потрібному форматі
for row in array:
    print(" ".join(map(str, row)))
