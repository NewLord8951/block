x = int(input("Введите расстояние в километрах x: "))
y = int(input("Введите расстояние в футах y: "))
x = x / 1000
y = y * 0.305
if x > y:
    print("больше:", x)
elif y > x:
    print("больше:", y)
