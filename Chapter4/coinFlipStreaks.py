import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    list = ''
    while len(list) < 100:
        list += str(random.randint(0, 1))

    # Code that checks if there is a streak of 6 heads or tails in a row.
    if '111111' in list or '000000' in list:
        numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))