# player.py
# holds player information

from fish import Species, Fish
import pickle
import os

class Player:
    '''a player of the game'''
    def __init__(self,username):
        '''initialize function. 
        
        Arguments: 
        username (str): the username of the player.
        '''
        self.username = username
        self.caught_species = self.initialize_caught_species()
        self.caught_fish = self.initialize_caught_fish()

        # Initialize inventory. Maxes at size 16. 
        self.inventory = self.initialize_inventory()

        #initialize currency
        self.gold = self.initialize_gold()

        # initialize unlocked locations
        self.unlocked_locations = self.initialize_locations()

    def initialize_caught_species(self):
        '''initialize the caught species list'''
        self.caught_species = {}

        # Initialize the caught species list (all false). Will be updated when fish are caught. 
        from main import get_species
        species_list = get_species()
        for species in species_list:
            self.caught_species[species.name] = False
        # Reading the pickle file to update caught species list. 
        filepath = f'./player_data/.{self.username}/.{self.username}.caught_species.pickle'

        # Ensure the subdirectory exists
        os.makedirs(f'./player_data/.{self.username}', exist_ok=True)

        # Write file
        if not os.path.exists(filepath):
            with open(filepath, 'wb') as file:
                pickle.dump(self.caught_species,file)
        with open(f'./player_data/.{self.username}/.{self.username}.caught_species.pickle', 'rb') as file:
            try:
                pickle_data = pickle.load(file)
            except:
                return
            else:
                self.caught_species.update(pickle_data)

        return self.caught_species
    
    def initialize_caught_fish(self):
        '''initialize the caught fish list'''
        self.caught_fish = []

        # Reading the pickle file to update caught species list. 
        filepath = f'./player_data/.{self.username}/.{self.username}.caught_fish.pickle'

        # Ensure the subdirectory exists * note, probably redundant because the initialize_caught_species function always runs this first, so can probably delete. 
        os.makedirs(f'./player_data/.{self.username}', exist_ok=True)

        # Write file
        if not os.path.exists(filepath):
            with open(filepath, 'wb') as file:
                pickle.dump(self.caught_fish,file)
        with open(f'./player_data/.{self.username}/.{self.username}.caught_fish.pickle', 'rb') as file:
            try:
                pickle_data = pickle.load(file)
            except:
                return
            else:
                for fish in pickle_data:
                    self.caught_fish.append(fish)

        return self.caught_fish
    
    def initialize_inventory(self):
        '''initialize the inventory list'''
        self.inventory = []

        # Reading the pickle file to update caught species list. 
        filepath = f'./player_data/.{self.username}/.{self.username}.inventory.pickle'

        # Ensure the subdirectory exists * note, probably redundant because the initialize_caught_species function always runs this first, so can probably delete. 
        os.makedirs(f'./player_data/.{self.username}', exist_ok=True)

        # Write file
        if not os.path.exists(filepath):
            with open(filepath, 'wb') as file:
                pickle.dump(self.inventory,file)
        with open(f'./player_data/.{self.username}/.{self.username}.inventory.pickle', 'rb') as file:
            try:
                pickle_data = pickle.load(file)
            except:
                return
            else:
                for fish in pickle_data:
                    self.inventory.append(fish)

        return self.inventory
    
    def initialize_gold(self):
        '''initialize the player's gold, loading from a previous save if applicable'''
        self.gold = 1000000

        # Reading the pickle file to update caught species list. 
        filepath = f'./player_data/.{self.username}/.{self.username}.gold.pickle'

        # Ensure the subdirectory exists * note, probably redundant because the initialize_caught_species function always runs this first, so can probably delete. 
        os.makedirs(f'./player_data/.{self.username}', exist_ok=True)

        # Write file
        if not os.path.exists(filepath):
            with open(filepath, 'wb') as file:
                pickle.dump(self.gold,file)
        with open(f'./player_data/.{self.username}/.{self.username}.gold.pickle', 'rb') as file:
            try:
                pickle_data = pickle.load(file)
            except:
                return
            else:
                self.gold = pickle_data

        return self.gold
    
    def initialize_locations(self):
        '''initialize the player's unlocked locations, loading from a previous save if applicable'''
        self.unlocked_locations = {"Local Pond"}
        
        # Reading the pickle file to update locations list. 
        filepath = f'./player_data/.{self.username}/.{self.username}.locations.pickle'

        # Ensure the subdirectory exists * note, probably redundant because the initialize_caught_species function always runs this first, so can probably delete. 
        os.makedirs(f'./player_data/.{self.username}', exist_ok=True)

        # Write file
        if not os.path.exists(filepath):
            with open(filepath, 'wb') as file:
                pickle.dump(self.unlocked_locations,file)
        with open(f'./player_data/.{self.username}/.{self.username}.locations.pickle', 'rb') as file:
            try:
                pickle_data = pickle.load(file)
            except:
                return
            else:
                for location in pickle_data:
                    self.unlocked_locations.add(location)

        return self.unlocked_locations

    def pickle_dump_data(self):
        '''pickles all player information into files'''
        with open(f'./player_data/.{self.username}/.{self.username}.caught_species.pickle', 'wb') as file:
            pickle.dump(self.caught_species,file)
        with open(f'./player_data/.{self.username}/.{self.username}.caught_fish.pickle', 'wb') as file:
            pickle.dump(self.caught_fish,file)
        with open(f'./player_data/.{self.username}/.{self.username}.inventory.pickle', 'wb') as file:
            pickle.dump(self.inventory,file)
        with open(f'./player_data/.{self.username}/.{self.username}.gold.pickle', 'wb') as file:
            pickle.dump(self.gold,file)
        with open(f'./player_data/.{self.username}/.{self.username}.locations.pickle', 'wb') as file:
            pickle.dump(self.unlocked_locations,file)


