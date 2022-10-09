#Напишите программу для. проверки истинности утверждения 
#¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#not(x or y or z) = not x and not y and not z

for x in range(1):
    for y in range(1):
        for z in range(1):
            if not(x or y or z) == (not x and not y and not z):
                print(True)
            else:
                print(False)