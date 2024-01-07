import random
import sys

wins = 0
losses = 0
ties = 0

plays = ['r', 'p', 's']
titles = ['ROCK', 'PAPER', 'SCISSORS']

# wins -2 1 1
# lose -1 -1 2

while True:
    print(wins, 'Wins,', losses, 'Losses,', ties, 'Ties')
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    selection = input()

    if selection in plays:
        index = plays.index(selection)
        gameChoice = random.randint(0, 2)

        print(titles[index], 'versus...')
        print(titles[gameChoice])

        result = index - gameChoice

        if result == 0:
            ties += 1
            print('It is a tie!')
        elif result == 1 or result == -2:
            wins += 1
            print('You win!')
        else:
            losses += 1
            print('You lose!')
    elif selection == 'q':
        sys.exit()
    else:
        print('Please enter a valid option')