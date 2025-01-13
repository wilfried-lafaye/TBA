# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : show this help.", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : exit the game.", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : move in a cardinal direction (N, E, S, W).", Actions.go, 1)
        self.commands["go"] = go
        history = Command("history", " : shows visited rooms.", Actions.history, 0)
        self.commands["history"] = history
        back = Command("back", " : go back in the last room.", Actions.back, 0)
        self.commands["back"] = back

        check = Command("check", " : show the items in your inventory.", Actions.check, 0)
        self.commands["check"] = check

     
        look = Command("look", " : show the items in the room.", Actions.look, 0)
        self.commands["look"] = look

        take = Command("take", " : take the chosen item.", Actions.take, 1)
        self.commands["take"] = take

        drop = Command("drop", " : drop the chosen item from your inventory.", Actions.drop, 1)
        self.commands["drop"] = drop

        talk = Command("talk", " : talk to a PNJ in the current room.", Actions.talk,1)
        self.commands["talk"] = talk

        
        # Setup rooms

        Bedroom = Room("Bedroom", "your bedroom.")
        self.rooms.append(Bedroom)
        local = Room("loca1", "the local.")
        self.rooms.append(local)
        PatientRoom = Room("PatientRoom", "another patient room")
        self.rooms.append(PatientRoom)
        office = Room("office", "")
        self.rooms.append(office)
        Hall = Room("Hall", "the upstairs hallway.")
        self.rooms.append(Hall)
        ElevatorUP = Room("ElevatorUP", "the elevator on the first floor.")
        self.rooms.append(ElevatorUP)
        ElevatorDOWN = Room("ElevatorDOWN", "the elevator on the ground floor.")
        self.rooms.append(ElevatorDOWN)
        Hall2 = Room("Hall2", "the groundfloor hallway.")
        self.rooms.append(Hall2)
        Closet = Room("Closet", "a closet.")
        self.rooms.append(Closet)
    

        # Create exits for rooms

        Bedroom.exits = {"N" : local, "E" : Hall, "S" : None, "O" : None, "U" : None, "D" : None}
        local.exits = {"N" : None, "E" : PatientRoom, "S" : Bedroom, "O" : None, "U" : None, "D" : None}
        PatientRoom.exits = {"N" : None, "E" : office, "S" : None, "O" : local, "U" : None, "D" : None}
        office.exits = {"N" : None, "E" : None, "S" : None, "O" : PatientRoom, "U" : None, "D" : None}
        Hall.exits = {"N" : None, "E" : ElevatorUP, "S" : None, "O" : Bedroom, "U" : None, "D" : None}
        ElevatorUP.exits = {"N" : None, "E" : None, "S" : None, "O" : Hall, "U" : None, "D" : ElevatorDOWN}
        ElevatorDOWN.exits = {"N" : None, "E" : None, "S" : None, "O" : Hall2, "U" : ElevatorUP, "D" : None}
        Hall2.exits = {"N" : None, "E" : ElevatorDOWN, "S" : Closet, "O" : None, "U" : None, "D" : None}
        Closet.exits = {"N" : Hall2, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}

        # Setup player and starting room

        self.player = Player("Bob")
        self.player.current_room = Bedroom
        self.player.current_room.inventory.add(Item("sword", "une épée au fil tranchant comme un rasoir", 2))

        # Setup items
        local.inventory.add(Item("casque","casque de protection contre les monstres",2))
        Hall.inventory.add(Item("bouclier","un bouclier",2))

        # Setup PNJs
        
        local.characters.update({"bob" : Character("Bob", "un bob", local, ["a","b","c"] )})

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]
        if command_word in "          ": 
            return False

        # If the command is not recognized, print an error message
        if command_word.lower() not in self.commands.keys():
            print(f"\nCommand '{command_word}' does not exits. Write 'help' to see all the commands\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word.lower()]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(self.player.current_room.get_long_description())
        
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
