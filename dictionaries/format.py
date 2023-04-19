import sys
first_name = sys.argv[1]
last_name = sys.argv[2]
age = sys.argv[3]

user = {
   "first_name": first_name,
   "last_name": last_name,
   "age": age
}

print("{} {}, {}".format(user["last_name"], user["first_name"], user["age"]))
print("{u[last_name]} {u[first_name]}, {u[age]}".format(u=user))
print("{last_name} {first_name}, {age}".format(**user))


name = sys.argv[1]
category = sys.argv[2]
price = sys.argv[3]

product = {
   "name": name,
   "category": category,
   "price": price
}
product_template = "{name} ({category}), {price} руб."
print(product_template.format(**product))

product_template = "{product[name]} ({product[category]}), {product[price]} руб."
print(product_template.format(product=product))


t_from = sys.argv[1]
t_to = sys.argv[2]
amount = sys.argv[3]

transaction = {
   "from": t_from,
   "to": t_to,
   "amount": amount
}

t_template = "Перевод {t[amount]} руб. со счета {t[from]} на счет {t[to]}."
print(t_template.format(t=transaction))
