'''Напишите функцию replace_all, которая принимает два аргумента: текст и словарь. Функция должна сделать в тексте замены в соответствии с данными из словаря. Так если в
словаре есть ключ "one" со значением "один" ({'one': 'один'}), то функция должна заменить в тексте слово 'one' на 'один'. Обратите внимание, что в словаре может быть сколько угодно
элементов и нужно сделать замены для каждого из них. Для успешной работы данной программы вам также понадобится функция get_dict из прошлой задачи.

Пример использования функции:
result = replace_all("one, two, three, four", {'one': 'один', 'three': 'три', 'five': 'пять', 'two': 'два'})
print(result)
'один, два, три, four' '''

import get_dict

def replace_all(text, data):
    for k, v in data.items():
        if k in text:
            text = text.replace(k, v)

    return text

def replace_all2(text, data):
    for i in data.keys():
        if i in text:
            text = text.replace(i, data[i])

    return text

result = replace_all("one, two, three, four", {'one': 'один', 'three': 'три', 'five': 'пять', 'two': 'два'})
result2 = replace_all2("one, two, three, four", {'one': 'один', 'three': 'три', 'five': 'пять', 'two': 'два'})

print(result)
print(result2)
