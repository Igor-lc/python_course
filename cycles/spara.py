list = [i.casefold().replace('спар', 'SPAR').strip() for i in open("dict.txt", encoding='utf8') if "спар" in i.casefold()]
print('\n'.join(list))
