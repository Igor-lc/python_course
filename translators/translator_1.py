from string import ascii_lowercase

dic = {'one': 'один', 'three': 'три', 'five': 'пять', 'two': 'два', 'i': 'я', 'want': 'хочу', 'relax': 'отдыхать', 'never': 'никогда', 'work': 'работать', 'not': 'не'}

verbs = {'be': 'быть', 'have': 'иметь', 'do': 'делать', 'make': 'совершать', 'get': 'получать', 'take': 'брать', 'try': 'пробовать', 'know': 'знать', 'think': 'думать', 'feel': 'чувствовать',
         'see': 'видеть', 'give': 'давать', 'bring': 'приносить', 'buy': 'покупать', 'cost': 'стоить', 'break': 'разрушать', 'put': 'класть', 'eat': 'есть', 'sleep': 'спать', 'drink': 'пить',
         'understand': 'понимать', 'write': 'писать', 'read': 'читать', 'speak': 'говорить', 'tell': 'сказать', 'meet': 'встречать', 'teach': 'обучать', 'learn': 'учиться', 'send': 'отправлять'}

def en_ru(text, data):
    for k, v in data.items():
        if k in text:
            text = text.replace(k, v)
    return text

def ru_en(text, data):
    for k, v in data.items():
        if v in text:
            text = text.replace(v, k)
    return text

while True:
    text = input("Enter text to translate: ")
    if text[0].lower() in ascii_lowercase:
        print(en_ru(text.lower(), dic))
    else:
        print(ru_en(text.lower(), dic))

