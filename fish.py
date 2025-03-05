# fish.py
# holds class information for fishies

import random
import datetime
import math

class Species:
    def __init__(self,name,description,rarity,rarity_weight,base_length,length_std_dev,weight_factor,weight_std_dev):
        '''
        Represents a fish species.
        Arguments: 
            name (str): The name of the species
            rarity (str): The rarity category of the species ex. bronze, silver, gold, platinum, diamond
            rarity_weight (float): The rarity number of this species, which impacts likelihood of catch. 
            base_length (float): Average length of the species.
            length_std_dev (float): Standard deviation for length variation. 
            weight_factor (float): Factor that converts the length to weight based on a normal distribution. 
            weight_std_dev (float): Standard deviation for weight variation. 
        '''
        self.name = name
        self.rarity = rarity
        self.description = description
        self.rarity_weight = rarity_weight
        self.base_length = base_length
        self.length_std_dev = length_std_dev
        self.weight_factor = weight_factor
        self.weight_std_dev = weight_std_dev

    def generate_length(self):
        '''Generates a random length of an instance of this species'''
        return round(random.gauss(self.base_length, self.length_std_dev), 2)
    
    def generate_weight(self,length):
        '''Generates a random weight of an instance of this species, based on the length'''
        mean_weight = length * self.weight_factor
        return round(random.gauss(mean_weight, self.weight_std_dev), 2)

class Fish:
    '''an instance of a caught fish''' 
    def __init__(self,species):
        '''Initializes a fish. 
        Arguments: 
            species (Species): The species of this fish. 
        '''
        self.species = species
        self.description = self.species.description
        self.length = species.generate_length()
        self.weight = species.generate_weight(self.length)
        self.time_caught = datetime.datetime.now()
        self.length_grade = self.determine_length_grade()
        self.weight_grade = self.determine_weight_grade()
        self.colouration = self.determine_colouration()
        self.condition = self.determine_condition()
        self.grade = self.determine_overall_grade()

    def __str__(self):
        '''String representation of the caught fish'''
        return (f"{self.grade} {self.species.name} of {self.colouration} Colouration and {self.condition} Condition ({self.length} in, {self.weight} lbs) on {self.time_caught.strftime('%Y-%m-%d %H:%M:%S')}")

    def determine_length_grade(self):
        '''determines a length grade for a caught fish'''
        z_scores = {
        "Diamond": 2.33,
        "Platinum": 1.28,
        "Gold": 0.67,
        "Silver": 0,
        "Bronze": -2.33,
        "Copper": -float("inf"),
        }

        grades = ["Copper", "Bronze", "Silver", "Gold", "Platinum", "Diamond"]
        for grade in reversed(grades):
            z_score = z_scores[grade]
            cutoff = self.species.base_length + (z_score * self.species.length_std_dev)
            if self.length >= cutoff:
                return grade
            
        return "Copper" # as default
    
    def determine_weight_grade(self):
        '''determines a weight grade for a caught fish'''

        z_scores = {
        "Diamond": 2.33,
        "Platinum": 1.28,
        "Gold": 0.67,
        "Silver": 0,
        "Bronze": -2.33,
        "Copper": -float("inf"),
        }

        # Mean weight calculation for a fish of this species
        mean_weight = self.species.base_length * self.species.weight_factor

        # Calculate the standard deviation for weight considering both length distribution and weight
        sigma_weight = math.sqrt(self.species.weight_std_dev**2 + (self.species.weight_factor * self.species.length_std_dev)**2)

        grades = ["Copper", "Bronze", "Silver", "Gold", "Platinum", "Diamond"]
        for grade in reversed(grades):
            z_score = z_scores[grade]
            cutoff = mean_weight + (z_score * sigma_weight)
            if self.weight >= cutoff:
                return grade
            
        return "Copper" # as default

    def determine_colouration(self):
        '''finds a colouration based on other factors (makes it easier for diamond fish to have good colouration)'''

        if self.length_grade == "Diamond":
            colouration_odds = {
            "Intense": 0.5,
            "Vivid": 0.125,
            "Neutral": 0.125,
            "Subdued": 0.125,
            "Pale": 0.125,
            }
        elif self.length_grade == "Platinum":
            colouration_odds = {
            "Intense": 0.2,
            "Vivid": 0.2,
            "Neutral": 0.2,
            "Subdued": 0.2,
            "Pale": 0.2,
            }
        else: 
            colouration_odds = {
            "Intense": 0.05,
            "Vivid": 0.2,
            "Neutral": 0.4,
            "Subdued": 0.25,
            "Pale": 0.1,
            }
        
        colouration = random.choices(list(colouration_odds.keys()), weights=list(colouration_odds.values()), k=1)[0]

        return colouration
    
    def determine_condition(self):
        '''finds a condition based on length (to make it slightly easier to get great fish)'''

        if self.length_grade == "Diamond":
            condition_odds = {
            "Pristine": 0.5,
            "Excellent": 0.125,
            "Good": 0.125,
            "Fair": 0.125,
            "Poor": 0.125,
            }
        elif self.length_grade == "Platinum":
            condition_odds = {
            "Pristine": 0.2,
            "Excellent": 0.2,
            "Good": 0.2,
            "Fair": 0.2,
            "Poor": 0.2,
            }
        else: 
            condition_odds = {
            "Pristine": 0.05,
            "Excellent": 0.2,
            "Good": 0.4,
            "Fair": 0.25,
            "Poor": 0.1,
            }
        
        condition = random.choices(list(condition_odds.keys()), weights=list(condition_odds.values()), k=1)[0]

        return condition

    def determine_overall_grade(self):
        '''find the overall grade for a fish based on the factors outlined'''

        if self.length_grade == "Diamond":
            length_grade_numeric = 500
        elif self.length_grade == "Platinum":
            length_grade_numeric = 400
        elif self.length_grade == "Gold":
            length_grade_numeric = 300
        elif self.length_grade == "Silver":
            length_grade_numeric = 200
        elif self.length_grade == "Bronze":
            length_grade_numeric = 100
        else:
            length_grade_numeric = -100

        if self.weight_grade == "Diamond":
            weight_grade_numeric = 50
        elif self.weight_grade == "Platinum":
            weight_grade_numeric = 40
        elif self.weight_grade == "Gold":
            weight_grade_numeric = 30
        elif self.weight_grade == "Silver":
            weight_grade_numeric = 20
        elif self.weight_grade == "Bronze":
            weight_grade_numeric = 10
        else:
            weight_grade_numeric = -100

        if self.colouration == "Intense":
            colouration_numeric = 5
        elif self.colouration == "Vivid":
            colouration_numeric = 4
        elif self.colouration == "Neutral":
            colouration_numeric = 3
        elif self.colouration == "Subdued":
            colouration_numeric = 2
        elif self.colouration == "Pale":
            colouration_numeric = 1

        if self.condition == "Pristine":
            condition_numeric = 5
        elif self.condition == "Excellent":
            condition_numeric = 4
        elif self.condition == "Good":
            condition_numeric = 3
        elif self.condition == "Fair":
            condition_numeric = 2
        elif self.condition == "Poor":
            condition_numeric = 1

        grade_raw = length_grade_numeric + weight_grade_numeric + colouration_numeric + condition_numeric
            
        if grade_raw == 560:
            grade = "Perfect"
        elif grade_raw >= 558:
            grade = "Diamond"
        elif grade_raw >= 446:
            grade = "Platinum"
        elif grade_raw >= 335:
            grade = "Gold"
        elif grade_raw >= 223:
            grade = "Silver"
        elif grade_raw > 0:
            grade = "Bronze"
        elif grade_raw == -198:
            grade = "Rotten"
        else:
            grade = "Copper"

        return grade


