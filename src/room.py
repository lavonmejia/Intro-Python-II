from item import Item  

# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    '''
    This is a room class with attributes:
    name, description
    '''
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    # def __str__(self):
        # return f"In this room {self.name}, {self.description}, {self.items}"   

    # def __repr__(self):
    #     return f"In this room {self.name}, {self.description}, {self.items}"   

    def add_item(self, room):
        self.items.append(room)

    
        


    
        



        
    
        
