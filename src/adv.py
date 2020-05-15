from termcolor import colored, cprint
from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('Sage', room['outside'])
# print(sage)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


directions = {'n': 'n_to', 's': 's_to', 'e': 'e_to', 'w': 'w_to'}
moving = True

while moving:
    print('-------------------------------')
    if player.room.name == 'Outside Cave Entrance':
        print("You are " + player.room.name)
        print(player.room.description)
    elif player.room.name == 'Treasure Chamber':
        cprint("You found the Treasure Chamber!", 'yellow', attrs=['blink'])
        print(player.room.description)
    else:
        print("You are in the " + player.room.name)
        print(player.room.description)

    cprint('Pick a Direction: [n] North [e] East [s] South [w] West [q] Quit', 'blue', attrs=[
           'blink'])
    choice = input("Which way, Gandalf? Input: ")

    if not choice == 'q':
        direction = directions[choice]
        try:
            player.room = getattr(player.room, direction)
        except AttributeError:
            print("Sorry you can't go that way!")
    else:
        print("Thanks for playing!")
        exit()
