from room import Room
from room_not_found_error import RoomNotFoundError



class AdventureMap(Room): # child class to Room

    def __init__(self): # constructor that initializes the empty adventure map dictionary
        self.adventure_map = {}

    def add_room(self, room): # method which adds the room to the adventure map dictionary
        self.adventure_map[room.get_name().lower()] = room
    
    def get_room(self, room_name): # method which returns the value of the room_name key from the adventure map dictionary
        return self.adventure_map[room_name.lower()]
