# gear.py
# holds gear information

class Gear:
    '''a piece of Gear the user can use'''

    def __init__(self, name, price, owned=False, equipped=False):
        '''initializes an instance of a piece of Gear'''

        self.name = name
        self.price = price
        self.owned = owned
        self.equipped = equipped

        
