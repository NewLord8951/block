num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))
if num1 > num2 and num1 > num3:
    print("Наибольшее: первое ", num1)
elif num2 > num3:
    print("Наибольшее: второе ", num2)
else:
    print("Наибольшее: третье ", num3)
if num1 < num2 and num1 < num3:
    print("Наименьшее: первое ", num1)
elif num2 < num3:
    print("Наименьшее: второе ", num2)
else:
    print("Наименьшее: третье", num3)
