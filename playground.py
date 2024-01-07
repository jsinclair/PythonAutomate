import random
import pprint

"""Multiline comment! 
This is a playground file, 
for testing concepts as I read them.
Source: https://automatetheboringstuff.com/2e/
"""

def hello(name):
    print('Hello,', name)
hello('Hannah')
hello('Carli')
hello('Varlets')

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument. ')

for a in range(5):
    test = a
    print(a)
print(test)

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

animals = ['cat', 'bat', 'rat', 'elephant']
print(animals)
print(animals[0])
print(animals[0:4])
print(animals[1:3])
print(animals[-1])
print(len(animals))
del animals[2]
print(animals)
print(len(animals))
animals += ['Pug']
print(animals)
print(len(animals))
animalsSlice = animals[1:]
print(len(animalsSlice))
print(animalsSlice)

for i in range(len(animals)):
    print('animals[', i, ']: ', animals[i], sep='')

cat = ['fat', 'gray', 'loud']
size, color, disposition = cat
print(size, color, disposition)

for index, item in enumerate(animals):
    print('animals[', index, ']: ', item, sep='')

print(random.choice(animals))
random.shuffle(animals)
for index, item in enumerate(animals):
    print('animals[', index, ']: ', item, sep='')

print('at' in size)

myCat = {'size': 'small', 'color': 'tortoise shell', 'disposition': 'friendly'}
print('size' in myCat)

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)
pprint.pprint(count)