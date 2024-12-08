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
        self.history = []

    def get_history(self):
        print("You've already been in these rooms :\n")
        for room in self.history:
            print(f"- {room.get_description_history()}")
        return ""
    
    def get_history2(self):
        return self.history
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        if direction.lower() not in {"n", "nord", "north", "s", "sud", "south", "e", "est", "east", "o", "ouest", "west", "u", "up", "d", "down"}:
            print("This direction doesn't exist.")
            return False
        elif direction.lower() in {"n", "nord", "north"}:
            if self.current_room.get_exits()["N"]  != None :
                next_room = self.current_room.exits["N"]
            else :
                print("You can't go in that direction.")
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
                print("You can't go in that direction.")
                return False
        else :
            print("This direction doesn't exist.")
            return False

    
        
        # Set the current room to the next room and save this room on the history.
        
        self.current_room = next_room
        if self.current_room.get_description_history() not in self.history :
            self.history.append(self.current_room)
        print(self.current_room.get_long_description())
        print(self.get_history())
        return True
    
    