import re

def isStrongPassword(password):
    passwordRegex = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")
    return passwordRegex.match(password) != None

tests = ['password', 'Password', 'P@ssword', 'P@ssw0rd']

for test in tests:
    print(test, ": ", isStrongPassword(test), sep="")