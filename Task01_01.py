# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот 
# день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = input('Введите число: ')
if 0 < int(a) and int(a) < 8:
    print('Да')
else:
    print('Нет')