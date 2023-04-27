##############################################################################
# Title: RPG Inventory                                                               
# Class: Computer Science 30                                                            
# Date:  April 18, 2023                                                               
# Coders Name: Abullah Hashmi                                                      
# Version: 002   
##############################################################################
''' This code allows character to access the inventory with items in it '''

# Create a dictionary to hold inventory
inventory = {
    'pencil': 10,
    'eraser': 5,
    'mop': 1,
    'map': 1,
    'calculator': 1,
    'marker': 1
}

# Define a function to display the player's inventory
def display_inventory():
    print("Your inventory:")
    for item, count in inventory.items():
        print(f"{item}: {count}")

# Call the display_inventory function to show the initial inventory
display_inventory()

# Define a function to add an item to the player's inventory
def add_item(item, count=1):
    if item in inventory:
        inventory[item] += count
    else:
        inventory[item] = count
    print(f"{count} {item} added to your inventory.")

# Define a function to remove an item from the player's inventory
def remove_item(item, count=1):
    if item in inventory:
        if inventory[item] >= count:
            inventory[item] -= count
            print(f"{count} {item} removed from your inventory.")
        else:
            print(f"You don't have {count} {item} in your inventory.")
    else:
        print(f"You don't have {item} in your inventory.")

# Call the add_item function to add a new item to the inventory
add_item('marker', 1)

# Call the remove_item function to remove an item from the inventory
remove_item('map', 1)

# Call the display_inventory function again to show the updated inventory
display_inventory()
