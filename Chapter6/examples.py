import pyperclip

print(r'This is James\' puppy')

multilineString = '''This is 
a multiline
string'''
print(multilineString)

# String interpolation
name = 'Cthulu'
age = 10000
print('My name is %s. I am %s years old.' % (name, age))
print(f'My name is {name}. I am {age + 1} years old.')

# Useful string methods
testStr = 'Hello'
print(f'testStr: {testStr}')
print(f'testStr.isupper(): {testStr.isupper()}')
print(f'testStr.islower(): {testStr.islower()}')
print(f'testStr.isalpha(): {testStr.isalpha()}')
print(f'testStr.isdecimal(): {testStr.isdecimal()}')
print(f'testStr.isspace(): {testStr.isspace()}')
print(f'testStr.istitle(): {testStr.istitle()}')
print(f'testStr.isalnum(): {testStr.isalnum()}')
print(f'testStr.startswith(\'Hel\'): {testStr.startswith("Hel")}')
print(f'testStr.endswith(\'llo\'): {testStr.endswith("llo")}')

print(', '.join(['cats', 'rats', 'bats']))
print('My name is Simon'.split())

# Partition splits around a character
print(f'\'Hello, world!\'.partition(\'w\'): {"Hello, world!".partition("w")}')

# rjust, ljust, and center for padding to specific lengths with whichever character
print(f"'Hello'.rjust(10): {'Hello'.rjust(10)}")
print(f"'Hello'.ljust(20, '-'): {'Hello'.ljust(20, '-')}")

# ord() to get the code point of a 1 char string and chr() to get the 1 char string for an int
print(f"ord('A'): {ord('A')}")
print(f"chr(66): {chr(66)}")

# use pyperclip for acces to system copy/paste
# pip install pyperclip

print("pyperclip.copy('Hello, world!')")
pyperclip.copy('Hello, world!')
print(f"pyperclip.paste(): {pyperclip.paste()}")
