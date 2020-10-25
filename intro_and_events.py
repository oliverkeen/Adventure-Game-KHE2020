# Collosal sci-fi adventure
# Kent Hack Enough (KHE) 2020

from locations_and_items import *

# Intro function
def intro():
    # Outputs intro, asks user to choose character
    print("Welcome to Colossal Sci-Fi Adventure! It is the year 2720, and your ship \nFirebird is deep in space, far from any inhabited planets. You, your crewmate, \nand your dog Lucy are on your way home from a top secret mission for the \nGalactic Authority. ", end = '')

    chosen = False
    character = ''

    while (chosen == False):
        character = input("Whom would you like to play as? \n\nMajor Valerian (male) or Sergeant Laureline (female)?\n")

        if (character == "Valerian" or character == "valerian" or character == "Major Valerian" or character == "major valerian"):
            print("Valerian is a young, dark-haired major with several medals of honor.\n")
            confirm = input("Play as Valerian? (Y/n)\n")

            if (confirm == "Yes" or confirm == 'Y' or confirm == "yes" or confirm == 'y'):
                character == "Valerian"
                chosen = True

        elif (character == "Laureline" or character == "laureline" or character == "Sergeant Laureline" or character == "sergeant laureline"):
            character = "Laureline"
            print("Laureline is an intelligent redhead with a fiesty personality.\n")
            confirm = input("Play as Laureline? (Y/n)\n")

            if (confirm == "Yes" or confirm == 'Y' or confirm == "yes" or confirm == 'y'):
                character == "Laureline"
                chosen = True

        else:
            print("Error: Please check your spelling and try again.\n")

    #pick_char(character) # Buggy
    print("\nYou wake up and take in your surroundings...")

    # Call the your quarters function for bedroom description
    your_quarters()

# Event 1 function
def event1():
    print("event 1")

# Event 2 function
def function2():
    print("event 2")

# Event 3 function
def function3():
    print("event 3")

# Ending
