a = int(input('Введите a — целое число, a > b: '))
b = int(input('Введите b — целое число, a > b: '))
c = int(input('Введите c — целое число, c > d: '))
d = int(input('Введите d — целое число, c > d: '))
if a > b and c > d:
    print(f'Вот сколько можно разместить прямоугольников \
          на столе длинной стороной {a // c}, короткой стороной {a // d}')
else:
    print('Данные не верные :(')
