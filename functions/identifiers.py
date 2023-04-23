import string
ALLOWED = string.ascii_letters + string.digits + '-'


def gen_id(name, ids):
    name = name.strip().lower().replace(" ", "-")
    eng_name = ""
    for c in name:
        if c in ALLOWED:
            eng_name += c

    new_name = eng_name
    i = 2
    while new_name in ids:
        new_name = f"{eng_name}-{i}"
        i += 1

    return new_name


print(gen_id("Alpen Gold", ["snickers", "bounty", "mars"]))
print(gen_id("Mars", ["snickers", "bounty", "mars"]))
print(gen_id("Mars", ["snickers", "bounty", "mars", "mars-2"]))
print(gen_id("M&Ms", ["snickers", "bounty", "mars"]))


'''314. IDENTIFIERS

Often, for the title of an article on a website or a product in an online store, you need to generate a unique identifier, which can then be inserted into the URL. Write a gen_id function that generates such an id.

The first argument to the function is the name of the product in English, as well as a list of already existing identifiers. The new identifier is generated according to the following rules:

The original name is converted to lower case.
Spaces to the right and left of the name are removed.
All spaces are replaced with dashes.
All characters, except for the Latin alphabet, numbers, and the dash sign, must be deleted.
If the received identifier already exists, then the function should add a dash to the end of the generated number, which starts with a two. If an identifier with a two also exists, then the number is increased by 1. And so on until an identifier is found that does not exist.

print(gen_id("Alpen Gold", ["snickers", "bounty", "mars"]))
# alpen-gold
print(gen_id("Mars", ["snickers", "bounty", "mars"]))
# mars-2
print(gen_id("Mars", ["snickers", "bounty", "mars", "mars-2"]))
# mars-3
print(gen_id("M&Ms", ["snickers", "bounty", "mars"]))
# mms'''
