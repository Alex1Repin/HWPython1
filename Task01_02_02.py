# Напишите программу, которая принимает на вход координаты точки 
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#  в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def Quarter(x, y):
    if x > 0 and y > 0:
        print(1)
    elif x < 0 and y > 0:
        print(2)
    elif x < 0 and y < 0:
        print(3)
    elif x > 0 and y < 0:
        print(4)
    elif x == 0 and y != 0:
        print('Точка лежит нв оси X')
    elif x != 0 and y == 0:
        print('Точка лежит на оси Y')
    else:
        print('Начало координат')

Quarter(2, 48)
Quarter(-1, 45)
Quarter(-1, -34)
Quarter(34, -4)
Quarter(0, -2)
Quarter(3, 0)
Quarter(0, 0)
