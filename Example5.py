# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fibbonachi(n):
    if n == 0:
        return 0    
    elif n in [-1, 1, 2]:
        return 1
    elif n < -1:
        return fibbonachi(n + 2) - fibbonachi(n + 1)
    else:
        return fibbonachi(n - 1) + fibbonachi(n - 2)

number = int(input('Введите целое число: '))
fibbonachi_list = []
for i in range(-number, number + 1):
    fibbonachi_list.append(fibbonachi(i))
print(fibbonachi_list)