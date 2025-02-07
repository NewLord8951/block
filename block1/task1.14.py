from math import sin, radians, sqrt, cos

x = int(input("Введите число x:"))
y = int(input("Введите число y:"))
a = int(input("Введите число a:"))
n = int(input("Введите число n:"))
b = int(input("Введите число b:"))

print(f"a) 2 * x = {2 * x}")
print(f"б) sin(x) = {round(sin(radians(x)), 2)}")
print(f"в) a * a = {a * a}")
print(f"г) sqrt(x) = {round(sqrt(x), 2)}, {round(x ** 0.5, 2)}")
print(f"д) abs(n) = {abs(n)}")
print(f"е) 5 * cos(y) = {5 * round(cos(radians(y)), 2)}")
print(f"ж) -7.5 * a * a = {-7.5 * a * a}")
print(f"з) 3 * sqrt(x) = {round(3 * sqrt(x), 2)}, {round(3 * x ** 0.5, 2)}")
print(f"и) sin(a) * cos(b) + cos(a) * sin(b) = {round(
    sin(a) * cos(b) + cos(a) * sin(b), 2)}")
print(f"к) a * sqrt(2 * b) = {round(a * sqrt(2 * b), 2)}, \
      {round(a * 2 ** 0.5 * b ** 0.5)}")
print(f"л) 3 * sin(2 * a) * cos(3 * b) = \
      {round(3 * sin(2 * a) * cos(3 * b)), 2}")
print(f"м) -5 * sqrt(x + sqrt(y)) = {-5 * sqrt(x + sqrt(y))}, \
      {round(-5 * (x * y ** 0.5) ** 0.5)}")
