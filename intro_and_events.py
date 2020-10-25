#collosal scifi adventure
#KHE 2020



#intro function
def intro():
    print('''
Welcome to Colossal SciFi Adventure. It is the year 2720
and your spaceship, Firebird, is deep in space far from any
inhabited planets. You, your partner and your dog Lucy are on
your way home from a top secret mission for the Galactic Authority.

Which character would you like to play as? Major Valerian (male) or
Laureline (female)?
'''
#pick a character and output character description
    character = input()

    if(character == 'Valerian' or character == 'valerian'):
          print("description of Valerian")
    if(character == 'Laureline' or character == 'laureline'):
          print("description of Laureline")
    else:
        print("Error. Please enter valid input.")

    print("You wake up and look around you.")

    #call the your quarters function for bedroom description
    your_quarters()

#event 1 function
def function1():

#event 2 function
def function2():

#event 3 function
def function3():

#ending
