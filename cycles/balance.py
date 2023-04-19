from sys import argv

print(sum([int(i.split(';')[2]) if i.split(';')[1] == 'income' else -int(i.split(';')[2]) for i in open("transactions.txt")]))

total = 0
for i in open("bank.txt").readlines():
    if i.split(';')[0] == argv[1]:
        total -= int(i.split(';')[2])
    if i.split(';')[1] == argv[1]:
        total += int(i.split(';')[2])
print(total)

total = 0
for transaction in open("bank.txt", "r"):
    account_from, account_to, amount = transaction.split(";")
    if account_from == argv[1]:
        total -= int(amount)
    if account_to == argv[1]:
        total += int(amount)
print(total)

