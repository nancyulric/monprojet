# Import the choice function of the random module
# https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list

# Assign to a list the 3 possible options: 'stone', 'paper' or 'scissors'.

# Assign a variable to the maximum number of games: 1, 3, 5, etc ...

# Assign a variable to the number of games a player must win to win.
# Preferably the value will be based on the number of maximum games

# Define a function that randomly returns one of the 3 options.
# This will correspond to the play of the machine. Totally random
import random


def machine_player_choice():
    """this fonction indicate the machine choice"""
    machine_player = ('stone', 'paper', 'scissors')
    print(random.choice(machine_player))
    return (machine_player_choice)

# Define a function that asks your choice: 'stone', 'paper' or 'scissors'
# you should only allow one of the 3 options. This is defensive programming.
# If it is not stone, paper or scissors keep asking until it is.


options = ('stone', 'paper', 'scissors')
def human_player_choice():
    while 1:
        options = input("Enter your sign:")
        if options == "stone":
            break
        if options == "paper":
            break
        if options == "scissors":
            break
        else:
            print("You must enter a sign!!!")
        return humain_player_choice

print(input("Enter your sign:"))


