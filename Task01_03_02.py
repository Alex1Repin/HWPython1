# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def Hypotenuza(ax, ay, bx, by):
    catet_a = ax - bx
    catet_b = ay - by
    hypotenuza = (catet_a**2 + catet_b**2)**0.5
    print(round(hypotenuza, 2))
    


Hypotenuza(3, 6, 2, 1)
Hypotenuza(7, -5, 1, -1)