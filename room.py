class Room:
    """
    This class defines the features of a room.

    Attributes:
        name (str): The name of the room.
        description (str): The description of the room.
        exits (): 

    Methods:
        __init__(self, name, description) : The constructor.
        __get_exit__(self, direction) : .
        __get_exit_string__(self): .
        __get_long_description__(self):
    """
    def __init__(self, name, description):
        "Define the constructor"
        self.name = name
        self.description = description
        self.exits = {}

    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
        # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string
    
    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nYou're actually in {self.description}"#\n\n{self.get_exit_string()}\n"

    def get_name_room(self):
        return {self.name}
