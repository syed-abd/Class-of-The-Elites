##############################################################################
# Title: Class of the Elite
# Assignment: RPG Modules                                                               
# Class: Computer Science 30                                                            
# Date:  May 5th, 2023                                                               
# Coders Name: Abullah Hashmi                                                      
# Version: 003   
##############################################################################
''' This code allows character to access the inventory with items in it '''

# create a 4x5 map with each block containing a setting
# create a 4x5 map with each block containing a setting
map = [
    ["start", "janitor closet", "lab", "washroom", "gym"],
    ["gym", "classroom", "janitor closet", "lab", "washroom"],
    ["washroom", "gym", "classroom", "janitor closet", "lab"],
    ["lab", "washroom", "gym", "classroom", "janitor closet"]
]

tile = {
    "start": {"Description": "Your in the entrance of the school."},
    "classroom": {"Description": "You have entered the classroom take a seat at your desk."},
    "janitor closet": {"Description": "You have entered the janitor closet time to mop the floor."},
    "lab": {"Description": "You have entered the lab the chemical reactions will blow up!"},
    "washroom": {"Description": "You have entered the washroom the toilets smell stinky."},
    "gym": {"Description": "You have entered the gym listen to the loud echos of the basketball."},
}

# define the starting position of the character
x, y = 0, 0

# add empty list for inventory
inventory = []

# create two inventories using nested dictionaries
objects = {
    "pencil": {"description": "A sharp tip for combat", "location": "classroom"},
    "potion": {"description": "A potion that restores health", "location": [None, None]},
    "book": {"description": "A book filled with ancient knowledge", "location": [None, None]}, 
    "key": {"description": "A key that unlocks a mysterious door", "location": [None, None]}
}

def describe_setting(setting):
    '''Describes the setting of the block'''
    print(f"You are in the {setting}. {tile[setting]['Description']}")

def search():
    for obj in objects:
        if objects[obj]["location"] == map[x][y]:
            print(f"You have found {obj}!")
            print(f"{objects[obj]['description']}")
            take_item(obj)

# define a function to access the inventory
def access_inventory():
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Your inventory contains:")
        for item in inventory:
            print(f"- {item}")

# define a function to add an item to the inventory
def take_item(object):
    global inventory
    answer = input(f"Do you want to keep the {object}? (yes, no)")
    if answer == "yes":
        inventory.append(object)
        print(f"You have taken the {object}.")
    elif answer == "no":
        print(f"You did not take the {object}")
    else:
        print("Invalid choice")
        take_item(object)

# define a function to remove an item from the inventory
def drop_item():
    global inventory
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Which item do you want to drop?")
        for item in inventory:
            print(item)
        item_choice = input()
        if item_choice not in inventory:
            print("Invalid item.")
        else:
            inventory.remove(item_choice)
            print(f"You have dropped the {item_choice}.")

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
    mainMenu = input("What do you want to do? (walk, inventory, drop item)")
    
    # update the character's position based on the user's input
    if mainMenu == "walk":
        movement()
        search()
    elif mainMenu == "inventory":
        access_inventory()
    elif mainMenu == "drop item":
        drop_item()
    else:
        print("Invalid")



  