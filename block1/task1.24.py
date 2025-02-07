from math import sin

a = float(input("Введите дробное число a: "))
x = float(input("Введите дробное число x: "))

# а)
x = (((2 * a) + sin(abs(5 * x))) / 3.56) ** 0.5
print(x)

# б)
y = sin(3.2 + ((1 + x) ** 0.5) / abs(5 * x))
print(y)
