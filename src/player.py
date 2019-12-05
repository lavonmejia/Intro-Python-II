# Write a class to hold player information, e.g. what room they are in
# currently.

from abc import ABC, abstractmethod

class Player(ABC):
    '''
    This is a player class with attributes:
    location, species, job
    '''
    def __init__(self, location,species, job, specs):
        self._location = location
        self._species = species
        self._job = job
        self._specs = specs

        # #Specs
    def __repr__(self):
        return f"{self._specs}: {self._species}, {self._job} currently in {self.location} "
    def __str__(self):
        return f"{self._specs}"
    def get_player(self):
        '''
        Returns the players specs
        '''
        return self._specs

        # #Location --TO BE ADDED
    def __repr__(self):
        return f"{self._specs}: {self._species}, {self._job} currently in {self.location} "
    def __str__(self):
        return f"{self._specs}"
    def get_player(self):
        '''
        Returns the players specs
        '''
        return self._specs


    @abstractmethod
    def speak(self):
        print("This is awesome! So happy to be here")