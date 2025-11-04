import random, sys


rock, paper, scissors = 0,1,2
computer_score, user_score = 0,0

print('#### ROCK PAPER SCISSORS ####')

for current_turn in range(0,3):

    print(f'\nRound {current_turn} \nEnter a number: 0: rock, 1: paper, 2: scissors')
    user_choice = int(input('>'))
    computer_choice = random.randint(0, 3)
    print(f'User choice: {user_choice}, Computer choice: {computer_choice}' )

    if user_choice == computer_choice:
        print('Draw in this round')
    elif (user_choice == 1 and computer_choice == 2 ) or (user_choice == 2  and computer_choice == 3) or (user_choice == 3 and computer_choice == 0) or (user_choice == 2 and computer_choice == 0) or (user_choice == 1 and computer_choice == 3):
        print('Computer wins this round')
        computer_score += 1
    elif (user_choice == 2 and computer_choice == 1 ) or (user_choice == 3  and computer_choice == 2) or (user_choice == 0 and computer_choice == 3)  or (user_choice == 0 and computer_choice == 2) or (user_choice == 3 and computer_choice == 1):
        print('User wins this round')
        user_score += 1

    print(f'Current Score: User:{user_score}, Computer: {computer_score}')

print(f'\nFinal Score: User:{user_score}, Computer: {computer_score}')
if user_score == computer_score:
    print("It's a tie")
elif user_score < computer_score:
    print('You lose')
else:
    print('You win')


