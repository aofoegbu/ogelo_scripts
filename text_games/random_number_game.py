import random
import sys

secret_number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20')

# Ask the user to guess 6 times
print("You have 6 guesses to find the right number")
for guesses_taken in range(1, 7):
    print('Take a guess')
    guess = int(input('>'))
    if guess < secret_number:
        print('Your guess is too low')
    elif guess > secret_number:
        print('Your guess is too high')

    else:
        print('You got the number ' + str(guess) + ' correct.')
        sys.exit()
