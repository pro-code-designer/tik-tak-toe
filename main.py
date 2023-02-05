import random
from termcolor import colored
import os
import time


# -------------------------------------------------------------------------------------------------------------------------------
# Global variables to keep track of the game state
win_con = False
lose_con = False
lose_place = []
win_place = []
xwin = [0, 0, 0, 0, 0, 0, 0, 0]
owin = [0, 0, 0, 0, 0, 0, 0, 0]
open_corner_house = [0, 2, 6, 8]
open_side_house = [1, 3, 5, 7]
is_finished = 0
house = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]


# -------------------------------------------------------------------------------------------------------------------------------
# Function to check if 'O' wins
def check_win():
    global win_con
    for a in range(8):
        # Check if the number of Os in a row, column, or diagonal is greater than 1 and number of Xs is 0
        if owin[a] > 1 and xwin[a] == 0:
            win_place.append(a)
            # Set the win condition to True
            win_con = True

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Function to check if 'X' wins
def check_lose(a):
    global lose_con
    # Check if the number of Xs in a row, column, or diagonal is equal to 3
    if xwin[a] == 3:
        print(colored("YOU WON", 'green'))
        # End the game
        quit()
    # Check if the number of Xs in a row, column, or diagonal is greater than 1 and number of Os is 0
    elif xwin[a] > 1 and owin[a] == 0:
        lose_place.append(a)
        # Set the lose condition to True
        lose_con = True

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Function to print the current board state
def print_board():
    os.system('cls')
    for x in house:
        print("|", end='')
        for y in x:
            if y == 'O':
                print(colored(y, 'red'), end='|')
            elif y == 'X':
                print(colored(y, 'green'), end='|')
            else:
                print(y, end='|')
        print('\n-------')

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Function to remove the chosen position from the open_corner_house and open_side_house lists
def safe_play(z):
    try:
        open_corner_house.remove(z)
    except:
        pass
    try:
        open_side_house.remove(z)
    except:
        pass

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Function to update the win/lose conditions of 'X' and 'O'
def win_adder(a, y, x):
    if a == 1:
        xwin[y] += 1
        # Check the lose condition after each move
        check_lose(y)
        xwin[3+x] += 1
        check_lose(3+x)
        if (x+y) % 2 == 0:
            if x == y:
                xwin[6] += 1
                check_lose(6)
                if x == 1:
                    xwin[7] += 1
                    check_lose(7)
            else:
                xwin[7] += 1
                check_lose(7)
        # Check the win condition after each move
        check_win()
    else:
        owin[y] += 1
        owin[3+x] += 1
        if (x+y) % 2 == 0:
            if x == y:
                owin[6] += 1
                if x == 1:
                    owin[7] += 1
            else:
                owin[7] += 1


# -------------------------------------------------------------------------------------------------------------------------------
# The first turn is determined randomly by generating a random integer value between 1 and 2
# If turn is 1, player's turn to choose a square
# If turn is 0, computer's turn to choose a square
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
        win_adder(1, y, x)
        safe_play(z)
        turn = 0
    else:
        print('computer is thinking.......')
        time.sleep(1.5)
        if win_con:
            s = int(win_place[0]/3)
            t = win_place[0] % 3
            if s == 0:
                for h in range(3):
                    if house[t][h].isdigit():
                        house[t][h] = 'O'
            elif s == 1:
                for h in range(3):
                    if house[h][t].isdigit():
                        house[h][t] = 'O'
            elif t == 0:
                for h in range(3):
                    if house[h][h].isdigit():
                        house[h][h] = 'O'
            else:
                for h in range(3):
                    t = 2-h
                    if t < 0:
                        t = -t
                    if house[h][t].isdigit():
                        house[h][t] = 'O'
            print_board()
            print(colored("YOU LOSE", 'red'))
            quit()
        elif lose_con:
            s = int(lose_place[0]/3)
            t = lose_place[0] % 3
            if s == 0:
                for h in range(3):
                    if house[t][h].isdigit():
                        house[t][h] = 'O'
                        win_adder(0, t, h)
                        safe_play(t*3+h)
            elif s == 1:
                for h in range(3):
                    if house[h][t].isdigit():
                        house[h][t] = 'O'
                        win_adder(0, h, t)
                        safe_play(h*3+t)
            elif t == 0:
                for h in range(3):
                    if house[h][h].isdigit():
                        house[h][h] = 'O'
                        win_adder(0, h, h)
                        safe_play(h*3+h)
            else:
                for h in range(3):
                    t = 2-h
                    if t < 0:
                        t = -t
                    if house[h][t].isdigit():
                        house[h][t] = 'O'
                        win_adder(0, h, t)
                        safe_play(h*3+t)
            lose_place.remove(lose_place[0])
            if not lose_place:
                lose_con = False
        elif open_corner_house:
            random_item = random.choice(open_corner_house)
            y = int(random_item/3)
            x = random_item % 3
            open_corner_house.remove(random_item)
            house[y][x] = 'O'
            win_adder(0, y, x)
        elif house[1][1].isdigit() == True:
            house[1][1] = 'O'
            win_adder(0, 1, 1)
        else:
            random_item = random.choice(open_side_house)
            y = int(random_item/3)
            x = random_item % 3
            open_side_house.remove(random_item)
            house[y][x] = 'O'
            win_adder(0, y, x)
        print_board()
        turn = 1

    is_finished += 1

print('TIE')
