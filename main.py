
from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:
    def __init__(self):
        "Define the constructor"
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None

    def setup(self):
        # Setup commands
        # Setup rooms

        room1 = Room("room1", "dark")
        self.rooms.append(room1)

        # Setup links between rooms
        # Setup starting room
        #self.player.current_room = 
        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help

        self.player = Player("test")
        self.player.current_room = room1
    
    def play(self):
        #Initiate the game
        self.setup()
        self.print_context()
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None
    
    def process_command(self, command_string) -> None:
        list_of_words = command_string.split(" ")
        command_word = list_of_words[0]
    
        #Verify if the command exists
        if command_word not in self.commands.keys():
            print(f"\nCommand '{command_word}' does not exits. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    def print_context(self):
        """Print the welcome message"""
        #Print the current position
        print(self.player.current_room.get_long_description()) 

def main():
    Game().play()
    
if __name__ == "__main__":
    main()
