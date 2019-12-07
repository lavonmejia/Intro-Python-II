from item import Item  

# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    '''
    This is a player class with attributes:
    room, species, job
    '''
    def __init__(self, room, species, job):
        self.room = room
        self.species = species
        self.job = job
        self.inventory = []


    def add_to_inventory(self, player):
        self.inventory.append(player)


    #     self.specs = specs

    #     # #Specs
    # def __repr__(self):
    #     return f"{self.specs}: {self.species}, {self.job} "
    # def __str__(self):
    #     return f"{self.specs}"
    # def get_player(self):
    #     '''
    #     Returns the players specs
    #     '''
    #     return self.specs
   
    def speak(self):
        print("This is awesome! So happy to be here") 
