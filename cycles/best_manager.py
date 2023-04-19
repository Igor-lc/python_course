from collections import defaultdict

managers = {}
managers = defaultdict(int)  # https://docs.python.org/3/library/collections.html#collections.defaultdict

for i in open("sales.txt", encoding='utf-8'):
    k, v = i.split('\t')
    managers[k] += int(v)

best_manager = max(managers, key=managers.get)
print(f"{best_manager}, {managers[best_manager]}")



# ver 2
managers = {}

for i in open("sales.txt", encoding='utf-8'):
    k, v = i.split('\t')
    if not managers.get(k):
        managers[k] = int(v)
    else:
        managers[k] += int(v)

best_manager = max(managers, key=lambda k: managers[k])
print(f"{best_manager}, {managers[best_manager]}")
