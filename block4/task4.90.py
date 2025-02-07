from math import sin, radians
x = int(input("Введите число x: "))
if sin(radians(x)) >= 0:
    k = x ** 2
elif sin(radians(x)) < 0:
    k = abs(x)
else:
    print("Вы как это сделали???")
if x < k:
    print(f"f = {abs(x)}")
elif x >= k:
    print(f"f = {k * x}")
else:
    print("Не то вводите")
