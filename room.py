class Room:
    def __init__(self, name='', description='', exits=[], items=[]): #constructor to initialize the rooms attributes: name, description, exits, and items
        self.name = name
        self.description = description
        self.exits = exits
        self.items = items
    
    def get_name(self): # get_name method to return the name of the room
        return self.name
    
    def get_description(self): # get_description method to return the description of the room
        return self.description

    def get_exits(self): # get_exits method to return the list of exits that correlate with the room
        return self.exits
    
    def get_items(self): # getter method to return items in the corresponding room
        return self.items

    def list_exits(self): # function that iterates throught the exits lists and prints them each on a newline
        # initialize an empty string to add to that will contain each exit separated by a newline
        exit_str = ''
        for i in range(len(self.exits)): # for loop to iterate through the exit list
            exit_str += f'\n{str(self.exits[i])}' # increment the string by the current iterated element of the list on a newline
        return exit_str # return the final string to use in the __str__ method
    
    def __str__(self): # method that prints the room name, followed by its description and the list of exits from the room
        return f"{self.get_name()}: {self.get_description()}\n\nExits:{self.list_exits()}"