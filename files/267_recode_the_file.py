"""
ПЕРЕКОДИРУЕМ ФАЙЛ
Рядом с программой находится файл product.txt в кодировке cp1251.
Напишите программу, которая перекодирует его в кодировку utf-8.
"""

with open("product.txt", encoding="cp1251") as fi:
    products = fi.read().strip()

    # открываем на запись в кодировке utf-8 (encoding="utf-8" можно не писать)
    with open("product.txt", "w") as new_food:
        print(products, file=new_food)
