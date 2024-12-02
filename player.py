# Define the Player class.
class Player():
    """
    This class represents a player. A player is composed of a name and a current room.

    Attributes:
        name (str): The name of the player.
        current_room (str): The room where the player is.

    Methods:
        __init__(self, name) : The constructor.
        move(self, direction) : This function changes the current room of the player

    Examples:

    >>> from player import Player
    >>> self.player = Player(input("Bob"))
    >>> self.player.name
    'Bob'
    >>> self.player.current_room
    'None'
    """
    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.

        if direction.lower() not in {"n", "nord", "north", "s", "sud", "south", "e", "est", "east", "o", "ouest", "west", "u", "up", "d", "down"}:
            return False
        elif direction.lower() in {"n", "nord", "north"}:
            if self.current_room.get_exits()["N"]  != None :
                next_room = self.current_room.exits["N"]
            else :
                print("TYou can't go in that direction.")
                return False
        elif direction.lower() in {"s", "sud", "south"}:
            if self.current_room.get_exits()["S"]  != None :
                next_room = self.current_room.exits["S"]
            else :
                print("You can't go in that direction.")
                return False
        elif direction.lower() in {"e", "est", "east"}:
            if self.current_room.get_exits()["E"]  != None :
                next_room = self.current_room.exits["E"]
            else :
                print("You can't go in that direction.")
                return False
        elif direction.lower() in {"o", "ouest", "west"}:
            if self.current_room.get_exits()["O"]  != None :
                next_room = self.current_room.exits["O"]
            else :
                print("You can't go in that direction.")
                return False
        elif direction.lower() in {"u", "up"}:
            if self.current_room.get_exits()["U"]  != None :
                next_room = self.current_room.exits["U"]
            else :
                print("You can't go in that direction.")
                return False
        elif direction.lower() in {"d", "down"}:
            if self.current_room.get_exits()["D"]  != None :
                next_room = self.current_room.exits["D"]
            else :
                print("Tou can't go in that direction.")
                return False
        else :
            print("YThis direction doesn't exist.")
            return False

        # If the next room is None, print an error message and return False.
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    