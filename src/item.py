class Item():
    '''
    This is an item class with attributes:
    name
    '''
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Items in this room: {self.name} "

    def __repr__(self):
        return f"{self.name}, {self.description}"  