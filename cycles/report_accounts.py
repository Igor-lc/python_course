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


'''316. ACCOUNT REPORT
Difficulty: 7 out of 10

You have already calculated the balance of each account separately. Now it's time to build a report on all bank accounts.

Write a program that goes through all the transactions in the bank.txt file, and then displays all the accounts and the balance of each account.

The data must be output in the following format:
Account1 Balance1;Account2 Balance2;Account N; Balance N.
That is, the accounts are separated by a semicolon, and each account individually contains its number and balance, separated by a space.

Invoices should be displayed in ascending order of balance (see sample report below).

Please note that the file has account 000 - this is the bank's internal account, you do not need to display it:

000;123;200
123;456;100
456;789;200
789;123;500

> python program.py
789 -300;456 -100;123 600'''
