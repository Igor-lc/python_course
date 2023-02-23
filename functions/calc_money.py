def calc_money(m, t):
    money = m * t[0] + round(m * t[1] / 60)
    return money

print(calc_money(1500, (7, 37)))
