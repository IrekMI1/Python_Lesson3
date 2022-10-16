# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

dec_number = int(input('Введите число: '))
bin_str = ''
while dec_number != 0:
    bin_str += str(dec_number % 2)
    dec_number //= 2
bin_str = "".join(reversed(bin_str))
print(bin_str)