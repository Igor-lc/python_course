with open("products.txt", "r", encoding="utf8") as f:
    data = f.read().strip().split("\n")
    data.sort(key=str.lower)
    data = "\n".join(data)

with open("products.txt", "w", encoding="utf8") as f_:
    print(data, file=f_, end="")
