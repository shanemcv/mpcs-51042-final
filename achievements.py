# achievements.py
# holds information for the achievement and achievements classes

class Achievement:
    '''holds information about a given achievement'''

    def __init__(self, name, description, achieved=False):
        '''initializes an achievement'''

        self.name = name
        self.description = description
        self.achieved = achieved