from room import Room
from player import Player

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
#______________________
#_____|__ok___||___t___
#_____|___f____|___n___
#_____|___os___|_______

# Make a new player object that is currently in the 'outside' room.

jordan = Player('outside')
print(jordan.inventory)

# 0 = north(n), 1 = east(e), 2 = south(s) , 3 = west(w)

movements = ['n', 'e', 's', 'w']
leave_game = 'q'

# Write a loop that:
#
#if an if is nested in anotehr if the first if is checked and the second if is checked
#if an if condition is met, the elif condition will not run

x = True
while x:
    player_move = input("~~> ")
    if player_move == leave_game:
        print('Goodbye!!!')
        break
    if jordan.player_room is 'outside':
      if player_move == movements[0]:
          jordan.player_room = 'foyer'
          print(f"{room['outside'].n_to.name}, \n {room['outside'].n_to.description}")
      else:
          print('Sorry, you can not go that way!')
    elif jordan.player_room is 'foyer':
        if player_move == str(movements[2]):
            print(f"{room['foyer'].s_to.name}, \n {room['foyer'].s_to.description}")
            jordan.player_room = 'outside'
        elif player_move == str(movements[0]):
            print(f"{room['foyer'].n_to.name}, \n {room['foyer'].n_to.description}")
            jordan.player_room = 'overlook'
        elif player_move == str(movements[1]):
            print(f"{room['foyer'].e_to.name}, \n {room['foyer'].e_to.description}")
            jordan.player_room = 'narrow'
        elif player_move == str(movements[3]):
            print('Sorry, you can not go that way!')
    elif jordan.player_room is 'overlook':
        if player_move == str(movements[2]):
            print(f"{room['overlook'].s_to.name}, \n {room['overlook'].s_to.description}")
            jordan.player_room = 'foyer'
        else:
            print('Sorry, you can not go that way!')
    elif jordan.player_room is 'narrow':
        if player_move == str(movements[0]):
            print(f"{room['narrow'].n_to.name}, \n {room['narrow'].n_to.description}")
            jordan.player_room = 'treasure'
        elif player_move == str(movements[3]):
            print(f"{room['narrow'].w_to.name}, \n {room['narrow'].w_to.description}")
            jordan.player_room = 'foyer'    
        else:
            print("sorry you can not go that way!")    
    elif jordan.player_room is 'treasure':
        if player_move == str(movements[2]):
            print(f"{room['treasure'].s_to.name}, \n {room['treasure'].s_to.description}")
            jordan.player_room = 'narrow'
        else:
            print('you can not go that way!')                

            

    

    






   
    

    
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
