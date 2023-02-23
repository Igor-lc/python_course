from sys import argv
month1 = int(argv[1])
month2 = int(argv[2])

fin = [
    {"income": 987, "expenses": 345},
    {"income": 1987, "expenses": 1247},
    {"income": 3011, "expenses": 2098},
    {"income": 3400, "expenses": 2798},
    {"income": 1987, "expenses": 1783},
    {"income": 2684, "expenses": 2004},
    {"income": 2008, "expenses": 1555},
    {"income": 2498, "expenses": 2210},
    {"income": 1714, "expenses": 1789},
    {"income": 6971, "expenses": 6971},
    {"income": 345, "expenses": 147},
    {"income": 2487, "expenses": 2101}
]

profitability1 = fin[month1 - 1]['income'] - fin[month1 - 1]['expenses']
profitability2 = fin[month2 - 1]['income'] - fin[month2 - 1]['expenses']

print(profitability2 - profitability1)
