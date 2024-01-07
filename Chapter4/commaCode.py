def commaCode(list):
    str = ''
    for index, value in enumerate(list):
        if index > 0:
            str += ', '
            if index == len(list) - 1:
                str += 'and '
        str += value
    return str

spam = ['apples', 'bananas', 'tofu', 'cats']
print(commaCode(spam))

spam = ['apples']
print(commaCode(spam))

spam = ['apples', 'pears']
print(commaCode(spam))

spam = []
print(commaCode(spam))