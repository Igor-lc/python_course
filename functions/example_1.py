def get_min_item(items):
    min_item = items[0]
    for item in items[1:]:
        if item < min_item:
            min_item = item
    return min_item


items1 = [23, 4, 7, 4, 12, 6, 8, 41, 20]
min_item = get_min_item(items1)
print(min_item)


print(get_min_item(items1))
