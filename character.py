import random
class Character():

    # Constructor
    def __init__(self, name, description, current_room, msgs):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs

    def __str__(self):
        return  f"{self.name} : {self.description}"
    
    def move(self, rooms):
        if random.choice([0,1])  :
            self.current_room = random.choice(rooms)
            return True

        return False
    
    def get_msg(self):
        msg = self.msgs.pop(0)
        self.msgs.append(msg)
        return msg
    
