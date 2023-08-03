import sys
numbers = sys.argv[1:]


i = 0
final_numbers = []
while i < len(numbers):
    number = int(numbers[i])
    j = 0
    while j < int(numbers[i]):
        final_numbers.append(str(number))
        j += 1
    i += 1
print(', '.join(final_numbers))


final_numbers = []
i = 0
while i < len(numbers):
    number = numbers[i]
    final_numbers.extend([number] * int(number))
    i += 1
print(', '.join(final_numbers))