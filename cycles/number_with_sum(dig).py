# ЧИСЛО С МАКСИМАЛЬНОЙ СУММОЙ ЦИФР
# Напишите программу, которая принимает из аргументов командной строки произвольное количество чисел, а затем выводит то, у которого максимальная сумма цифр.
# > python program.py 111 2 33 41
# 33

from sys import argv
args = argv[1:]
number_i = digit_i = current_sum = max_sum = max_args = 0

while number_i < len(args):
    while digit_i < len(args[number_i]):
        current_sum += int(args[number_i][digit_i])
        if max_sum < current_sum:
            max_sum = current_sum
            max_args = args[number_i]
        digit_i += 1
    number_i += 1
    digit_i = current_sum = 0

print(max_args)

#
max_sum = max_number = number_i = 0
while number_i < len(args):
    digit_i = 0
    current_sum = 0
    while digit_i < len(args[number_i]):
        current_sum += int(args[number_i][digit_i])
        digit_i += 1

    if current_sum > max_sum:
        max_sum = current_sum
        max_number = args[number_i]

    number_i += 1
print(max_number)

#
max_sum = max_number = number_i = 0
while number_i < len(args):
    number = int(args[number_i])
    digit_i = 0
    current_sum = 0

    while number > 0:
        current_sum += number % 10
        number //= 10

    if current_sum > max_sum:
        max_sum = current_sum
        max_number = args[number_i]

    number_i += 1
print(max_number)

'''
пояснение варианта 3:

Возьмем число 123 (number=123).
current_sum = 0

1. Первая итерация
number % 10 равно 3 (фактически остаток от деления на 10 всегда будет возвращать десятки, то есть последнюю цифру в числе)
current_sum += 3 будет 3
number //= 10 - это тоже самое, что и number = number // 10, - это целочисленное деление, то есть делим 123 на 10 и оставляет только целую часть - 12

2. Вторая итерация

number % 10 - 12 % 10 получаем 2
current_sum += 2 будет 5
number //= 10 - 12 // 10 = 1

3. Третья итерация

number % 10 - 1 % 10 получаем 1
current_sum += 1 будет 6
number //= 10 - 1 // 10 = 0 - дальше цикл выполняться не будет

В итоге в current_sum будет 6.'''
