import sys
input_word = sys.argv[1]

sorted_input_word = "".join(sorted(list(input_word)))

anagrams = []
for word in open("words.txt", encoding='utf8'):
    word = word.strip()

    # Сортируем буквы слова
    sorted_word = "".join(sorted(list(word)))

    # Если два отсортированных слова равны, то это анаграмма
    if sorted_word == sorted_input_word and word != input_word:
        anagrams.append(word)

print(", ".join(anagrams))



'''ANAGRAM SEARCH
Difficulty: 7 out of 10
An anagram is a trick where you rearrange the letters of a word to make another word.

Write a program that takes a word as its first command-line argument and then looks up anagrams for it in the words.txt file 
that is located next to the program. As a result, you need to display all the found words separated by a comma with a space 
in the order in which they are located in the file. The original word is not required.'''
