# Напишите программу, которая по заданному номеру четверти,
#  показывает диапазон возможных координат точек в этой 
#  четверти (x и y).

a = input('Введите четверть: ')
if a == '1':
    print('x > 0 and y > 0')
elif a == '2':
    print('x < 0 and y > 0')
elif a == '3':
    print('x < 0 and y < 0')
elif a == '4':
    print('x > 0 and y < 0')
else:
    print("It's not quarter")
    