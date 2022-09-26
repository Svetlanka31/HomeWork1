# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


x = int(input('Введите число 0 или 1: '))
y = int(input('Введите число 0 или 1: '))
z = int(input('Введите число 0 или 1: '))

if (x == 0 or x ==1) and (y == 0 or y ==1) and (z == 0 or z == 1):
    leftPart = not (x or y or z)
    rightPart = not x and not y and not z
    result = leftPart == rightPart
    if result == True:
        print('Утверждение истинно')

    else:
        print('Утверждение ложно')

else:
    print('неверно введено число')


