import sys

base_price = int(sys.argv[1])
new_price = int(sys.argv[2])

product = {
   "name": "Бинокль",
   "price": [base_price, new_price]
}

t_template = "{p[name]}: {p[price][1]} руб."
print(t_template.format(p=product))
