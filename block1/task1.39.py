from math import sin
x = int(input("Введите x: "))
y = int(input("Введите y: "))
z = round(
    (x + (((2 * x) + y) / (x ** 2))) / (y + (1 / (((x ** 2) + 10) ** 0.5))), 2)
q = round(2.8 * sin(x) + abs(y), 2)
print("z = ", z)
print("q = ", q)
