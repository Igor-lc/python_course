from sys import argv

revenue = {
    2017: 123_000,
    2018: 127_000,
    2019: 134_000,
    2020: 201_000,
    2021: 289_000
}

a = (revenue.get(int(argv[1]), 0) or 0) - (revenue.get(int(argv[2]), 0) or 0)
print(a)


year1 = int(argv[1])
year2 = int(argv[2])
if year1 < year2:
    a = (revenue.get(year2, 0) or 0) - (revenue.get(year1, 0) or 0)
else:
    a = (revenue.get(year1, 0) or 0) - (revenue.get(year2, 0) or 0)
print(a)


min_year = min(year1, year2)
max_year = max(year1, year2)
print((revenue.get(max_year, 0) or 0) - (revenue.get(min_year, 0) or 0))
