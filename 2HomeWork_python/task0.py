# Задача1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

number = input('Введите  число:')
if float(number) < 0:
    number = float(number)*(-1)
cull_sum =0
for i in str(number):
    if i != '.':
        cull_sum+=int(i)

print(f'Сумма чисел числа {number} = {cull_sum}')
    