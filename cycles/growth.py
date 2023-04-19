import sys
text = sys.argv[1]
swapped = ""
i = 0
while i < len(text) - 1:
    swapped += text[i+1] + text[i]
    i += 2
if len(text) % 2 == 1:
    swapped += text[-1]
print(swapped)

# ver 2
text = list(sys.argv[1])
for i in range(0, len(text) - 1, 2):
    text[i], text[i + 1] = text[i + 1], text[i]
print("".join(text))


# ver 3
text = sys.argv[1]
new_letters = []
for i, j in enumerate(text):
    if i & 1:
        new_letters.append(j)
        new_letters.append(text[i - 1])
    elif len(text) - len(new_letters) == 1:
        new_letters.append(text[-1])

print(''.join(new_letters))
