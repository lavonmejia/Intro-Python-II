from room import Room
from player import Player
from item import Item

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

items = {
    'mallet': Item('Rock', 'a smooth rock just small enough to fit in your pocket'),
    'notebook': Item('Cobweb', 'A cobweb clings loosely to the walls just above you..'),
    'satchel': Item('Gold Coin', 'A single piece of gold that seems to have lost its luster from aging'),
    'water': Item('Lit Torch', 'A dimly lit torch that helps you find your way in dark places'),
    'monster_parts': Item('Sword', 'A heavy Sword that mysteriously hasn\'t gone dull'),
    'potion': Item('Empty Chest', 'A chest that seems to have once held great treasures, but now is dusty and long since been emptied..'),
    'matches': Item('Chalice', 'A gold chalice left behind by whoever emptied the treasure chamber')
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


# Link items to rooms

room['outside'].add_item(items['mallet']) 
room['foyer'].add_item(items['notebook'])
room['foyer'].add_item(items['satchel'])
room['overlook'].add_item(items['water'])
room['overlook'].add_item(items['monster_parts'])
room['narrow'].add_item(items['potion'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'], 'Human', 'Paladin')



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


while True:
# game opens
    print()
    print(f"YOU, a {player.species},{player.job} are currently in the {player.room.name}.\n")
    print(f"Look around, {player.room.description}.\n")
    print(f"In this room, there is a: {player.room.items}")
    print()

# repeat turn prompt to select move or action 
    command = input("Would you like to move or do an action? Push m for move or a for action" )
    if command not in ('m', 'a'):
        print('Must select m or a, please try again.') 


# if action selected
# something wrong with first line
    if command == 'a' and player.room is room['outside']: 
        print(f"{player.species},{player.job} is dancing.")
    elif command == 'a' and {player.room.name} is not {room['outside'].name}:
        input("Would you like to know which items are in the room?")
    
# if move selected
    elif command == 'm': 
       command = input("Where would you like to go? You can try to go n, s, e, w or exit by typing 'q'.\n")
    else: 
        if command not in ('n', 's', 'e', 'w', 'q'):
            print("That command was not recognized, please try again. The valid options are 'n', 's', 'e', 'w' or exit by typing 'q'.\n")
        else:
            if command == 'n' and player.room.n_to is not None:
                player.room = player.room.n_to
                # print(player.room)
            elif command == 's' and player.room.s_to is not None:
                player.room = player.room.s_to
                # print(player.room)
            elif command == 'e' and player.room.e_to is not None:
                 player.room = player.room.e_to
                #  print(player.room)
            elif command == 'w' and player.room.w_to is not None:
                player.room = player.room.w_to
                # print(player.room)
            else:
                print("You have hit a wall, please try again!")


# if quit selected 
    if command == 'q':
        print('Fare Thee Well!\n')
        exit()

 