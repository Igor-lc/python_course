words = open("../../programming_in_python_3/additional/example.txt", "r", encoding="utf_8").read()

total_number_of_words = 0
different_words = []
total_number_of_different_words = 0
the_total_number_of_each_word = []
percent_word = []

for word in words.split():
    if word in words:
        total_number_of_words += 1
    if word not in different_words:
        different_words.append(word)
        total_number_of_different_words += 1
        the_total_number_of_each_word.append(words.count(word))

for count_word in the_total_number_of_each_word:
    percent_word.append(round((100 * count_word / total_number_of_words), 1))

print("total number of words =", total_number_of_words)
print("different words =", different_words)
print("total number of different words =", total_number_of_different_words)
print("the total number of each word =", the_total_number_of_each_word)
print(sum(the_total_number_of_each_word))
print("percent word", percent_word)
print(sum(percent_word))
