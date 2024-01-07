import random, sys

print('I am thinking of a number between 1 and 20.')

num = random.randint(1, 20)
guesses = 0

while True:
    guess = input('Take a guess: ')
    if guess.isnumeric():
        intGuess = int(guess)
        guesses += 1
        if intGuess > num:
            print('Your number is too high.')
        elif intGuess < num:
            print('Your number us too low.')
        else:
            print('Good job! You guessed my number in', guesses, 'guesses!')
            sys.exit()
    else:
        print('You need to enter a number.')
