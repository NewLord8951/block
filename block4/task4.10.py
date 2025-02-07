radius = int(input("Значение радиуса: "))
storona = int(input("Значение стороны: "))

a = 3.14 * (radius ** 2)
b = storona ** 2

if a > b:
    print("Площадь круга больше")
else:
    print("Площадь Квадрата больше")
