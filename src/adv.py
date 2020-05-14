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

sage = Player('sage', 'outside')
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


# I don't there's a need to do this but I'm trying anything at this point
outside = room['outside']
foyer = room['foyer']
overlook = room['overlook']
narrow = room['narrow']
treasure = room['treasure']

# Test
print("60", outside.description)

# Defines current room and description
# can this work as my "current room?" class Sage => 'description'
print("61", sage)
# doesn't seem to work
description = room[sage.__str__()].__str__()

# Prints current room name and description
print("65 Current Room: " + sage.__str__() +
      "\nDescription: " + description)

# Initiate user input
user = str(input("[w] North [d] East [s] South [a] West [q] Quit"))

# Start loop
while not user == 'q':

    # # Defines current room and description
    # currentRoom = sage.location
    # print("65", currentRoom)
    # description = room[currentRoom].description

    # # Prints current room name and description
    # print("69 Current Room: " + currentRoom +
    #       "\nDescription: " + description)

    # Handles user input
    if user == 'w':
        # Tried a bunch of stuff but \/ this => KeyError: '<room.Room object at 0x01323D60>'
        sage.location = room[f"{sage.__str__()}"].n_to
        print("86", sage.location)
    elif user == 'd':
        sage.location = room[sage.__str__()].e_to
    elif user == 's':
        sage.location = room[sage.__str__()].s_to
    elif user == 'a':
        sage.location = room[sage.__str__()].w_to
    else:
        print("Invalid selection. Please try again.")

    # # Prints current room name and description
    # print("97 Current Room: " + sage.__str__() +
    #       "\nDescription: " + description)
    # # User input
    # user = str(input("[w] North [d] East [s] South [a] West [q] Quit"))

print("Thanks for playing!")
