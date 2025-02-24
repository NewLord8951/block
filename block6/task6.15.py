a = float(input("Введите число a: "))


def print_number_less_than_a(a):
    n = 1
    while True:
        curent_number = 1 + 1 / n
        if curent_number < a:
            print(curent_number)
        else:
            break
        n += 1


print_number_less_than_a(a)
