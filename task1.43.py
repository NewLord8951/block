num1 = int(input("Введите num1: "))
num2 = int(input("Введите num2: "))

arithmetic_mean = abs((num1 + num2) / 2)
print(arithmetic_mean)

geometric_mean = abs(round((num1 * num2) ** 0.5, 2))
print(geometric_mean)
