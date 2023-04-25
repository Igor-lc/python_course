from collections import defaultdict
transactions_file = open("bank2.txt", "r")

# Словарь, который будет хранить счета.
# Используем defaultdict, чтобы автоматически создавать ключи.
accounts = defaultdict(int)

total = 0
for transaction in transactions_file:
    account_from, account_to, amount = transaction.split(";")

    # Заполняем данными.
    accounts[account_from] -= int(amount)
    accounts[account_to] += int(amount)

# Удаляем словарь 000
del accounts["000"]

# Сразу сортируем словарь и формируем финальный результат.
print(";".join([f"{account} {balance}" for account, balance in sorted(accounts.items(), key=lambda a: a[1])]))


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
