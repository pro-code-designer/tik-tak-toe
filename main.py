import tkinter as tk
from tkinter.font import Font
import random
import os
import time


class Game:
    # -------------------------------------------------------------------------------------------------------------------------------
    # Global variables to keep track of the game state
    def __init__(self):
        self.win_con = False
        self.lose_con = False
        self.lose_place = []
        self.win_place = []
        self.xwin = [0, 0, 0, 0, 0, 0, 0, 0]
        self.owin = [0, 0, 0, 0, 0, 0, 0, 0]
        self.open_corner_house = [0, 2, 6, 8]
        self.open_side_house = [1, 3, 5, 7]
        self.is_finished = 0
        self.house = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]

    # -------------------------------------------------------------------------------------------------------------------------------
    # Restart variables
    def restart(self):
        self.win_con = False
        self.lose_con = False
        self.lose_place = []
        self.win_place = []
        self.xwin = [0, 0, 0, 0, 0, 0, 0, 0]
        self.owin = [0, 0, 0, 0, 0, 0, 0, 0]
        self.open_corner_house = [0, 2, 6, 8]
        self.open_side_house = [1, 3, 5, 7]
        self.is_finished = 0
        self.house = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]
    # -------------------------------------------------------------------------------------------------------------------------------
    # Function to check if 'O' wins

    def check_win(self):
        for a in range(8):
            # Check if the number of Os in a row, column, or diagonal is greater than 1 and number of Xs is 0
            if self.owin[a] > 1 and self.xwin[a] == 0:
                self.win_place.append(a)
                # Set the win condition to True
                self.win_con = True

    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # Function to check if 'X' wins
    def check_lose(self, a):
        # Check if the number of Xs in a row, column, or diagonal is equal to 3
        if self.xwin[a] == 3:
            return True
        # Check if the number of Xs in a row, column, or diagonal is greater than 1 and number of Os is 0
        elif self.xwin[a] > 1 and self.owin[a] == 0:
            self.lose_place.append(a)
            # Set the lose condition to True
            self.lose_con = True
        return False

    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # Function to remove the chosen position from the open_corner_house and open_side_house lists
    def safe_play(self, z):
        try:
            self.open_corner_house.remove(z)
        except:
            pass
        try:
            self.open_side_house.remove(z)
        except:
            pass

    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # Function to update the win/lose conditions of 'X' and 'O'
    def win_adder(self, a, y, x):
        if a == 1:
            self.xwin[y] += 1
            # Check the lose condition after each move
            if(self.check_lose(y)):
                return True
            self.xwin[3+x] += 1
            if(self.check_lose(3+x)):
                return True
            if (x+y) % 2 == 0:
                if x == y:
                    self.xwin[6] += 1
                    if(self.check_lose(6)):
                        return True
                    if x == 1:
                        self.xwin[7] += 1
                        if(self.check_lose(7)):
                            return True
                else:
                    self.xwin[7] += 1
                    if(self.check_lose(7)):
                        return True
            # Check the win condition after each move
            self.check_win()
        else:
            self.owin[y] += 1
            self.owin[3+x] += 1
            if (x+y) % 2 == 0:
                if x == y:
                    self.owin[6] += 1
                    if x == 1:
                        self.owin[7] += 1
                else:
                    self.owin[7] += 1
        return False

    # -------------------------------------------------------------------------------------------------------------------------------
    # The first turn is determined randomly by generating a random integer value between 1 and 2
    # If turn is 1, player's turn to choose a square
    # If turn is 0, computer's turn to choose a square

    def play(self,x,y):
            self.house[y][x] = 'X'
            if(self.win_adder(1, y, x)):
                return True
            z=x*3+y
            self.safe_play(z)
            return False
    def bot_play(self):
        print(self.lose_con)
        if self.win_con:
            s = int(self.win_place[0]/3)
            t = self.win_place[0] % 3
            if s == 0:
                for h in range(3):
                    if self.house[t][h].isdigit():
                        self.house[t][h] = 'O'
                        return  True,h,t
            elif s == 1:
                for h in range(3):
                    if self.house[h][t].isdigit():
                        self.house[h][t] = 'O'
                        return  True,t,h
            elif t == 0:
                for h in range(3):
                    if self.house[h][h].isdigit():
                        self.house[h][h] = 'O'
                        return  True,h,h
            else:
                for h in range(3):
                    t = 2-h
                    if t < 0:
                        t = -t
                    if self.house[h][t].isdigit():
                        self.house[h][t] = 'O'
                        return  True,t,h
        elif self.lose_con:
            s = int(self.lose_place[0]/3)
            t = self.lose_place[0] % 3
            if s == 0:
                for h in range(3):
                    if self.house[t][h].isdigit():
                        self.house[t][h] = 'O'
                        self.win_adder(0, t, h)
                        self.safe_play(t*3+h)
                        self.lose_place.remove(self.lose_place[0])
                        if not self.lose_place:
                            self.lose_con = False
                        return  False,h,t
            elif s == 1:
                for h in range(3):
                    if self.house[h][t].isdigit():
                        self.house[h][t] = 'O'
                        self.win_adder(0, h, t)
                        self.safe_play(h*3+t)
                        self.lose_place.remove(self.lose_place[0])
                        if not self.lose_place:
                            self.lose_con = False
                        return  False,t,h
            elif t == 0:
                for h in range(3):
                    if self.house[h][h].isdigit():
                        self.house[h][h] = 'O'
                        self.win_adder(0, h, h)
                        self.safe_play(h*3+h)
                        self.lose_place.remove(self.lose_place[0])
                        if not self.lose_place:
                            self.lose_con = False
                        return  False,h,h
            else:
                for h in range(3):
                    t = 2-h
                    if t < 0:
                        t = -t
                    if self.house[h][t].isdigit():
                        self.house[h][t] = 'O'
                        self.win_adder(0, h, t)
                        self.safe_play(h*3+t)
                        self.lose_place.remove(self.lose_place[0])
                        if not self.lose_place:
                            self.lose_con = False
                        return  False,t,h
        elif self.open_corner_house:
            random_item = random.choice(self.open_corner_house)
            y = int(random_item/3)
            x = random_item % 3
            self.open_corner_house.remove(random_item)
            self.house[y][x] = 'O'
            self.win_adder(0, y, x)
            return False,x,y
        elif self.house[1][1].isdigit() == True:
            self.house[1][1] = 'O'
            self.win_adder(0, 1, 1)
            return False,1,1
        else:
            random_item = random.choice(self.open_side_house)
            y = int(random_item/3)
            x = random_item % 3
            self.open_side_house.remove(random_item)
            self.house[y][x] = 'O'
            self.win_adder(0, y, x)
            return False,x,y


class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.game = Game()
        self.master.title("Tic Tac Toe")
        self.master.resizable(False, False)
        self.master.config(bg="#0E0F18")

        # create a 3x3 grid of buttons
        self.buttons = [[tk.Button(self.master, width=8, height=4, font=Font(family="Segoe UI", size=18), bg="#7C8196", fg="#F5F5F5",
                                   borderwidth=0, command=lambda row=row, column=column: self.button_click(row, column)) for column in range(3)] for row in range(3)]

        # place the buttons on the grid
        for row in range(3):
            for column in range(3):
                self.buttons[row][column].grid(
                    row=row, column=column, padx=5, pady=5)

        # create label for announcing winner
        self.winner_label = tk.Label(self.master, font=Font(
            family="Segoe UI", size=24), bg="#0E0F18", fg="#F5F5F5")

        # initialize game state
        self.player = "X"
        self.enemy="O"
        self.game_over = False
        self.turn = random.randint(1, 2)
        self.full_house_nummber=0
        print(self.turn)

        # create menu bar
        self.menu_bar = tk.Menu(master)
        self.master.config(menu=self.menu_bar)

        # create Game menu
        self.game_menu = tk.Menu(self.menu_bar, tearoff=False, bg="#0E0F18",
                                 fg="#F5F5F5", font=Font(family="Segoe UI", size=14))
        self.game_menu.add_command(label="New Game", command=self.new_game)
        self.game_menu.add_separator()
        self.game_menu.add_command(label="Exit", command=master.quit)
        self.menu_bar.add_cascade(label="Game", menu=self.game_menu)
        if(self.turn==2):
            self.bot_play()

    def button_click(self, row, column):
        if not self.game_over:
            button = self.buttons[row][column]
            print(row," ",column)
            if button["text"] == "":
                button["text"] = self.player
                button.config(bg="#00B7C2")
                self.full_house_nummber+=1
                if(self.game.play(row,column)):
                    self.game_over = True
                    self.show_winner()
                elif(self.full_house_nummber==9):
                    self.game_over = True
                    self.show_tie()
                else:
                    self.bot_play()
                    
    def bot_play(self):
        lose,x,y=self.game.bot_play()
        button = self.buttons[x][y]
        print(x," ",y)
        button["text"] = self.enemy
        button.config(bg="#FF4875")
        button = self.buttons[x][y]
        self.full_house_nummber+=1
        if(lose):
            self.game_over = True
            self.show_loser()
        elif(self.full_house_nummber==9):
            self.game_over = True
            self.show_tie()

    def show_winner(self):
        winner = "You win!"
        self.winner_label.config(text=winner)
        self.winner_label.grid(row=3, column=0, columnspan=3)

    
    def show_loser(self):
        winner = "You lose!"
        self.winner_label.config(text=winner)
        self.winner_label.grid(row=3, column=0, columnspan=3)

    
    def show_tie(self):
        winner = "Tie"
        self.winner_label.config(text=winner)
        self.winner_label.grid(row=3, column=0, columnspan=3)


    def new_game(self):
        # clear the board
        for row in self.buttons:
            for button in row:
                button["text"] = ""
                button.config(bg="#7C8196")
        # reset game state
        self.current_player = "X"
        self.game_over = False
        self.full_house_nummber=0
        # hide winner label
        self.winner_label.grid_remove()
        self.game.restart()
        self.turn = random.randint(1, 2)
        if(self.turn==2):
            self.bot_play()


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
