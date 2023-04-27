##############################################################################
# Title: RPG Map                                                               
# Class: Computer Science 30                                                            
# Date:  March 15, 2023                                                               
# Coders Name: Abullah Hashmi                                                        
# Version: 001   
##############################################################################
'''This assignment is a code that constructs a map in which allows the
character to move into a different room in the map
Current Assignment:
Explain the whole Program here
'''
#-----------------------------------------------------------------------------
# create a 4x5 map with each block containing a setting
map = [
    ["classroom", "janitor closet", "lab", "washroom", "gym"],
    ["gym", "classroom", "janitor closet", "lab", "washroom"],
    ["washroom", "gym", "classroom", "janitor closet", "lab"],
    ["lab", "washroom", "gym", "classroom", "janitor closet"]
]
# define the starting position of the character
x, y = 0, 0

# define a function to describe the setting of the block
def describe_setting(setting):
    if setting == "classroom":
        print("You have entered the classroom take a seat at your desk.")
    elif setting == "janitor closet":
        print("You have entered the janitor closet time to mop the floor.")
    elif setting == "lab":
        print("You have entered the lab the chemical reactions will blow up!")
    elif setting == "washroom":
        print("You have entered the wasroom the toilets smell stinky.")
    elif setting == "gym":
        print("You have entered the gym listen to the loud echos of the basketball.")


def movement():
    '''Determines where the charcter will move'''
    global x, y
    thinking = True
    warning = "You have reached the edge of the map!"
    while thinking:
        # ask the user where to move next
        direction = input("Where do you want to go? (north, south, west, east) ")
        # update the character's position based on the user's input
        if direction == "north":
          if y != 0:
            y -= 1
            thinking = False
          else:
            print(warning)
        elif direction == "south":
          if y != 3:
            y += 1
            thinking = False
          else:
            print(warning) 
        elif direction == "west":
          if y != 0:
            x -= 1
            thinking = False
          else:
            print(warning)
        elif direction == "east":
           if y != 4:
             x += 1
             thinking = False
           else:
            print(warning)
        else:
          print("Invalid")

      
# loop through the map and describe the setting when the character moves into a block
while True:
    setting = map[y][x]
    describe_setting(setting)
    
    # ask the user where to move next
    mainMenu = input("What do you want to do? (walk)")
    
    # update the character's position based on the user's input
    if mainMenu == "walk":
        movement()
    else:
        print("Invalid")