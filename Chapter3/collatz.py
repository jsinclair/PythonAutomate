def collatz(number):
    if number % 2 == 0:
        newNum = number / 2
    else:
        newNum = 3 * number + 1
    print(newNum)
    return newNum

try:
    num = int(input('Enter a number: '))
except ValueError:
    print('You need to enter a valid number.')

while num != 1:
    num = collatz(num)