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
        self.inventory = {}
        self.max_weight = 4

    
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        if direction.lower() in {"n", "north", "s", "south", "e", "east","w" , "west", "u", "up", "d", "down"} :

            if self.current_room.exits[direction[0].upper()]  != None :
                if self.current_room.exits[direction[0].upper()].name == "ElevatorDOWN" and "card" not in self.inventory :
                    print("You can't use the elevator without the card !!!")
                    game.finished = True
                    return True
                
                if self.current_room.exits[direction[0].upper()].name == "Exit" and "number" not in self.inventory :
                    print("Micheal didn't let you escape !!!")
                    game.finished = True
                    return True
                
                if self.current_room.exits[direction[0].upper()].name == "Exit" and "number" in self.inventory :
                    print("You have escape the laboratory ! Congratulations !")
                    game.finished = True
                    return True
                
                

                next_room = self.current_room.exits[direction[0].upper()]
                self.history.append(self.current_room)
                self.current_room = next_room
                print(self.current_room.get_long_description())
                print(self.get_history())
                return True
            else :
                print("You can't go in that direction.")
                return False
        # Set the current room to the next room and save this room on the history.
        print("This direction doesn't exist.") 
        return False

    def get_history(self):
        print("You've already been in these rooms :\n")
        for room in self.history:
            print(f"- {room.description}")
        return ""

    def get_inventory(self):
        if not self.inventory : 
            return "\nYou're inventory is empty.\n"
        else :
            print("These are your items :")
            for items in self.inventory.values() :
                print(f"- {items}")

    