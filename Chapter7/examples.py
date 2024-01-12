import re

def isPhoneNumber(text):
    phoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
    return phoneNumberRegex.match(text) != None

print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(f'mo.group(0): {mo.group(0)}')
print(f'mo.group(1): {mo.group(1)}')
print(f'mo.group(2): {mo.group(2)}')

heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')

# optional, multiples allowed
batRegex = re.compile(r'Bat(wo)*man')
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

# At least one required, multiple allowed
batRegex = re.compile(r'Bat(wo)+man')
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

# Greedy regex, matches longest possible match, default behaviour
# non-greedy, put ? after curly braces, matches shortest possible

# Character classes
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))
# Negative character classes
negativeVowelRegex = re.compile(r'[^aeiouAEIOU]')
print(negativeVowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))
