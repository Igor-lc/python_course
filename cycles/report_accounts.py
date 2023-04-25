def balans(fprov):
    # В 1 цикле формируем c_from, c_to, summ
    # Используем свойства словаря, res[c_from] и res[c_to] - добавляем ключи, если их не было
    # Пишем значение по умолчанию = 0, используя метод get
    # Если ключи были - изменяем балансы отправителя и получателя

    res = {}
    with open(fprov, "r", encoding='utf8') as fi:
        for line in fi:
            (c_from, c_to, summ) = map(int, line.split(";"))
            res[c_from] = res.get(c_from, 0) - summ
            res[c_to] = res.get(c_to, 0) + summ

    tmp = []  # Формируем [(123, 600), (456, -100), (789, -300)] - кроме внутреннего счета банка
    for count in res.keys():
        if count != 0:
            tmp.append((count, res[count]))

    # Сортируем пузырьком: https://younglinux.info/algorithm/bubble
    n = len(tmp)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if tmp[i][1] > tmp[j][1]:
                tmp[i], tmp[j] = tmp[j], tmp[i]

    # формируем строку в нужном формате
    strout = ""
    for pair in tmp:
        strout = strout + str(pair[0]) + " " + str(pair[1]) + ";"
    ls = len(strout)
    return strout[0:ls - 1]

print(balans("bank2.txt"))
