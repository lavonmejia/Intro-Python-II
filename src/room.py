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

    def add_item(self, item):
        self.items.append(item)

    def list_items(self):
        i = 1
        pretty_list = ''
        for item in self.items:
            pretty_list += f"{i}) {item.name} - {item.description}\n"
            i += 1
        return pretty_list

    def item_here(self, item_name):
        for item in self.items:
            if item_name == item.name:
                return True
        return False
        


    
        



        
    
        
