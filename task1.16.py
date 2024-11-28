from math import sin, cos

x = int(input("Введите число x: "))
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))
R = 8.31
d = int(input("Введите число d: "))

print(f"a) a / b / c = {round(a / b / c, 2)}")
print(f"б) a * b / c = {round(a * b / c, 2)}")
print(f"в) a / b * c = {round(a / b * c, 2)}")
print(f"г) a + (b / c) = {round(a + (b / c), 2)}")
print(f"д) (a + b) / c = {round(a + b / c, 2)}")
print(f"е) a + b / b + c = {round(a + b / b + c, 2)}")
print(f"ж) (a + b) / (b + c) = {round((a + b) / (b + c), 2)}")
print(f"з) a / sin(b) = {round(a / sin(b), 2)}")
print(f"и) 1 / 2 * a * b * sin(x) = {round(1 / 2 * a * b * sin(x), 2)}")
print(f"к) 2 * b * c * cos(a / 2) / b + c \
       = {round(2 * b * c * cos(a / 2) / b + c, 2)}")
print(f"л) 4 * R * sin(a / 2) * sin(b / 2) * sin(c / 2) \
       = {round(4 * R * sin(a / 2) * sin(b / 2) * sin(c / 2), 2)}")
print(f"м) (a * x + b) / (c * x + d) = {round((a * x + b) / (c * x + d), 2)}")
print(f"н) 2 * sin(a + b) / 2 * cos(a - b) / 2 \
      = {round(2 * sin(a + b) / 2 * cos(a - b) / 2, 2)}")
print(f"о) abs(2) * sin(-3) * abs(x / 2) \
      = {round(abs(2) * sin(-3) * abs(x / 2), 2)}")
