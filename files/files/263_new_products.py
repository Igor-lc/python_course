with open("prod.txt", "a+", encoding="utf8") as file:
    file.write("\nМасло\nМясо")

with open("prod.txt", "r", encoding="utf8") as file:
    products = file.read()
    print(products)
