def find_min_negative_element():
    # Введення розміру масиву
    try:
        n = int(input("Введіть кількість елементів масиву (N): "))
        if n <= 0:
            print("Кількість елементів має бути більшою за нуль.")
            return
    except ValueError:
        print("Будь ласка, введіть ціле число для N.")
        return

    # Введення елементів масиву
    print("Введіть елементи масиву (дійсні числа):")
    try:
        array = [float(input(f"Елемент {i + 1}: ")) for i in range(n)]
    except ValueError:
        print("Будь ласка, вводьте тільки дійсні числа.")
        return

    # Пошук мінімального від'ємного елемента
    negative_elements = [num for num in array if num < 0]
    if negative_elements:
        min_negative = min(negative_elements)
        print(f"Мінімальний від’ємний елемент: {min_negative}")
    else:
        print("У масиві немає від’ємних елементів.")


# Виклик функції
find_min_negative_element()
