class Player():
    def __init__(self, name):
        self.current_room = None
    
    def move(self, direction):
        next_room = self.current_room.exits[direction]
        
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True