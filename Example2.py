# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from math import *
from random import *
some_list = []
for _ in range(randint(1, 10)):
    some_list.append(randint(0, 11))
print(some_list)
pair_mult = []
for i in range(ceil(len(some_list) / 2)):
    pair_mult.append(some_list[i] * some_list[len(some_list) - 1 - i])
print(pair_mult)