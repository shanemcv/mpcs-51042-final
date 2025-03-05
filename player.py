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


    def pickle_dump_data(self):
        '''pickles all player information into files'''
        with open(f'./player_data/.{self.username}/.{self.username}.caught_species.pickle', 'wb') as file:
            pickle.dump(self.caught_species,file)
        with open(f'./player_data/.{self.username}/.{self.username}.caught_fish.pickle', 'wb') as file:
            pickle.dump(self.caught_fish,file)
        with open(f'./player_data/.{self.username}/.{self.username}.inventory.pickle', 'wb') as file:
            pickle.dump(self.inventory,file)


