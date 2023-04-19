def choose_plural(count_, words):
    c, w = str(count_)[-1], words.split(',')
    if int(c) == 0 or 5 <= int(c) <= 9 or 10 <= count_ <= 20:
        return w[2]
    elif int(c) == 1:
        return w[0]
    elif 2 <= int(c) <= 4:
        return w[1]


def choose_plural2(amount, variants):
    variants = variants.split(",")
    if amount % 10 == 1 and amount % 100 != 11:
        variant = 0
    elif amount % 10 >= 2 and amount % 10 <= 4 and \
         (amount % 100 < 10 or amount % 100 >= 20):
        variant = 1
    else:
        variant = 2
    return variants[variant]

print(choose_plural(0, "ананас,ананаса,ананасов"))
print(choose_plural2(21, "ананас,ананаса,ананасов"))
