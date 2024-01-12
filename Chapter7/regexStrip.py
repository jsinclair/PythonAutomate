import re

def strip(str: str, sep: str | None = None):
    if sep == None:
        regex = re.compile(r'^\s+')
    else:
        regex = re.compile('^(' + sep + '+)')

    stripped = regex.sub('', str)

    if sep == None:
        regex = re.compile(r"\s+\Z")
    else:
        regex = re.compile('(' + sep + '+)\Z')

    stripped = regex.sub('', stripped)
    return stripped

testStr = ' hello asd '
print(testStr)
print(testStr.strip())
print(testStr.strip().strip('h'))
print(strip(testStr), 'heyo', sep='')

testStr = 'hello asdhe'
print(strip(testStr, sep='he'), 'heyo', sep='')