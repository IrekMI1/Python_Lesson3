# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import *
some_list = []
for _ in range(10):
    some_list.append(round(uniform(0.0, 100.0), 3))
max_frac = some_list[0] - some_list[0] // 1
min_frac = some_list[1] - some_list[1] // 1
if min_frac > max_frac: 
    max_frac, min_frac = min_frac, max_frac
for i in range(2, len(some_list)):
    if some_list[i] - some_list[i] // 1 > max_frac:
        max_frac = some_list[i] - some_list[i] // 1
    elif some_list[i] - some_list[i] // 1 < min_frac:
        min_frac = some_list[i] - some_list[i] // 1
print(some_list)
print('Max =', round(max_frac, 3))
print('Min =', round(min_frac, 3))
print('Max - Min =', round(max_frac - min_frac, 3))