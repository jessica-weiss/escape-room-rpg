class Item: # create item class to hold the contents and attributed of each item in the rooms
    def __init__(self, name='', description=''): # initialize name and description strings to call the item with
        self.name = name
        self.decription = description
        # item content and action are initialized as None and will only be assigned to a string once the setter function is called in main.py
        self.item_content = None 
        self.action = None
    
    def set_action(self, action): # set action method to be called when an item has a corresponding action with it
        self.action = action
    
    def set_item_content(self, item_content): # set item content method to be called when an item has content to be read or played
        self.item_content = item_content

    def get_action(self): # getter method to return an item's action
        return self.action

    def get_name(self): # getter function to return an item's name
        return self.name
    
    def get_description(self): # getter function to return item's description
        return self.description
    
    def get_item_content(self): # getter function to return item's content
        return self.item_content

    
