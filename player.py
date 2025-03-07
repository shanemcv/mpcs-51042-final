# player.py
# holds player information

from fish import Species, Fish
from gear import Gear
from achievements import Achievement
import pickle
import os
import pickle
import sys
import math

def get_asset_path(relative_path):
    '''
    in order to run this game as an executable file, we need to be able to change the relative path to get the path that the 
    executable installer will use
    '''

    if getattr(sys, 'frozen', False): # boilerplate for running as .exe
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path,relative_path)

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

        # initialize experience and level
        self.xp = self.initialize_xp()
        self.level = self.get_level(self.xp)
        self.remaining_xp = self.get_xp_to_next_level(self.xp)

        # initialize gear
        self.gear = self.initialize_gear()

        # initialize achievements
        self.achievements = self.initialize_achievements()

    def initialize_caught_species(self):
        '''initialize the caught species list'''
        self.caught_species = {}

        # Initialize the caught species list (all false). Will be updated when fish are caught. 
        from main import get_species
        species_list = get_species()
        for species in species_list:
            self.caught_species[species.name] = False
        # Reading the pickle file to update caught species list. 
        filepath = get_asset_path(f'./player_data/.{self.username}/.{self.username}.caught_species.pickle')

        # Ensure the subdirectory exists
        os.makedirs(get_asset_path(f'./player_data/.{self.username}'), exist_ok=True)

        # Write file
        if not os.path.exists(filepath):
            with open(filepath, 'wb') as file:
                pickle.dump(self.caught_species,file)
        with open(get_asset_path(f'./player_data/.{self.username}/.{self.username}.caught_species.pickle'), 'rb') as file:
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
        filepath = get_asset_path(f'./player_data/.{self.username}/.{self.username}.caught_fish.pickle')

        # Ensure the subdirectory exists * note, probably redundant because the initialize_caught_species function always runs this first, so can probably delete. 
        os.makedirs(get_asset_path(f'./player_data/.{self.username}'), exist_ok=True)

        # Write file
        if not os.path.exists(filepath):
            with open(filepath, 'wb') as file:
                pickle.dump(self.caught_fish,file)
        with open(get_asset_path(f'./player_data/.{self.username}/.{self.username}.caught_fish.pickle'), 'rb') as file:
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
        filepath = get_asset_path(f'./player_data/.{self.username}/.{self.username}.inventory.pickle')

        # Ensure the subdirectory exists * note, probably redundant because the initialize_caught_species function always runs this first, so can probably delete. 
        os.makedirs(get_asset_path(f'./player_data/.{self.username}'), exist_ok=True)

        # Write file
        if not os.path.exists(filepath):
            with open(filepath, 'wb') as file:
                pickle.dump(self.inventory,file)
        with open(get_asset_path(f'./player_data/.{self.username}/.{self.username}.inventory.pickle'), 'rb') as file:
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
        self.gold = 0

        # Reading the pickle file to update caught species list. 
        filepath = get_asset_path(f'./player_data/.{self.username}/.{self.username}.gold.pickle')

        # Ensure the subdirectory exists * note, probably redundant because the initialize_caught_species function always runs this first, so can probably delete. 
        os.makedirs(get_asset_path(f'./player_data/.{self.username}'), exist_ok=True)

        # Write file
        if not os.path.exists(filepath):
            with open(filepath, 'wb') as file:
                pickle.dump(self.gold,file)
        with open(get_asset_path(f'./player_data/.{self.username}/.{self.username}.gold.pickle'), 'rb') as file:
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
        filepath = get_asset_path(f'./player_data/.{self.username}/.{self.username}.locations.pickle')

        # Ensure the subdirectory exists * note, probably redundant because the initialize_caught_species function always runs this first, so can probably delete. 
        os.makedirs(get_asset_path(f'./player_data/.{self.username}'), exist_ok=True)

        # Write file
        if not os.path.exists(filepath):
            with open(filepath, 'wb') as file:
                pickle.dump(self.unlocked_locations,file)
        with open(get_asset_path(f'./player_data/.{self.username}/.{self.username}.locations.pickle'), 'rb') as file:
            try:
                pickle_data = pickle.load(file)
            except:
                return
            else:
                for location in pickle_data:
                    self.unlocked_locations.add(location)

        return self.unlocked_locations
    
    def initialize_xp(self):
        '''initialize the player's experience, loading from a previous save if applicable'''
        self.xp = 0

        # Reading the pickle file to update caught species list. 
        filepath = get_asset_path(f'./player_data/.{self.username}/.{self.username}.xp.pickle')

        # Ensure the subdirectory exists * note, probably redundant because the initialize_caught_species function always runs this first, so can probably delete. 
        os.makedirs(get_asset_path(f'./player_data/.{self.username}'), exist_ok=True)

        # Write file
        if not os.path.exists(filepath):
            with open(filepath, 'wb') as file:
                pickle.dump(self.xp,file)
        with open(get_asset_path(f'./player_data/.{self.username}/.{self.username}.xp.pickle'), 'rb') as file:
            try:
                pickle_data = pickle.load(file)
            except:
                return
            else:
                self.xp = pickle_data

        return self.xp
    
    def get_level(self, xp):
        '''initializes player level based on experience'''

        # exponential leveling formula
        level = 1 + (math.log((xp + 999) / 1337) / math.log(1.1))
        level = max(1, int(level))
        if level > 99:
            level = 99
        return level
    
    def get_xp_to_next_level(self, xp):
        '''initializes player level based on experience'''

        current_level = self.get_level(xp)
        xp_for_next = 1337 * (1.1 ** current_level) - 999
        if xp_for_next % 1 == 0:
            xp_for_next = int(xp_for_next + 1)
        else:
            xp_for_next = int(xp_for_next)
        
        remaining_xp = xp_for_next - xp
        return remaining_xp
    
    def initialize_gear(self):
        '''initialize the player's gear, loading from a previous save if applicable'''
        self.gear = [Gear("Basic Fishing Rod", 10, True, True)]
        
        # Reading the pickle file to update gear list. 
        filepath = get_asset_path(f'./player_data/.{self.username}/.{self.username}.gear.pickle')

        # Ensure the subdirectory exists * note, probably redundant because the initialize_caught_species function always runs this first, so can probably delete. 
        os.makedirs(get_asset_path(f'./player_data/.{self.username}'), exist_ok=True)

        # Write file
        if not os.path.exists(filepath):
            with open(filepath, 'wb') as file:
                pickle.dump(self.gear,file)
        with open(get_asset_path(f'./player_data/.{self.username}/.{self.username}.gear.pickle'), 'rb') as file:
            try:
                pickle_data = pickle.load(file)
            except:
                return
            else:
                self.gear = pickle_data

        self.gear = list(set(self.gear)) # remove duplicate items

        return self.gear
    
    def initialize_achievements(self):
        '''initialize the player's achievements, loading from a previous save if applicable'''
        self.achievements = [
            Achievement("Fisherman!", "Catch any fish", False),
            Achievement("Diamond in the Rough", "Catch any diamond-rarity fish", False),
            Achievement("Traveller", "Unlock any new Location", False),
            Achievement("Perfect Catch", "Catch a Perfect Grade (6-Star) fish", False),
            Achievement("Moneybags", "Have a gold stack exceeding 10,000 coins", False) 
        ]
        
        # Reading the pickle file to update achievements list. 
        filepath = get_asset_path(f'./player_data/.{self.username}/.{self.username}.achievements.pickle')

        # Ensure the subdirectory exists * note, probably redundant because the initialize_caught_species function always runs this first, so can probably delete. 
        os.makedirs(get_asset_path(f'./player_data/.{self.username}'), exist_ok=True)

        # Write file
        if not os.path.exists(filepath):
            with open(filepath, 'wb') as file:
                pickle.dump(self.achievements,file)
        with open(get_asset_path(f'./player_data/.{self.username}/.{self.username}.achievements.pickle'), 'rb') as file:
            try:
                pickle_data = pickle.load(file)
            except:
                return
            else:
                self.achievements = pickle_data

        return self.achievements

    def pickle_dump_data(self):
        '''pickles all player information into files'''
        with open(get_asset_path(f'./player_data/.{self.username}/.{self.username}.caught_species.pickle'), 'wb') as file:
            pickle.dump(self.caught_species,file)
        with open(get_asset_path(f'./player_data/.{self.username}/.{self.username}.caught_fish.pickle'), 'wb') as file:
            pickle.dump(self.caught_fish,file)
        with open(get_asset_path(f'./player_data/.{self.username}/.{self.username}.inventory.pickle'), 'wb') as file:
            pickle.dump(self.inventory,file)
        with open(get_asset_path(f'./player_data/.{self.username}/.{self.username}.gold.pickle'), 'wb') as file:
            pickle.dump(self.gold,file)
        with open(get_asset_path(f'./player_data/.{self.username}/.{self.username}.locations.pickle'), 'wb') as file:
            pickle.dump(self.unlocked_locations,file)
        with open(get_asset_path(f'./player_data/.{self.username}/.{self.username}.xp.pickle'), 'wb') as file:
            pickle.dump(self.xp,file)
        with open(get_asset_path(f'./player_data/.{self.username}/.{self.username}.gear.pickle'), 'wb') as file:
            pickle.dump(self.gear,file)
        with open(get_asset_path(f'./player_data/.{self.username}/.{self.username}.achievements.pickle'), 'wb') as file:
            pickle.dump(self.achievements,file)
        


