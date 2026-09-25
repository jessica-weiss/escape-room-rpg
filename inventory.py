
class Inventory(): # create inventory class to hold player's items that they have picked up
    def __init__(self, item_inventory=[]): # initialize item inventory list
        self.item_inventory = item_inventory
    
    def pickup_item(self, item): # when player picksup item, append the item to their inventory
        self.item_inventory.append(item)

    def get_inventory(self): # get method to return the contents in the player's inventory
        return self.item_inventory
    
