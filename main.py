#main file
import os

os.system('intro_and_events.py')
os.system('locations_and_items')

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

while(input != quit):
    command = input()

    if(command == help):
        help()
    if(command == move):
        move()
    if(command == look):
        look()
    else:
        print("Sorry what was that? Please reenter valid input.")


    
