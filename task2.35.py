num1 = input("Введите двухзначное число: ")
num2 = input("Введите двухзначное число: ")

a2 = num1[0]
a1 = num1[1]

b2 = num2[0]
b1 = num2[1]

match b1:
    case "0":
        s = a1
    case "1":
        s = int(a1) + 1
    case "2":
        s = int(a1) + 2
    case "3":
        s = int(a1) + 3
    case "4":
        s = int(a1) + 4
    case "5":
        s = int(a1) + 5
    case "6":
        s = int(a1) + 6
    case "7":
        s = int(a1) + 7
    case "8":
        s = int(a1) + 8
    case "9":
        s = int(a1) + 9
    case _:
        s = None

match b2:
    case "0":
        q = a2 + (int(s) // 10)
    case "1":
        q = int(a2) + 1 + (int(s) // 10)
    case "2":
        q = int(a2) + 2 + (int(s) // 10)
    case "3":
        q = int(a2) + 3 + (int(s) // 10)
    case "4":
        q = int(a2) + 4 + (int(s) // 10)
    case "5":
        q = int(a2) + 5 + (int(s) // 10)
    case "6":
        q = int(a2) + 6 + (int(s) // 10)
    case "7":
        q = int(a2) + 7 + (int(s) // 10)
    case "8":
        q = int(a2) + 8 + (int(s) // 10)
    case "9":
        q = int(a2) + 9 + (int(s) // 10)
    case _:
        q = None

print(f"Ответ: {str(q) + str(s)}")
