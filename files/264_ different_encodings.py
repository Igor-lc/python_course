'''
264. РАЗНЫЕ КОДИРОВКИ
Рядом с программой находятся два файла: products.txt и new_products.txt.
Первый сохранен в кодировке cp1251, а второй в koi8-r.

Напишите программу, которая копирует список продуктов из файла new_products.txt в
products.txt.
'''


with open("new_products.txt", encoding="koi8-r") as file_new:
    new_products = file_new.read()

with open("products.txt", "a", encoding="cp1251") as file:
    file.write(new_products)
