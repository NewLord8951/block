two = int(input("Введите двухзначное число: "))
a = int(input("Введите число a: "))
two_str = str(two)
a_str = str(a)
if "3" in two_str:
    print("а) Цифра 3 есть в числе")
else:
    print("а) Цифра 3 нету в числе")

if a_str in two_str:
    print("б) Цифра a есть в числе")
else:
    print("б) Цифры a нету в числк")
