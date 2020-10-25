### Kiersten Campbell and Oliver Keen
### Adventure Game main function implementation
### Kent Hack Enough (KHE) 24-hour hackathon
### 10/25/2020

from locations_and_items import *
from intro_and_events import *

intro()  # Player chooses character
curr_room = 3 # Game starts in personal quarters

def print_help():
    print("Commands: help, move, look, quit")

player = "Lucy" # Buggy in main, needs defined somewhere else or implemented differently, too tired to know for sure it's 6am my dude
def pick_char(choice):
    if choice == "Valerian":
        player = "Valerian"
    elif choice == "Laureline":
        player = "Laureline"

def set_room(curr_room, direction): # My eureka moment at 5:40am
    if direction == up or direction == down:
        direction = up_down # Adjusts input for unique location member

    new_room = "Your mom's house"
    valid_dir = False

    while valid_dir == False:
        for i in loc_list:
            if curr_room == i.room_n:
                if i.direction != "":
                    valid_dir = True
                    for j in loc_list:
                        if j.room == i.direction:
                            new_room = j.room_n
                else:
                    print("Error: Invalid direction, please try again.")
                    break
    
    # loop through loc_list until you find the current room
    # check that direction is valid

    return new_room

def move():
    direction = "I fart in your general direction"
    valid_dir = False

    while valid_dir == False:
        direction = input("Direction: ")

        if ((direction == "up" or direction == "down") and loc_list[curr_room].up_down != ""):
            valid_dir = True
            curr_room = set_room(curr_room, direction)
            #curr_room = loc_list
        elif (direction == "left" and loc_list[curr_room].left != ""):
            valid_dir = True
            #curr_room =
        elif (direction == "right" and loc_list[curr_room].right != ""):
            valid_dir = True
            #curr_room =
        elif ((direction == "back" or direction == "backward" or direction == "backwards") and loc_list[curr_room].back != ""):
            valid_dir = True
            #curr_room =
        elif ((direction == "forward" or direction == "forwards") and loc_list[curr_room].forward != ""):
            valid_dir = True
            #curr_room =
        else:
            print("Error: Invalid direction, please try again.")

        # Make sure direction is valid
    #updates current location to the room in the direction chosen
    look()

def look(): # Prints current room description
    if curr_room == 0:
        medbay()
    if curr_room == 1:
        cafeteria()
    if curr_room == 2:
        crew_quarters()
    if curr_room == 3:
        your_quarters()
    if curr_room == 4:
        engines()
    if curr_room == 5:
        storage()
    if curr_room == 6:
        reactor()
    if curr_room == 7:
        oxygen()
    if curr_room == 8:
        cockpit()

command = "puppy"

while command != "quit":
    command = input()

    if command == "help":
        print_help()
    elif command == "move":
        move()
    elif command == "look":
        look()
    elif command == "debug":
        print("Player = " + player + "\ncurr_room = " + room)
    elif command != "quit":
        print("Error: Invalid command, type \"help\" to print list of possible commands.")

print("Closing...")
    
