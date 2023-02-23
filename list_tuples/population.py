from sys import argv
s = argv[1].capitalize()
s = list(s)

i = argv[1].rfind(",")
s[i] = " и "

print("".join(s).replace(",", ", "), end=".")



products = argv[1].split(",")
products_str = ", ".join(products[:-1])
products_str = products_str + " и " + products[-1] + "."

print(products_str.capitalize())
