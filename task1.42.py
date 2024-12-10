from math import sin, radians


e = int(input("Введите e: "))
f = int(input("Введите f: "))
g = int(input("Введите g: "))
h = int(input("Введите h: "))
a = round((e + (f / 2)) / 3, 2)
b = round(abs((h ** 2) - g), 2)
c = round((((g - h) ** 2) - (3 * sin(radians(e))) ** 0.5), 2)
print("a =", a)
print("b =", b)
print("c =", c)
