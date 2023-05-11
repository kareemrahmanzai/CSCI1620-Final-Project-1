import tkinter
import random
from tkinter import *

root = Tk()
root.title = ("Rock, Paper, Scissors")
root.geometry("300x300")

rand_int = random.randint(0,2)

if rand_int == 0:
    random_choice = 'Rock'
elif rand_int == 1:
    random_choice = 'Papaer'
elif rand_int == 2:
    random_choice = 'Scissors'


def rock():
    player_choice_label['text'] = 'Player Chooses: ROCK'

    if random_choice == 'Rock':
        result['text'] = 'Tie!'
        random_choice_label['text'] = 'Computer Chooses: ROCK'
    elif random_choice == 'Paper':
        result['text'] = 'PAPER Beats ROCK. Computer Wins!'
        random_choice_label['text'] = 'Computer Chooses: PAPER'
    elif random_choice == 'Scissors':
        result['text'] = 'ROCK Beats SCISSORS. Player Wins!'
        random_choice_label['text'] = 'Computer Chooses: SCISSORS'

def paper():
    player_choice_label['text'] = 'Player Chooses: PAPER'

    if random_choice == "Paper":
        result['text'] = "Tie!"
        random_choice_label['text'] = 'Computer Chooses: PAPER'
    elif random_choice == "Scissors":
        result['text'] = "SCISSORS Beats PAPER. Computer wins!"
        random_choice_label['text'] = 'Computer Chooses: SCISSORS'
    elif random_choice == "Rock":
        result['text'] = "PAPER Beats ROCK. Player wins!"
        random_choice_label['text'] = 'Computer Chooses: ROCK'

def scissors():
    player_choice_label['text'] = 'Player Chooses: SCISSORS'

    if random_choice == "Scissors":
        result['text'] = "Tie!"
        random_choice_label['text'] = 'Computer Chooses: SCISSORS'
    elif random_choice == "Rock":
        result['text'] = "ROCK Beats SCISSORS. Computer wins!"
        random_choice_label['text'] = 'Computer Chooses: ROCK'
    elif random_choice == "Paper":
        result['text'] = "SCISSORS Beats PAPER. Player wins!"
        random_choice_label['text'] = 'Computer Chooses: PAPER'

def reset():
    global random_choice
    rand_int = random.randint(0, 2)
    if rand_int == 0:
        random_choice = 'Rock'
    elif rand_int == 1:
        random_choice = 'Paper'
    elif rand_int == 2:
        random_choice = 'Scissors'


result = tkinter.Label(root, text="Choose Either Rock, Paper, or Scissors")
result.pack()

rock = tkinter.Button(root, text="ROCK", command=rock)
rock.pack()

paper = tkinter.Button(root, text="PAPER", command=paper)
paper.pack()

scissors = tkinter.Button(root, text="SCISSORS", command=scissors)
scissors.pack()

random_choice_label = tkinter.Label(root, text="")
random_choice_label.pack()

player_choice_label = tkinter.Label(root, text="")
player_choice_label.pack()

reset = tkinter.Button(root, text="RESET", command=reset)
reset.pack()


root.mainloop()
