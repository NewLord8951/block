def find_max_min_indices(numbers):
    if not numbers:
        return -1, -1

    # Инициализация
    max_num = min_num = numbers[0]
    max_index = min_index = 0

    # Поиск индексов
    for i, num in enumerate(numbers):
        if num > max_num:
            max_num = num
            max_index = i
        if num < min_num:
            min_num = num
            min_index = i

    return max_index, min_index


numbers = [5, 3, 8, 3, 8, 2]
max_index, min_index = find_max_min_indices(numbers)
print(f"Номер последнего максимального числа: {max_index}")
print(f"Номер первого минимального числа: {min_index}")
