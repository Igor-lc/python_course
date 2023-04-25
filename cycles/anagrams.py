import sys
word = list(sys.argv[1])

lst1 = []  # ['ш', 'ша', 'шак', 'шака', 'шакал', 'а', 'ак', 'ака', 'акал', 'к', 'ка', 'кал', 'а', 'ал', 'л'] - начало анаграмм
lst2 = []  # ['акал', 'кал', 'ал', 'л', '', 'шкал', 'шал', 'шл', 'ш', 'шаал', 'шал', 'ша', 'шакл', 'шак', 'шака'] - конец анаграмм, где мы удаляем по каждой букве и вставляем ее на все возможные позиции

for i in range(len(word)):
    for i2 in range(1, len(word) + 1):
        if i2 > i:
            word2 = ''.join(word[:i] + word[i2:])
            remainder = ''.join(word[i:i2])
            lst1.append(remainder), lst2.append(word2)

with open("words.txt", encoding='utf8') as f:
    words = [word.strip() for word in f.readlines()]
    anagrams = []

    for x, wrd in enumerate(lst2):
        wrd = list(wrd)
        for i, l in enumerate(wrd):
            wrd_ = wrd.copy()
            wrd_.pop(i)
            for i2 in range(len(wrd)):
                wrd_.insert(i2, l)
                anagram = lst1[x] + ''.join(wrd_)

                if anagram in words and anagram != sys.argv[1] and anagram not in anagrams:
                    anagrams.append(anagram)
                wrd_.pop(i2)

    x = len(anagrams)
    for word in words:
        if word in anagrams:
            anagrams.append(word)
    print(', '.join(anagrams[x:]))


'''ANAGRAM SEARCH
Difficulty: 7 out of 10
An anagram is a trick where you rearrange the letters of a word to make another word.

Write a program that takes a word as its first command-line argument and then looks up anagrams for it in the words.txt file 
that is located next to the program. As a result, you need to display all the found words separated by a comma with a space 
in the order in which they are located in the file. The original word is not required.'''
