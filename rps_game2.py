# rps_game
import random

player_rps = 'Rock'
computer_rps = 'Rock'

player_score = 0
computer_score = 0

print('#### WELCOME TO ROCK PAPER SCISSORS #####')

for game in range(0, 3):
    player_turn = int(input('\nEnter a number: Rock: 0, Paper: 1, Scissors: 2\n>'))
    computer_turn = random.randint(0, 2)

    match player_turn:
        case 0:
            player_rps = 'Rock'
        case 1:
            player_rps = 'Paper'
        case 2:
            player_rps = 'Scissors'
        case _:
            pass

    match computer_turn:
        case 0:
            computer_rps = 'Rock'
        case 1:
            computer_rps = 'Paper'
        case 2:
            computer_rps = 'Scissors'
        case _:
            pass

    print(f'Player chose {player_rps}, Computer chose {computer_rps}')

    if (player_turn == 3 and computer_turn == 1) or (player_score == 2 and computer_score == 0) or player_turn < computer_turn:
        print('Computer wins this round')
        computer_score += 1
    elif (player_turn == 1 and computer_turn == 3) or (player_turn == 0 and computer_turn == 2) or player_turn > computer_turn:
        print('Player wins this round')
        player_score += 1
    elif player_turn == computer_turn:
        print('This round was a draw')
    else:
        print('Something went wrong')

print(f'\nPlayer_score is {player_score}; Computer score is {computer_score}')
if player_score > computer_score:
    print('Player wins game')
elif player_score < computer_score:
    print('Computer wins game')
else:
    print('Game was a draw')