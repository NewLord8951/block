a = int(input("Введите трёхзначное число: "))
a0 = a // 100
a1 = (a // 10) % 10
a2 = a % 10
a_2 = a ** 2
a_3 = (a0 ** 3) + (a1 ** 3) + (a2 ** 3)


if a_2 == a_3:
    print("Равны")
else:
    print("Не равны")
