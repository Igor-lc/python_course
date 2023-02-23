def sum_mult_index(l_):
    result = 0
    for i, el in enumerate(l_):
        result += (i * l_[i])

    return result


def sum_mult_index2(l_):
    return sum(e * i for e, i in enumerate(l_[1:], 1))


print(sum_mult_index([11, 22, 33, 44, 55]))
print(sum_mult_index2([11, 22, 33, 44, 55]))
