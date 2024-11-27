# Define the Room class.

class Room:
    """
    This class represents a room. A room is composed of a name, a description, and a dictionary which represents all of the connected rooms.

    Attributes:
        name (str): The name of the room.
        description (str): The description of the room.
        exits (dict): All of the connected rooms.

    Methods:
        __init__(self, command_word, help_string, action, number_of_parameters) : The constructor.
        __str__(self) : The string representation of the command.

    Examples:

    >>> from actions import go
    >>> command = Command("go", "Permet de se déplacer dans une direction.", go, 1)
    >>> command.command_word
    'go'
    >>> command.help_string
    'Permet de se déplacer dans une direction.'
    >>> type(command.action)
    <class 'function'>
    >>> command.number_of_parameters
    1

    """


    # Define the constructor. 
    def __init__(self, name, description):
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
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
