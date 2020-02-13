from room import Room
from player import Player
from items import Item

# Declare all the rooms



room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", 
                     [Item("flashlight", "Lightens up the room!")]),
    

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("glasses", "improves vision by 10%")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("binoculars", "Vision becomes zoomed in by 20%")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("hammer", "level 1 weapon"), Item("backpack" , "carry up to 5 extra items")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("gold", "You have 10 Gold nuggets"), Item("diamonds", "You have earned 5 diamonds")]),
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

jordan = Player(room['outside'])


# 0 = north(n), 1 = east(e), 2 = south(s) , 3 = west(w)

movements = ['n', 'e', 's', 'w']
leave_game = 'q'

# Write a loop that:
#
#if an if is nested in anotehr if the first if is checked and the second if is checked
#if an if condition is met, the elif condition will not run

x = True

while x:
    #print(f"you are in {room['outside']}")
    player_move = input("~~> ")
    if player_move == leave_game:
        print('Goodbye!!!')
        break
    if len(player_move.split(' ')) == 2:
        if player_move.split(' ')[0] == 'get':
            jordan.get_item(player_move.split(' ')[1])
        elif player_move.split(' ')[0] == 'drop':
            pass
    elif jordan.player_room is room['outside']:
        if  player_move == movements[0]:
            jordan.player_room = room['foyer']
            jordan.get_item(jordan.player_room.items[0])
            print(jordan.player_room)
        else:
            print('Sorry, you can not go that way!')
    elif jordan.player_room is room['foyer']:
        if  player_move == str(movements[2]):
            jordan.player_room = room['outside']
            print(jordan.player_room)
        elif player_move == str(movements[0]):
            jordan.player_room = room['overlook']
            print(jordan.player_room)
        elif player_move == str(movements[1]):
            jordan.player_room = room['narrow']
            print(jordan.player_room)
        elif player_move == str(movements[3]):
            print('Sorry, you can not go that way!')
    elif jordan.player_room is room['overlook']:
        if  player_move == str(movements[2]):
            jordan.player_room = room['foyer']
            print(jordan.player_room)
        else:
            print('Sorry, you can not go that way!')
    elif jordan.player_room is room['narrow']:
        if  player_move == str(movements[0]):
            jordan.player_room = room['treasure']
            print(jordan.player_room)
        elif player_move == str(movements[3]):
            jordan.player_room = room['foyer']
            print(jordan.player_room)    
        else:
            print("sorry you can not go that way!")    
    elif jordan.player_room is room['treasure']:
        if  player_move == str(movements[2]):
            jordan.player_room = room['narrow']
            print(jordan.player_room)
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
