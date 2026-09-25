"""
Author:         Jessica Weiss
Date:           December 3, 2024
Assignment:     Project 02
Course:         CPSC1050
Section:        003

CODE DESCRIPTION: Use multiple files to code an escape room containing a main file that executes the code, as well as 4 files that contain classes to be called
                  multiple times and 1 file containing a custom error. In the main file, call the classes and functions, and execute the code using
                  try and except functions to raise an error if the player inputs improper responses.

"""

# import classes from the corresponding files
from room import Room
from adventure_map import AdventureMap
from inventory import Inventory
from item import Item
from room_not_found_error import RoomNotFoundError

def main():
    print("\nWelcome to the Adkins house! This time you won't be able to leave so easily. Goodluck.")

    # Initialize map w/room storage
    adventure_map = AdventureMap()
    
    # Initialize player inventory 
    inventory = Inventory()
    
    # Initialize Items
    book = Item("Book", "\"A Tale of Two Cities by Charles Dickens\". The greatest novel ever written.") # call an instance of the Item class and assign it to the variable book
    book.set_action("read") # set the book's action to 'read' to be called if the player chooses to read
    # set books content to be outputted to the player after they choose to read the book
    book.set_item_content("You skip to the ending to read Sydney Carton's final speech:\n\tIt is a far, far better thing that I do, than I have ever done; it is a far far better rest that I go to than I have ever known.\nWhat a perfect ending...")
    book_description = "\"A Tale of Two Cities by Charles Dickens\". The greatest novel ever written." # description of book to be printed in inventory action

    fork = Item("Fork", "A conveniently pronged eating utensil. Now I just need something to eat.") # call an instance of the Item class to be assigned with the fork's attributes
    fork_description = "A conveniently pronged eating utensil. Now I just need something to eat." # description of fork to be printed in inventory action

    pizza_cutter = Item("Pizza Cutter", "This must be left over from the tragedy that occurred at Adkin's Pizzeria") # call an instance of the Item class to be assigned with the pizza cutter's attributes
    pizza_cutter_description = "This must be left over from the tragedy that occurred at Adkin's Pizzeria" # description of pizza cutter to be printed in inventory action

    harmonica = Item("Harmonica", "A mouth organ. This might keep me entertained for a couple of hours.") # call an instance of the Item class to be assigned with the harmonica's attributes
    harmonica.set_action("play") # set the harmonica's action to play
    harmonica.set_item_content("You play the sweet sweet melodies of Piano Man on the harmonica. If only someone could hear you...") # set the harmonica's content to be outputted to player if they choose to play the harmonica
    harmonica_description = "A mouth organ. This might keep me entertained for a couple of hours." # description of harmonica to be printed in inventory

    key = Item("Key", "A golden key. This has to unlock something. Right?") # call an instance of Item class to be assigned with attributes of the key
    key.set_action("unlock") # set the key's action to unlock
    key.set_item_content("You unlock the trapdoor under the bed. You crawl through it and into the real world.\nParadiso awaits.\nCongratulations.") # set the key's content to be outputted if player 'unlocks'
    key_description = "A golden key. This has to unlock something. Right?" # description of key to be outputted in inventory

    trophy = Item("Old Trophy", "An old youth bowling league trophy. The words engraved in the plaque are: \"Highest Youth Average: Richard Khouri 186\"") # call an Item instanc to be assigned with trophy's attributes
    trophy_description = "An old youth bowling league trophy. The words engraved in the plaque are: \"Highest Youth Average: Richard Khouri 186\"" # description of trophy to be outputted in inventory action

    picture = Item("Picture", "An old picture found on the night stand.") # call an Item instance to be assigned with picture's attributes
    picture.set_action("inspect") # setter function to set the picture's action to inspect
    # setter function to set the picture's content to be outputted if the player inspects the picture
    picture.set_item_content("You take a closer look at the picture. It's an old picture of Evan Kessler and Richard Khouri back when they studied at Clemson. Good times.") 
    picture_description = "An old picture found on the night stand." # description string to be outputted in player's inventory


    # Call an Room instance to be assigned with each room's attributes, including their name, description, and items
    adventure_map.add_room(Room("Guest Room", "A room filled with numerous torture devices. Who said anything about welcome guests?", ['Kitchen'], [harmonica]))
    adventure_map.add_room(Room("Library", "Better version of the study. It has all of the different books that one may want. Make sure that you stay quiet or the mean librarian will slap you!", ["Holodeck", "Trophy Room", "Study"], [book]))
    adventure_map.add_room(Room("Kitchen", "This amazing culinary art studio has it all: cheese cellar, wine racks, and a 16 stove burner. With its pizza oven, it makes for the perfect Italian getaway.", ["Study", "Guest Room"], [fork, pizza_cutter]))
    adventure_map.add_room(Room("Study", "Do you love being disturbed while working? This room has it all. It is the central hub to the whole house. It has a giant wall of computers and amazing lighting, but doors that exit out into numerous different rooms.", ["Kitchen", "Library", "Bedroom"]))
    adventure_map.add_room(Room("Holodeck", "A room that can disguise itself in a variety of ways. Experience a lush, humid rainforest, a speakeasy of the 1920’s, or the dungeons of Cooper Library.", ["Library"], [key]))
    adventure_map.add_room(Room("Trophy Room", "Spacious room with oak wood as far as the eye can see, shelves filled to the brim with trophies and obscure collections, it really makes you wonder who they belong to.", ["Bedroom", "Library"], [trophy]))
    adventure_map.add_room(Room("Bedroom", "A lavished bed adorns the center of this room, with long curtains, beautiful rugs, and gilded furniture acting as little details to truly make this a great bedroom. You see a trapdoor hidden under the bed.", ["Study", "Trophy Room"], [picture]))
   

    # dictionary of possible actions that the player can respond with
    inputs = {"exit": ["exit", "leave"],
              "lookaround": ["look around", "lookaround", "look"],
              "pickup": ["pick up","pickup", "take", "grab"],
              "play": ['play'],
              "read": ['read'],
              "inventory": ['inventory'],
              "unlock": ['unlock'],
              "inspect": ['inspect']
              }

    # player starts in the study, so the study's attributes are called using the getter function 
    room = adventure_map.get_room('study')
    print(room) # output the attributes of the study

    escaped = False # initialize the player as not having as escaped to use in for loop
    has_key = False # intialize the player as not having the key, so they cannot win the game
    actions = 0 # intialize counter that outputs the amount of actions the user takes to win the game

    while not escaped: # for loop that continues while the player has not escaped the house
        print('Please choose an action:')
        action = input().strip() # get action from player input

        for key, value in inputs.items(): # iterate through the inputs dictionary to ensure the player enters a proper action
            if action.lower() in value:
                action = key 
                actions += 1 # increment actions by 1

        try: # try function which outputs to the player based on the action they inputted and raises an error if room is not found
            if action.lower() == 'exit': # if user wants to exit the room
                print('Where would you like to go?')
                new_room = input().strip()
                if not new_room.title() in room.get_exits(): # if the inputted room to exit to is not found, raise an error and exit the if-else statement
                    raise RoomNotFoundError(f'Invalid room: {new_room} -> Room not found')
                else:
                    room = adventure_map.get_room(new_room) # if the player inputs a supported room, call the getter function to be assigned with the new room
                    print(room) # print attributes of the new room

            elif action.lower() == 'lookaround': # if user chooses to lookaround the room, output the items that are found in the room
                print(room.get_description())
                items = room.get_items() # assign a variable to the items that are found in the room using the getter function
                print('You find some items around you:', end=' ')
                if items: # if the room has items in it (and the player has not already picked up all of the room's items)
                    length = len(items) 
                    for item in items: # iterate through each item in the room
                        item_name = item.get_name() # use the getter function to be able to print the item's name and not just coordinates
                        if length > 1: # if-else statement depending on if the amount of items in the room, printing the proper punctuation
                            print(f'{item_name}', end=', ')
                            length -= 1
                        else:
                            print(f'{item_name}', end='.')
                    print('\n')
                else: # if there are no items in the room, tell the player
                    print('There are no items around here.')
                        
            elif action.lower() == 'pickup': # if the user wants to pickup an item
                items = room.get_items() # assign items variable to the items in the room, if there are no items, it will be assigned to False
                if items: # if there are items in the room (that have not already been picked up), then the player is able to pick it up
                    print('Picked up', end=' ')
                    length = len(items)
                    item_name = items.pop(0).get_name() # item name is assigned to the item at element 0, and then removes it from the list
                    print(f'{item_name}.')
                    if item_name == 'Key': # if the user picks up the key, change has_key to equal True
                        has_key = True
                    inventory.pickup_item(item_name) # pickup item and append it to the player's inventory
            
            elif action.lower() == 'play': # if player wants to play the harmonica (only if they have picked it up)
                items = inventory.get_inventory()
                if 'Harmonica' in items: # if the player has the harmonica, output the harmonica's item content
                    print(harmonica.get_item_content())
                else: # if the player does not have the harmonica in their inventory, print statement to say there is nothing to play
                    print("I don't have anything to play.")

            elif action.lower() == 'read': # if player wants to read the book
                items = inventory.get_inventory()
                if 'Book' in items: # ensure that the player has picked up the book, if so, then print the book's content
                    print(book.get_item_content())
                else: # if the player does not have the book in their inventory
                    print("I don't have anything to read.")

            elif action.lower() == 'inventory': # if player wants to get their inventory items along with their descriptions
                print('INVENTORY:')
                for item in inventory.get_inventory(): # iterate through each item in the player's inventory using a getter method
                    print(f'        {item.title()}-', end=' ') # print item title, followed by a hyphen
                    if item == 'Book': # if the item is a book, print the previously assigned description
                        print(book_description)
                    elif item == 'Fork': # if the item is the fork, print the previously assigned description
                        print(fork_description)
                    elif item == 'Pizza Cutter': # if the item is the pizza cutter, print the previously assigned description
                        print(pizza_cutter_description)
                    elif item == 'Harmonica': # if the item is the harmonica, print the previously assigned description
                        print(harmonica_description)
                    elif item == 'Key': # if the item is the key, print the previously assigned description
                        print(key_description)
                    elif item == 'Old Trophy': # if the item is the old trophy, print the previously assigned description
                        print(trophy_description)
                    elif item == 'Picture': # if the item is the picture, print the previously assigned description
                        print(picture_description)

            elif action.lower() == 'unlock': # if player wants to unlock, using the key
                items = inventory.get_inventory()
                if has_key: # check that the player has the key in their inventory
                    print("You unlock the trapdoor under the bed. You crawl through it and into the real world.\nParadiso awaits.\nCongratulations.")
                    escaped = True # set escaped to be True, so the while loop exits after this loop
                else: # if the player does not have the key, continue the loop
                    continue
                
            elif action.lower() == 'inspect': # if player wants to inspect the trophy or picture
                items = inventory.get_inventory()
                if 'Trophy' in items: # check if player has trophy in their inventory; if so, print the book's content
                    print(trophy.get_item_content())
                elif 'Picture' in items: # check if player has picture in their inventory; if so, print the picture's content
                    print(picture.get_item_content())
                else: # if the player has neither the trophy nor the picture, print that there is nothing to inspect in their inventory
                    print("I don't have anything to inspect.")
            
            else: # if the player enters an unsupported action, print statement and continute through the loop
                print(f'I don\'t know the word "{action}".')

        except RoomNotFoundError as excpt: # except the room not found error if it was raised in the try loop
            print(excpt) # print except statement that was called when the error was raised
 

    f = open('gamelog.txt', 'w') # open gamelog.txt in write mode, which will create a new file if it does not exist
    f.write(f'Congratulations! You finished the game in {actions + 1} steps.') # output the player's actions that it took them to finish the game
    f.close() # close the file

# call the main function to be executed
if __name__ == "__main__":
    main()
