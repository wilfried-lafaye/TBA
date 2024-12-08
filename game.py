# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

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

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        
        # Setup rooms

        Bedroom = Room("Bedroom", "your bedroom.")
        self.rooms.append(Bedroom)
        room1 = Room("room1", "")
        self.rooms.append(room1)
        room2 = Room("room2", "")
        self.rooms.append(room2)
        office = Room("room3", "")
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

        Bedroom.exits = {"N" : room1, "E" : Hall, "S" : None, "O" : None, "U" : None, "D" : None}
        room1.exits = {"N" : None, "E" : room2, "S" : Bedroom, "O" : None, "U" : None, "D" : None}
        room2.exits = {"N" : None, "E" : office, "S" : None, "O" : room1, "U" : None, "D" : None}
        office.exits = {"N" : None, "E" : None, "S" : None, "O" : room2, "U" : None, "D" : None}
        Hall.exits = {"N" : None, "E" : ElevatorUP, "S" : None, "O" : Bedroom, "U" : None, "D" : None}
        ElevatorUP.exits = {"N" : None, "E" : None, "S" : None, "O" : Hall, "U" : None, "D" : ElevatorDOWN}
        ElevatorDOWN.exits = {"N" : None, "E" : None, "S" : None, "O" : Hall2, "U" : ElevatorUP, "D" : None}
        Hall2.exits = {"N" : None, "E" : ElevatorDOWN, "S" : Closet, "O" : None, "U" : None, "D" : None}
        Closet.exits = {"N" : Hall2, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}

        # Setup player and starting room

        self.player = Player("Bob")
        self.player.current_room = Bedroom

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
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
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
