class Item():

    # Constructor
    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        return  f"{self.name} : {self.description} ({self.weight}kg)"
    
    def get_name(self):
        return self.name
    def get_weight(self):
        return self.weight 
