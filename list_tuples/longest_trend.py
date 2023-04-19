import sys
trends = [int(i) for i in sys.argv[1].split()]
print(*trends)
# конвертируем список '1 2 3 7 7 3 2' в формат 'None 1 1 1 0 -1 -1', чтоб легче думать
better_trends = [None]
for i, curr in enumerate(trends[1:]):
    dif = curr - trends[i]
    if dif < 0:
        better_trends.append(-1)
    elif dif == 0:
        better_trends.append(0)
    else:
        better_trends.append(1)
print(*better_trends)

# исходные тренды:    2     1  1  2  3  4  4   3   2  3
# better_trend:       None -1  0  1  1  1  0  -1  -1  1  в цикле ниже prev - это предыдущий элемент, curr - текущий
# тренд 1:            2     1  1
# тренд 2:                  1  1  2  3  4  4
# тренд 3:                              4  4   3   2
# тренд 4:                                         2  3
# теперь видим, что условие начала тренда:  str(prev) in 'None-11'
# условие конца тренда:                     str(curr) in '-11'
# при условии prev != curr
# находим индексы начала и конца всех трендов:
starts, ends = [], []
for i, curr in enumerate(better_trends[1:]):
    prev = better_trends[i]
    starts.append(i) if str(prev) in 'None-11' and prev != curr else None
    ends.append(i) if str(curr) in '-11' and prev != curr and i != 0 else None
ends.append(i + 1)

longest = []
for x, y in zip(starts, ends):
    if y + 1 - x > len(longest):
        longest = trends[x:y + 1]
print(*longest)


# version 2
starts, ends = [], []
for i, curr in enumerate(better_trends[1:]):
    prev = better_trends[i]
    starts.append(i) if str(prev) in 'None-11' and prev != curr else None
    ends.append(i) if str(curr) in '-11' and prev != curr and i != 0 else None
ends.append(i + 1)


longest = []
for x, y in zip(starts, ends):
    if y + 1 - x > len(longest):
        longest = trends[x:y + 1]
#print(*longest)
