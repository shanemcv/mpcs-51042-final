# locations.py
# holds location information

class Location:
    '''a location that the user can go fishing in'''

    def __init__(self, name, unlock_price, unlocked=False):
        '''initializes an instance of a location'''

        self.name = name
        self.unlock_price = unlock_price
        self.unlocked = unlocked
