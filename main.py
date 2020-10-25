from locations_and_items import *
from intro_and_events import *


intro()

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
    #updates current location
    look()

def look():
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


    
