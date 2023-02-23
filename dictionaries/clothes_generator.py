from sys import argv
name = argv[1]
size = argv[2]
sexx = argv[3]


sizes = {
    "44": "xs",
    "46": "s",
    "48": "m",
    "50": "l",
    "52": "xl"
}

sex = {
    "m": "m",
    "f": "w",
    "w": "w"
}

size = sizes.get(size, 'all')
sexx = sex.get(sexx, 'unisex')
name = name.lower().replace(" ", "-")

print(name, size, sexx, sep='-')
