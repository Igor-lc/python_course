def sum_num(num):
    sum_ = num
    for i in range(num):
        sum_ += i
    return sum_


def sum_num2(num):
    sum_ = 0
    while num > 0:
        sum_ += num
        num -= 1
    return sum_


def sum_num_rec(num):
    if num <= 1:
        return num
    return num + sum_num_rec(num - 1)


def sum_num_guass(num):
    return int(num * (num + 1) / 2)


print(sum_num_guass(4))
