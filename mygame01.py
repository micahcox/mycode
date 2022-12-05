#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""
import random
import time

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east' : 'Dining Room',
                  'item' : 'golden key' # item with two words and space
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item' : 'monster'
                },

            'Dining Room' : {
                'west' : 'Hall'
            }
         }

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)
    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    
    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if  len(move) < 2:
            print('Get what?')
        # Use == instead of 'in' to prevent substring search
        #   otherwise "ke", "k", etc match "key"
        elif "item" in rooms[currentRoom] and move[1] == rooms[currentRoom]['item']:
            #add the item to their inventory.  Use the dictionary instead of "move[1]"
            # because original and future code may allow substring
            # Ex: "get key" resulted in "key" being in inventory instead of "golden key"
            inventory.append(rooms[currentRoom]['item'])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # seed the random number generator with the current floating point time
    random.seed(time.time()) 
    ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        # Player gets chance to survive
        if random.randint(0, 100) > 75: 
            # Yer dead.
            print('A monster has got you... GAME OVER!')
            break
        else:
            # Run away!  Run away!
            # TODO: Add logic earlier in program to fight back.
            #       "get monster" with random chance of 
            #           putting monster in your "infinite bag of storage"
            print('A monster took a bite out of you... fight back or run!')
     

   