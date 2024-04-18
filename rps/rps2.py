import sys
import random
from enum import Enum

class RPS(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

playagain = True

while playagain:
    playerchoice = input('\nEnter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n')

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit('You must enter 1, 2 or 3.')

    computerchoice = random.choice('123')
    computer = int(computerchoice)

    print('\nYou chose ' +  str(RPS(player)).replace ('RPS.', '') + '.')
    print('Python chose ' +  str(RPS(computer)).replace('RPS.', '') + '.\n')

    if player == 1 and computer == 3:
        print('🎉 You win!')
    elif player == 2 and computer == 1:
        print('🎉 You win!')
    elif player == 3 and computer == 2:
        print('🎉 You win!')
    elif player == computer:
        print('🤝 Tie game!')
    else:
        print('🐍 Python wins')

    playagain = input('Do you want to play again? \nY for Yes, N for No\n')

    if playagain.lower() == 'y':
        continue
    else:
        print('\nThank you for playing!\n')
        break

sys.exit('Till next time boss!')

