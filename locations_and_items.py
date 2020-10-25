# Locations and item function descriptions

def medbay():
    print("You are standing in the medbay. Behind you, a door leads back to the cafeteria.")

def cafeteria(): ########### Missing in other file, needs added
    print("You are in the middle of the cafeteria. Ahead, there is a door to the oxygen \nroom, and above you is the cockpit entrance. To your left is the medbay door, \nand to your right is the crew's quarters. Behind you, there is an entrance to \nyour personal quarters.")

def crew_quarters(): ### make sure names match
    print("You are standing in the crew's quarters. The door ahead leads to the reactor \nroom, and on your right is a storage entrance. Behind you, a door leads to the \ncafeteria.")

def your_quarters(): ### make sure names match
    print("You are in your personal quarters. The engine room lays after the door in front \nof you, and on your left is a storage entrance. A doorway to the cafeteria is \nbehind you.")

def engines():
    print("You are standing in the engine room. The door behind you leads back to your \nquarters.")

def storage():
    print("You are standing in storage. On your left is an entrance to your personal \nquarters, and to your right is an entrance to the crew's quarters.")

def reactor():
    print("You are standing in the reactor room. Behind you, a door leads back to the \ncrew's quarters.")

def oxygen():
    print("You are standing in the oxygen room. The door behind you leads back to the \ncafeteria.")

def cockpit():
    print("You are in the ship's cockpit. The hatch to the cafeteria lays below you.")

"""
### Output testing
medbay()
cafeteria()
crew_quarters()
your_quarters()
engines()
storage()
reactor()
oxygen()
cockpit()
"""

class location:
    def __init__(self, room, up_down, left, right, back, forward):
        self.room = room
        self.up_down = up_down
        self.left = left
        self.right = right
        self.back = back
        self.forward = forward

loc_list = []

'''
# loc_list elements:
0 = medbay
1 = cafeteria
2 = crew_quarters
3 = your_quarters
4 = engines
5 = storage
6 = reactor
7 = oxygen
8 = cockpit
'''

loc_list.append(location("medbay", "", "", "", "cafeteria", ""))
loc_list.append(location("cafeteria", "cockpit", "medbay", "crew_quarters" , "your_quarters", "oxygen"))
loc_list.append(location("crew_quarters", "", "", "storage", "cafeteria", "reactor"))
loc_list.append(location("your_quarters", "", "storage", "", "cafeteria", "engine"))
loc_list.append(location("engines", "", "", "", "your_quarters", ""))
loc_list.append(location("storage", "", "your_quarters", "crew_quarters", "", ""))
loc_list.append(location("reactor", "", "", "", "crew_quarters", ""))
loc_list.append(location("oxygen", "", "", "", "cafeteria", ""))
loc_list.append(location("cockpit", "cafeteria", "", "", "", ""))
