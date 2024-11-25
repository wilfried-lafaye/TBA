class Player():
    def __init__(self, name):
        self.current_room = None
    
    def move(self, room):
        """
        Move the player in the room specified by the parameter.
        The parameter must be the name of a room.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        """
      
            #print("\nYou're already in this room\n")
            #return False

        print(self.current_room.get_name_room())

        if str(room) not in  {"room1","room2", "room3"}:
            print("\nThis room does not exits\n")
            return False
        next_room = self.current_room.exits[room]
        
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True