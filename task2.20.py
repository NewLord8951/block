a = int(input("Введите четырёхзначное число: "))
b = a // 1000
c = (a // 100) % 10
d = (a // 10) % 10
e = a % 10
print(int(''.join([str(e), str(d), str(c), str(b)])))
print(int(''.join([str(c), str(b), str(e), str(d)])))
print(int(''.join([str(b), str(d), str(c), str(e)])))
print(int(''.join([str(d), str(e), str(b), str(c)])))
