import sys
word = list(sys.argv[1])

lst1 = []  # ['ш', 'ша', 'шак', 'шака', 'шакал', 'а', 'ак', 'ака', 'акал', 'к', 'ка', 'кал', 'а', 'ал', 'л']
lst2 = []  # ['акал', 'кал', 'ал', 'л', '', 'шкал', 'шал', 'шл', 'ш', 'шаал', 'шал', 'ша', 'шакл', 'шак', 'шака']

for i in range(word.__len__()):
    for i2 in range(1, len(word) + 1):
        if i2 > i:
            word2 = ''.join(word[:i] + word[i2:])
            remainder = ''.join(word[i:i2])
            lst1.append(remainder)
            lst2.append(word2)

with open("words.txt", encoding='utf8') as f:
    words = [word.strip() for word in f.readlines()]
    anagrams = []

    for x, wrd in enumerate(lst2):
        wrd = list(wrd)
        for i, l in enumerate(wrd):
            wrd_ = wrd[:]
            wrd_.pop(i)
            for i2 in range(len(wrd)):
                wrd_.insert(i2, l)
                anagram = lst1[x] + ''.join(wrd_)
                if anagram in words and anagram != sys.argv[1] and anagram not in anagrams:
                    anagrams.append(anagram)
                wrd_.pop(i2)

x = len(anagrams)
with open("words.txt", encoding='utf8') as f:
    for i in f:
        if i.strip() in anagrams:
            anagrams.append(i.strip())
print(', '.join(anagrams[x:]))
