with open("shopping_list_1.txt", encoding='utf8') as f1, open("shopping_list_2.txt", encoding='utf8') as f2, open("shopping_list_3.txt", encoding='utf8') as f3:
    f = f1.read() + f2.read() + f3.read()
    result = {i: 1 for i in f.strip().split('\n')}
    result = sorted(list(result.keys()))
    with open("shopping_list.txt", 'w', encoding='utf8') as r:
        for i in result:
            print(i, file=r)
