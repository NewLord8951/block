a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
if (a ** 0.5) > (b ** 0.5):
    c = b * 2
    print("Второе число теперь равно: ", c)
else:
    print("Нет, корень первого числа меньше корень второго")
