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
        self.characters =[]
    
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
        local = Room("local", "the local.")
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
        Exit = Room("Exit", "the exit.")
        self.rooms.append(Exit)
    

        # Create exits for rooms

        Bedroom.exits = {"N" : local, "E" : Hall, "S" : None, "W" : None, "U" : None, "D" : None}
        local.exits = {"N" : None, "E" : PatientRoom, "S" : Bedroom, "W" : None, "U" : None, "D" : None}
        PatientRoom.exits = {"N" : None, "E" : office, "S" : None, "W" : local, "U" : None, "D" : None}
        office.exits = {"N" : None, "E" : None, "S" : None, "W" : PatientRoom, "U" : None, "D" : None}
        Hall.exits = {"N" : None, "E" : ElevatorUP, "S" : None, "W" : Bedroom, "U" : None, "D" : None}
        ElevatorUP.exits = {"N" : None, "E" : None, "S" : None, "W" : Hall, "U" : None, "D" : ElevatorDOWN}
        ElevatorDOWN.exits = {"N" : None, "E" : None, "S" : None, "W" : Hall2, "U" : ElevatorUP, "D" : None}
        Hall2.exits = {"N" : None, "E" : ElevatorDOWN, "S" : Closet, "W" : Exit, "U" : None, "D" : None}
        Closet.exits = {"N" : Hall2, "E" : None, "S" : None, "W" : None, "U" : None, "D" : None}
        Exit.exits = {"N" : None, "E" : None, "S" : None, "W" : None, "U" : None, "D" : None}

        # Setup player and starting room

        self.player = Player("Bob")
        self.player.current_room = Bedroom

        self.player.current_room.inventory.add(Item("sword", "une épée au fil tranchant comme un rasoir", 2))

        # Setup items
        local.inventory.add(Item("coat","a coat that allow you to hide from the scientist",2))
        office.inventory.add(Item("card","this card allows you to use the elevator",1))
        office.inventory.add(Item("number", "Daisy's phone number",1))
        PatientRoom.inventory.add(Item("key", "a mysterious key",2))
    

        # Setup PNJs
        
        Michael = Character("Micheal", "a cleaning agent, you can corrupt him by giving him Daisy's number.", Hall2, ["go away let me do my work","oh wait I recognize you",
                                                                                                                      "I will let you escape if you give me Daisy's number"] )
        Hall2.characters.update({"micheal" : Michael})
        self.characters.append(Michael)
        
        Scientist = Character("Scientist", "an old man with white hair and an arched back ", office, ["a","f","u"] )
        office.characters.update({"scientist" : Scientist })
        self.characters.append(Scientist)

        Daisy = Character("Daisy","a 35-year-old laboratory nurse, is a methodical and passionate woman.", Bedroom, ["a","fg","f"])
        Bedroom.characters.update({"daisy" : Daisy})
        self.characters.append(Daisy)

    

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
        print("\nYour story takes place in a gloomy, empty hospital hospital. You wake up in a hospital room with no memory of how they got there and what they did to you. You're just thinking one thing, ESCAPE!\n")
        
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
