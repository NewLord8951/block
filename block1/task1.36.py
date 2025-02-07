from math import pi
r1 = int(input("Введите внешний радиус: "))
r2 = int(input("Введите внутрений радиус: "))
s = round(pi * ((r1 ** 2) - (r2 ** 2)), 2)
print("Площадь = ", s)
