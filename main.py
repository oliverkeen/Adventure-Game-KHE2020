from locations_and_items import *
from intro_and_events import *

intro()

room = 3

def help():
    print('''
Commands include:
help
move
look
quit
''')

def move():
    #gets input for which way you are moving
    # make sure that move input is valid
    #updates current location to the room in the direction chosen i.e. room = 2
    look()

def look():
    #figure out current room
    if (room == 3):
        your_quarters()
        
    #call description function for that room
    print("look function called")
    
command = "puppy"

while(command != quit):
    command = input()

    if(command == "help"):
        help()
    if(command == "move"):
        move()
    if(command == "look"):
        look()


    
