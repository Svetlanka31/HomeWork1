# 5. Задача 5.Реализуйте алгоритм перемешивания списка.

import random

def mix_list(list):
    list_copy = list[:]
    list_copy_length=len(list_copy)
    for i in range(list_copy_length):
        index = random.randint(0,list_copy_length-1)
        list_copy[i],list_copy[index] = list_copy[index],list_copy[i]
        return list_copy
list = ['Hello',',','my','teacher','!']
mixed_list = mix_list(list)
print(list)
print(f'Получившийся список {mixed_list}')
