a = int(input("Введите трёхзначное число: "))
b = a // 100
c = (a // 10) % 10
d = a % 10
print(f"{c}{b}{d}")
