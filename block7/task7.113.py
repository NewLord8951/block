numbers_input = input("Введите 9 вещественных чисел через пробел: ")

total_sum = 0
count = 0

for number_str in numbers_input.split():
    number = float(number_str)
    if number > 10:
        total_sum += number
        count += 1

if count > 0:
    average = total_sum / count
    print(f"Среднее арифметическое чисел, больших 10: {average:.2f}")
else:
    print("Нет чисел, больших 10.")
