import os
import random


# -------------------------------------------------------------------------------------------------------------------------------
# Global variables to keep track of the game state
house = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Function to print the current board state
def print_board():
    os.system('cls')
    for x in house:
        print("|", end='')
        for y in x:
            if y == 'O':
                print(y, end='|')
            elif y == 'X':
                print(y, end='|')
            else:
                print(y, end='|')
        print('\n-------')

# -------------------------------------------------------------------------------------------------------------------------------
# The first turn is determined randomly by generating a random integer value between 1 and 2
# If turn is 1, player's turn and 0 stands for computer's turn
turn = random.randint(1, 2)
print_board()