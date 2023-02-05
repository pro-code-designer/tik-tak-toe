import os
import time
import random


# -------------------------------------------------------------------------------------------------------------------------------
# Global variables to keep track of the game state
win_con = False
lose_con = False
open_corner_house = [0, 2, 6, 8]
open_side_house = [1, 3, 5, 7]
is_finished = 0
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
# The game continues until 9 moves have been made (all squares have been filled) or until a player wins
while is_finished != 9:
    if turn == 1:
        first = True
        x = 0
        y = 0
        # If the player selects an invalid square, the turn continues until a valid square is selected
        while first or not house[y][x].isdigit():
            first = False
            print_board()
            print("select number=")
            try:
                z = input()
            except:
                continue
            if z.isdigit():
                z = int(z)
                y = int(z/3)
                x = z % 3
            else:
                continue
        house[y][x] = 'X'
        print_board()
        turn = 0
    else:
        print('computer is thinking.......')
        time.sleep(1.5)
        if win_con:
            pass
        elif lose_con:
            pass
        elif open_corner_house:
            random_item = random.choice(open_corner_house)
            y = int(random_item/3)
            x = random_item % 3
            open_corner_house.remove(random_item)
            house[y][x] = 'O'
        elif house[1][1].isdigit() == True:
            house[1][1] = 'O'
        else:
            random_item = random.choice(open_side_house)
            y = int(random_item/3)
            x = random_item % 3
            open_side_house.remove(random_item)
            house[y][x] = 'O'
        print_board()
        turn = 1
    is_finished += 1

print('TIE')