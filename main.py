# Welcome to Fishtown :)
# main.py - core gameplay loop

import random
from fish import Species, Fish
from player import Player
import tkinter as tk
from tkinter import messagebox
from locations import Location
from gear import Gear
from achievements import Achievement

def get_species():
    '''create the species list'''

    # original small species list, leaving for posterity
    '''species_list = [
    Species("Bluegill", "A small, common freshwater fish found in ponds and lakes.", "bronze", 0.5, 6, 1, 0.1, 0.02),
    Species("Largemouth Bass", "A popular game fish known for its aggressive strikes.", "bronze", 0.6, 18, 3, 0.15, 0.05),
    Species("Rainbow Trout", "A colorful freshwater fish prized by anglers.", "silver", 0.3, 16, 2, 0.12, 0.04),
    Species("Atlantic Salmon", "A sleek, powerful fish found in cold rivers and oceans.", "gold", 0.15, 30, 4, 0.25, 0.08),
    Species("Northern Pike", "A predatory fish with sharp teeth and a sleek body.", "gold", 0.1, 40, 5, 0.3, 0.1),
    Species("Bluefin Tuna", "A massive, fast-swimming ocean predator highly valued in sushi.", "platinum", 0.05, 80, 10, 1.5, 0.5),
    Species("Swordfish", "An iconic deep-sea fish known for its elongated bill.", "platinum", 0.03, 120, 15, 2.5, 0.7),
    Species("Golden Dorado", "A stunning, rare freshwater fish revered by anglers.", "diamond", 0.02, 36, 6, 0.6, 0.2),
    Species("Giant Trevally", "A strong ocean fish sought after for its challenge and size.", "diamond", 0.01, 48, 8, 0.8, 0.3),
    Species("Arctic Char", "A rare, cold-water fish with vibrant coloration.", "diamond", 0.005, 28, 3, 0.18, 0.05)
    ]'''

    species_list = [
    Species("Bluegill", "A small, common freshwater fish found in ponds and lakes.", "bronze", 0.8, 20, 5, 0.5, 0.15),
    Species("Largemouth Bass", "A popular game fish known for its aggressive strikes.", "bronze", 0.7, 45, 10, 0.8, 0.2),
    Species("Pumpkinseed Sunfish", "A colorful sunfish commonly found in ponds and lakes.", "bronze", 0.75, 18, 4, 0.4, 0.1),
    Species("Yellow Perch", "A small, yellow fish with black vertical stripes.", "silver", 0.6, 30, 8, 0.6, 0.18),
    Species("Northern Pike", "A predatory fish with sharp teeth and a sleek body.", "silver", 0.55, 70, 12, 1.2, 0.25),
    Species("Catfish", "A bottom-dwelling fish with a wide range of sizes.", "silver", 0.5, 60, 15, 1.0, 0.3),
    Species("Crappie", "A popular panfish known for its delicate taste and light catch.", "gold", 0.4, 40, 10, 0.7, 0.2),
    Species("Muskellunge", "A large and rare predator fish found in northern waters.", "gold", 0.3, 120, 20, 2.0, 0.4),
    Species("Walleye", "A predatory fish known for its sharp eyes and taste.", "platinum", 0.25, 60, 18, 1.5, 0.35),
    Species("Giant Freshwater Ray", "A massive, rare fish with incredible strength.", "diamond", 0.05, 250, 40, 3.0, 0.5),
    Species("Rainbow Trout", "A colorful freshwater fish prized by anglers.", "bronze", 0.75, 40, 7, 0.6, 0.15),
    Species("Brook Trout", "A small freshwater fish found in cold, fast-moving streams.", "bronze", 0.8, 30, 6, 0.5, 0.2),
    Species("Brown Trout", "A hearty fish with a distinct brown coloration, commonly found in rivers.", "bronze", 0.7, 50, 8, 0.7, 0.2),
    Species("Atlantic Salmon", "A migratory fish with excellent fighting abilities, native to rivers.", "silver", 0.6, 80, 15, 1.2, 0.3),
    Species("Steelhead Salmon", "A variant of the rainbow trout, known for its ocean migrations.", "silver", 0.55, 75, 12, 1.1, 0.25),
    Species("Smallmouth Bass", "A popular river fish known for its strong fight.", "silver", 0.5, 35, 7, 1.0, 0.25),
    Species("Channel Catfish", "A bottom-dwelling river fish known for its whiskers and aggressive bite.", "gold", 0.45, 70, 14, 1.3, 0.3),
    Species("Flathead Catfish", "A large, predatory catfish found in slow-moving river bends.", "gold", 0.4, 100, 18, 1.7, 0.35),
    Species("Tiger Muskie", "A hybrid of muskellunge and northern pike, known for its size and strength.", "platinum", 0.2, 130, 24, 2.0, 0.45),
    Species("Paddlefish", "A prehistoric river fish with a long, flat snout and filter-feeding habits.", "diamond", 0.15, 150, 30, 2.5, 0.45),
    Species("American Shad", "A migratory species known for its remarkable spawning runs.", "bronze", 0.7, 20, 5, 0.8, 0.2),
    Species("Coho Salmon", "A cold-water salmon with a silver sheen, prized by anglers.", "bronze", 0.6, 25, 6, 0.9, 0.3),
    Species("Alligator Gar", "A large, prehistoric fish known for its toothy grin and armored scales.", "silver", 0.5, 150, 30, 2.0, 0.4),
    Species("Peacock Bass", "A colorful, predatory species native to South American waters.", "silver", 0.4, 30, 7, 1.0, 0.3),
    Species("Clown Knifefish", "A predatory fish with a unique body shape and long fin, native to Southeast Asia.", "silver", 0.3, 36, 8, 1.1, 0.4),
    Species("Snakehead", "An aggressive, invasive species with a voracious appetite.", "gold", 0.35, 45, 9, 1.2, 0.5),
    Species("Oscar", "A highly intelligent, territorial cichlid found in slow-moving waters.", "gold", 0.3, 18, 5, 0.7, 0.25),
    Species("Golden Shiner", "A small, common baitfish that thrives in lakes and ponds.", "platinum", 0.2, 12, 3, 0.4, 0.1),
    Species("Panfish", "A variety of small fish that includes bluegill, sunfish, and crappie.", "platinum", 0.2, 10, 2, 0.3, 0.1),
    Species("Midas Cichlid", "A beautiful freshwater fish, known for its bright colors and territorial behavior.", "diamond", 0.1, 15, 4, 0.6, 0.2),
    Species("American Sturgeon", "A large, ancient fish known for its bony plates and powerful swim.", "silver", 0.6, 72, 12, 4.0, 0.7),
    Species("Black Acara", "A striking freshwater cichlid with vibrant blue and black coloration.", "silver", 0.4, 18, 5, 0.7, 0.3),
    Species("Jaguar Guapote", "A predatory fish from Central America with a beautiful spotted pattern.", "gold", 0.5, 24, 6, 1.0, 0.4),
    Species("Musky Fish", "A large predatory fish known for its elusive nature and razor-sharp teeth.", "gold", 0.45, 50, 10, 1.5, 0.5),
    Species("American Eel", "A long, snake-like fish found in freshwater rivers and lakes.", "silver", 0.5, 36, 8, 1.2, 0.4),
    Species("Freshwater Snook", "A predator found in both salt and freshwater, known for its fight.", "gold", 0.4, 30, 7, 1.3, 0.6),
    Species("Grass Carp", "A herbivorous species that can grow to massive sizes in slow-moving waters.", "silver", 0.35, 72, 15, 3.0, 0.7),
    Species("Brown Bullhead", "A bottom-dwelling fish with a catfish-like appearance, known for its hardy nature.", "bronze", 0.6, 14, 4, 0.5, 0.2),
    Species("Chain Pickerel", "A slender predator with sharp teeth, resembling a smaller pike.", "silver", 0.5, 24, 6, 0.8, 0.3),
    Species("Airbreathing Catfish", "A fish that can gulp air, allowing it to thrive in low-oxygen waters.", "diamond", 0.3, 36, 8, 1.5, 0.5),
    Species("Mackerel", "A fast-swimming fish found in schools.", "bronze", 0.25, 14, 3, 0.2, 1.5),
    Species("Sardine", "A small, silvery fish often caught in large numbers.", "bronze", 0.3, 6, 1.5, 0.1, 0.5),
    Species("Triggerfish", "A reef-dwelling fish with strong jaws.", "bronze", 0.2, 12, 2.5, 0.3, 1.2),
    Species("Grunt Fish", "Named for the grunting sounds they make.", "bronze", 0.25, 10, 2, 0.25, 1),
    Species("Bonito", "A torpedo-shaped fish related to tuna.", "bronze", 0.15, 20, 4, 0.5, 2),
    Species("Hogfish", "A reef fish known for its pig-like snout.", "silver", 0.1, 18, 3.5, 0.6, 2.5),
    Species("Lookdown Fish", "A shiny, disk-shaped fish with a reflective body.", "silver", 0.1, 16, 3, 0.4, 2),
    Species("Spotted Drum", "A striking black-and-white fish with a long dorsal fin.", "silver", 0.08, 14, 3, 0.35, 1.8),
    Species("Blacktip Shark", "A sleek shark species common in shallow waters.", "silver", 0.07, 50, 6, 2.5, 5),
    Species("Yellowtail Snapper", "A colorful snapper with a bright yellow stripe.", "silver", 0.08, 24, 5, 1.2, 3),
    Species("Barracuda", "A fierce predator with razor-sharp teeth.", "gold", 0.05, 36, 6, 2, 4.5),
    Species("Queen Angelfish", "A vibrant reef fish with electric blue and yellow colors.", "gold", 0.06, 18, 4, 0.8, 2.8),
    Species("Cobia", "A powerful fish known for its shark-like appearance.", "gold", 0.04, 40, 7, 2.8, 6),
    Species("Tarpon", "A large, silver fish famous for its leaps.", "gold", 0.03, 60, 8, 3, 7),
    Species("Mahi-Mahi", "A dazzling blue-green fish prized for its speed and taste.", "gold", 0.02, 48, 7, 2.2, 5.5),
    Species("Sailfish", "One of the fastest fish in the ocean, with a massive sail-like fin.", "platinum", 0.015, 70, 9, 3.5, 8),
    Species("Bluefin Tuna", "A highly prized deep-sea fish known for its strength.", "platinum", 0.01, 96, 10, 4, 10),
    Species("Goliath Grouper", "A massive reef fish capable of reaching enormous sizes.", "platinum", 0.008, 84, 12, 4.5, 12),
    Species("Oarfish", "A mysterious deep-sea fish with a long, ribbon-like body.", "diamond", 0.005, 200, 20, 6, 15),
    Species("Lunar Tetra", "A small, shimmering fish with a bioluminescent glow, illuminating the darkest waters.", "gold", 0.2, 12, 4, 0.3, 0.1),
    Species("Ghostly Trout", "A semi-transparent trout that glows faintly in moonlight, adding to its mysterious allure.", "platinum", 0.3, 24, 6, 0.8, 0.4),
    Species("Silverfin Leviathan", "A massive, mythical creature with glowing silver scales that can be seen from miles away.", "diamond", 0.5, 240, 40, 12.0, 2.5),
    Species("Frostbite Salmon", "A rare salmon with icy blue markings that thrive in frigid waters, said to grant strength.", "platinum", 0.6, 35, 7, 1.5, 0.7),
    Species("Aurora Sturgeon", "A mythical fish with vibrant, shifting colors, like the northern lights under the water.", "diamond", 0.4, 120, 20, 5.5, 1.2),
    Species("Crimson Merman Fish", "A deep-sea dweller with long, flowing fins that resemble the legendary merman.", "gold", 0.5, 65, 10, 3.0, 0.9),
    Species("Violet Spotted Pike", "A predatory fish with electric violet spots that flash when hunting.", "gold", 0.7, 45, 8, 1.2, 0.5),
    Species("Cursed Rayfish", "A ray with spiny barbs that glow ominously in the dark, rumored to curse those who catch it.", "platinum", 0.3, 80, 15, 4.5, 1.0),
    Species("Crystal Carp", "A translucent carp whose scales reflect light like crystal, making it nearly invisible underwater.", "diamond", 0.3, 28, 6, 1.0, 0.3),
    Species("Nightmare Fangtooth", "A vicious fish with enormous fang-like teeth and glowing red eyes, often feared by other fish.", "diamond", 0.2, 18, 4, 0.9, 0.2),
    Species("Abyssal Emperor", "A regal fish with long, flowing fins and a crown-like structure on its head, known as the king of the spring waters.", "diamond", 0.5, 200, 50, 10.0, 2.5),
    Species("Phoenix Carp", "A radiant, fiery-orange carp that is said to be reborn every century, with flames dancing on its scales.", "diamond", 0.4, 75, 20, 5.0, 1.5),
    Species("Eternal Serpent", "A snake-like fish that coils in the deep waters, revered for its ancient wisdom and mystical abilities.", "diamond", 0.6, 150, 40, 7.5, 2.0),
    Species("Golden Leviathan", "A colossal fish that glimmers like molten gold, known for its strength and size.", "platinum", 0.3, 300, 60, 15.0, 3.0),
    Species("Springwater Dragonfish", "A legendary dragonfish that glides through the waters with shimmering green scales and fierce, jagged fins.", "platinum", 0.4, 120, 30, 8.0, 2.5),
    Species("Celestial Sturgeon", "A giant, silver-blue sturgeon with stars reflected on its scales, often spotted during the rare celestial alignments.", "diamond", 0.2, 250, 70, 18.0, 4.0),
    Species("Moonlit Barracuda", "A sleek and powerful fish that moves with lightning speed, glowing faintly in the moonlight.", "platinum", 0.5, 45, 15, 2.5, 1.0),
    Species("Hydra Bass", "A multi-headed bass that regenerates quickly, said to be nearly impossible to defeat in a fishing contest.", "gold", 0.7, 60, 12, 3.0, 1.2),
    Species("Emerald Glimmerfish", "A glowing fish with radiant green scales that seem to pulse with light, known for its elusive nature.", "gold", 0.3, 30, 8, 1.5, 0.5),
    Species("Crystalfin Monarch", "A shimmering fish with scales like precious gems, its movement as elegant as a royal parade.", "gold", 0.4, 85, 25, 4.0, 1.0)
    ]

    return species_list

def get_locations(player):
    '''create the locations list. checks if player has unlocked any locations beyond the default'''

    locations_list = [
        Location("Local Pond", 0, True),
        Location("Timberflow River", 1000),
        Location("Blueberry Lake", 2000),
        Location("Titan Lake", 5000),
        Location("Deep Blue Sea", 10000),
        Location("Twilight Fjord", 25000),
        Location("Eternal Springs", 100000),
    ]

    for location in locations_list:
        if location.name in player.unlocked_locations:
            location.unlocked = True

    return locations_list

def get_species_by_location(location):
    '''gets available species by fishing location'''

    species_dict = {
        "Local Pond": [
    Species("Bluegill", "A small, common freshwater fish found in ponds and lakes.", "bronze", 0.8, 20, 5, 0.5, 0.15),
    Species("Largemouth Bass", "A popular game fish known for its aggressive strikes.", "bronze", 0.7, 45, 10, 0.8, 0.2),
    Species("Pumpkinseed Sunfish", "A colorful sunfish commonly found in ponds and lakes.", "bronze", 0.75, 18, 4, 0.4, 0.1),
    Species("Yellow Perch", "A small, yellow fish with black vertical stripes.", "silver", 0.6, 30, 8, 0.6, 0.18),
    Species("Northern Pike", "A predatory fish with sharp teeth and a sleek body.", "silver", 0.55, 70, 12, 1.2, 0.25),
    Species("Catfish", "A bottom-dwelling fish with a wide range of sizes.", "silver", 0.5, 60, 15, 1.0, 0.3),
    Species("Crappie", "A popular panfish known for its delicate taste and light catch.", "gold", 0.4, 40, 10, 0.7, 0.2),
    Species("Muskellunge", "A large and rare predator fish found in northern waters.", "gold", 0.3, 120, 20, 2.0, 0.4),
    Species("Walleye", "A predatory fish known for its sharp eyes and taste.", "platinum", 0.25, 60, 18, 1.5, 0.35),
    Species("Giant Freshwater Ray", "A massive, rare fish with incredible strength.", "diamond", 0.05, 250, 40, 3.0, 0.5)
        ],
        "Timberflow River": [
    Species("Rainbow Trout", "A colorful freshwater fish prized by anglers.", "bronze", 0.75, 40, 7, 0.6, 0.15),
    Species("Brook Trout", "A small freshwater fish found in cold, fast-moving streams.", "bronze", 0.8, 30, 6, 0.5, 0.2),
    Species("Brown Trout", "A hearty fish with a distinct brown coloration, commonly found in rivers.", "bronze", 0.7, 50, 8, 0.7, 0.2),
    Species("Atlantic Salmon", "A migratory fish with excellent fighting abilities, native to rivers.", "silver", 0.6, 80, 15, 1.2, 0.3),
    Species("Steelhead Salmon", "A variant of the rainbow trout, known for its ocean migrations.", "silver", 0.55, 75, 12, 1.1, 0.25),
    Species("Smallmouth Bass", "A popular river fish known for its strong fight.", "silver", 0.5, 35, 7, 1.0, 0.25),
    Species("Channel Catfish", "A bottom-dwelling river fish known for its whiskers and aggressive bite.", "gold", 0.45, 70, 14, 1.3, 0.3),
    Species("Flathead Catfish", "A large, predatory catfish found in slow-moving river bends.", "gold", 0.4, 100, 18, 1.7, 0.35),
    Species("Tiger Muskie", "A hybrid of muskellunge and northern pike, known for its size and strength.", "platinum", 0.2, 130, 24, 2.0, 0.45),
    Species("Paddlefish", "A prehistoric river fish with a long, flat snout and filter-feeding habits.", "diamond", 0.15, 150, 30, 2.5, 0.45)
        ],
        "Blueberry Lake": [
    Species("American Shad", "A migratory species known for its remarkable spawning runs.", "bronze", 0.7, 20, 5, 0.8, 0.2),
    Species("Coho Salmon", "A cold-water salmon with a silver sheen, prized by anglers.", "bronze", 0.6, 25, 6, 0.9, 0.3),
    Species("Alligator Gar", "A large, prehistoric fish known for its toothy grin and armored scales.", "silver", 0.5, 150, 30, 2.0, 0.4),
    Species("Peacock Bass", "A colorful, predatory species native to South American waters.", "silver", 0.4, 30, 7, 1.0, 0.3),
    Species("Clown Knifefish", "A predatory fish with a unique body shape and long fin, native to Southeast Asia.", "silver", 0.3, 36, 8, 1.1, 0.4),
    Species("Snakehead", "An aggressive, invasive species with a voracious appetite.", "gold", 0.35, 45, 9, 1.2, 0.5),
    Species("Oscar", "A highly intelligent, territorial cichlid found in slow-moving waters.", "gold", 0.3, 18, 5, 0.7, 0.25),
    Species("Golden Shiner", "A small, common baitfish that thrives in lakes and ponds.", "platinum", 0.2, 12, 3, 0.4, 0.1),
    Species("Panfish", "A variety of small fish that includes bluegill, sunfish, and crappie.", "platinum", 0.2, 10, 2, 0.3, 0.1),
    Species("Midas Cichlid", "A beautiful freshwater fish, known for its bright colors and territorial behavior.", "diamond", 0.1, 15, 4, 0.6, 0.2)
        ],
        "Titan Lake": [
    Species("American Sturgeon", "A large, ancient fish known for its bony plates and powerful swim.", "silver", 0.6, 72, 12, 4.0, 0.7),
    Species("Black Acara", "A striking freshwater cichlid with vibrant blue and black coloration.", "silver", 0.4, 18, 5, 0.7, 0.3),
    Species("Jaguar Guapote", "A predatory fish from Central America with a beautiful spotted pattern.", "gold", 0.5, 24, 6, 1.0, 0.4),
    Species("Musky Fish", "A large predatory fish known for its elusive nature and razor-sharp teeth.", "gold", 0.45, 50, 10, 1.5, 0.5),
    Species("American Eel", "A long, snake-like fish found in freshwater rivers and lakes.", "silver", 0.5, 36, 8, 1.2, 0.4),
    Species("Freshwater Snook", "A predator found in both salt and freshwater, known for its fight.", "gold", 0.4, 30, 7, 1.3, 0.6),
    Species("Grass Carp", "A herbivorous species that can grow to massive sizes in slow-moving waters.", "silver", 0.35, 72, 15, 3.0, 0.7),
    Species("Brown Bullhead", "A bottom-dwelling fish with a catfish-like appearance, known for its hardy nature.", "bronze", 0.6, 14, 4, 0.5, 0.2),
    Species("Chain Pickerel", "A slender predator with sharp teeth, resembling a smaller pike.", "silver", 0.5, 24, 6, 0.8, 0.3),
    Species("Airbreathing Catfish", "A fish that can gulp air, allowing it to thrive in low-oxygen waters.", "diamond", 0.3, 36, 8, 1.5, 0.5)
        ],
        "Deep Blue Sea": [
    Species("Mackerel", "A fast-swimming fish found in schools.", "bronze", 0.25, 14, 3, 0.2, 1.5),
    Species("Sardine", "A small, silvery fish often caught in large numbers.", "bronze", 0.3, 6, 1.5, 0.1, 0.5),
    Species("Triggerfish", "A reef-dwelling fish with strong jaws.", "bronze", 0.2, 12, 2.5, 0.3, 1.2),
    Species("Grunt Fish", "Named for the grunting sounds they make.", "bronze", 0.25, 10, 2, 0.25, 1),
    Species("Bonito", "A torpedo-shaped fish related to tuna.", "bronze", 0.15, 20, 4, 0.5, 2),
    Species("Hogfish", "A reef fish known for its pig-like snout.", "silver", 0.1, 18, 3.5, 0.6, 2.5),
    Species("Lookdown Fish", "A shiny, disk-shaped fish with a reflective body.", "silver", 0.1, 16, 3, 0.4, 2),
    Species("Spotted Drum", "A striking black-and-white fish with a long dorsal fin.", "silver", 0.08, 14, 3, 0.35, 1.8),
    Species("Blacktip Shark", "A sleek shark species common in shallow waters.", "silver", 0.07, 50, 6, 2.5, 5),
    Species("Yellowtail Snapper", "A colorful snapper with a bright yellow stripe.", "silver", 0.08, 24, 5, 1.2, 3),
    Species("Barracuda", "A fierce predator with razor-sharp teeth.", "gold", 0.05, 36, 6, 2, 4.5),
    Species("Queen Angelfish", "A vibrant reef fish with electric blue and yellow colors.", "gold", 0.06, 18, 4, 0.8, 2.8),
    Species("Cobia", "A powerful fish known for its shark-like appearance.", "gold", 0.04, 40, 7, 2.8, 6),
    Species("Tarpon", "A large, silver fish famous for its leaps.", "gold", 0.03, 60, 8, 3, 7),
    Species("Mahi-Mahi", "A dazzling blue-green fish prized for its speed and taste.", "gold", 0.02, 48, 7, 2.2, 5.5),
    Species("Sailfish", "One of the fastest fish in the ocean, with a massive sail-like fin.", "platinum", 0.015, 70, 9, 3.5, 8),
    Species("Bluefin Tuna", "A highly prized deep-sea fish known for its strength.", "platinum", 0.01, 96, 10, 4, 10),
    Species("Goliath Grouper", "A massive reef fish capable of reaching enormous sizes.", "platinum", 0.008, 84, 12, 4.5, 12),
    Species("Oarfish", "A mysterious deep-sea fish with a long, ribbon-like body.", "diamond", 0.005, 200, 20, 6, 15)
        ],
        "Twilight Fjord": [
    Species("Lunar Tetra", "A small, shimmering fish with a bioluminescent glow, illuminating the darkest waters.", "gold", 0.2, 12, 4, 0.3, 0.1),
    Species("Ghostly Trout", "A semi-transparent trout that glows faintly in moonlight, adding to its mysterious allure.", "platinum", 0.3, 24, 6, 0.8, 0.4),
    Species("Silverfin Leviathan", "A massive, mythical creature with glowing silver scales that can be seen from miles away.", "diamond", 0.5, 240, 40, 12.0, 2.5),
    Species("Frostbite Salmon", "A rare salmon with icy blue markings that thrive in frigid waters, said to grant strength.", "platinum", 0.6, 35, 7, 1.5, 0.7),
    Species("Aurora Sturgeon", "A mythical fish with vibrant, shifting colors, like the northern lights under the water.", "diamond", 0.4, 120, 20, 5.5, 1.2),
    Species("Crimson Merman Fish", "A deep-sea dweller with long, flowing fins that resemble the legendary merman.", "gold", 0.5, 65, 10, 3.0, 0.9),
    Species("Violet Spotted Pike", "A predatory fish with electric violet spots that flash when hunting.", "gold", 0.7, 45, 8, 1.2, 0.5),
    Species("Cursed Rayfish", "A ray with spiny barbs that glow ominously in the dark, rumored to curse those who catch it.", "platinum", 0.3, 80, 15, 4.5, 1.0),
    Species("Crystal Carp", "A translucent carp whose scales reflect light like crystal, making it nearly invisible underwater.", "diamond", 0.3, 28, 6, 1.0, 0.3),
    Species("Nightmare Fangtooth", "A vicious fish with enormous fang-like teeth and glowing red eyes, often feared by other fish.", "diamond", 0.2, 18, 4, 0.9, 0.2)
        ],
        "Eternal Springs": [
    Species("Abyssal Emperor", "A regal fish with long, flowing fins and a crown-like structure on its head, known as the king of the spring waters.", "diamond", 0.5, 200, 50, 10.0, 2.5),
    Species("Phoenix Carp", "A radiant, fiery-orange carp that is said to be reborn every century, with flames dancing on its scales.", "diamond", 0.4, 75, 20, 5.0, 1.5),
    Species("Eternal Serpent", "A snake-like fish that coils in the deep waters, revered for its ancient wisdom and mystical abilities.", "diamond", 0.6, 150, 40, 7.5, 2.0),
    Species("Golden Leviathan", "A colossal fish that glimmers like molten gold, known for its strength and size.", "platinum", 0.3, 300, 60, 15.0, 3.0),
    Species("Springwater Dragonfish", "A legendary dragonfish that glides through the waters with shimmering green scales and fierce, jagged fins.", "platinum", 0.4, 120, 30, 8.0, 2.5),
    Species("Celestial Sturgeon", "A giant, silver-blue sturgeon with stars reflected on its scales, often spotted during the rare celestial alignments.", "diamond", 0.2, 250, 70, 18.0, 4.0),
    Species("Moonlit Barracuda", "A sleek and powerful fish that moves with lightning speed, glowing faintly in the moonlight.", "platinum", 0.5, 45, 15, 2.5, 1.0),
    Species("Hydra Bass", "A multi-headed bass that regenerates quickly, said to be nearly impossible to defeat in a fishing contest.", "gold", 0.7, 60, 12, 3.0, 1.2),
    Species("Emerald Glimmerfish", "A glowing fish with radiant green scales that seem to pulse with light, known for its elusive nature.", "gold", 0.3, 30, 8, 1.5, 0.5),
    Species("Crystalfin Monarch", "A shimmering fish with scales like precious gems, its movement as elegant as a royal parade.", "gold", 0.4, 85, 25, 4.0, 1.0)
        ]
    }

    return species_dict.get(location.name, [])

def get_items_for_sale():
    '''gets the current sale items'''

    sale_list = [
        Gear("Basic Fishing Rod", 10, True, False),
        Gear("Bronze Fishing Rod", 500, False, False),
        Gear("Silver Fishing Rod", 2000, False, False),
        Gear("Gold Fishing Rod", 5000, False, False)
    ]

    return sale_list

    
class GameApp:
    def __init__(self, root):

        # Game info
        self.species_list = get_species()

        # Root tkinter stuff
        self.root = root
        self.root.title("Fishtown")
        self.root.geometry("1306x735")  # Set the window size 

        # game icon
        root.iconbitmap("images/icon.ico") 

        # Bind the window close (X button) to on_close method
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Background image
        self.bg_image = tk.PhotoImage(file = "images/bg_1306_735.gif")
        #self.bg_image = self.bg_image.subsample(2,2)
        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(relwidth=1,relheight=1) # stretch to fill window

        # Placeholder for player instance (initially None)
        self.player = None

        # Label for Welcome Message
        self.welcome_label = tk.Label(self.root, text="🎣 Welcome to FishTown! 🐟",
                                    font=("Times New Roman", 30, "bold"),
                                    fg="dodger blue")
        self.welcome_label.pack(side="top", pady=10)

        # Label for username prompt
        self.username_label = tk.Label(self.root, text="Enter your username:")
        self.username_label.pack(side="top", pady=10)

        # Entry field for username
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(side="top", pady=10)

        # Game Options - initially hidden
        self.main_menu_label = tk.Label(self.root, text="🎣 Welcome to FishTown! 🐟",
                                    font=("Times New Roman", 30, "bold"),
                                    fg="dodger blue")
        # Go fish image and button
        self.go_fish_image = tk.PhotoImage(file = "images/go_fish.gif")
        self.go_fishing_button = tk.Button(self.root, 
                                   text="Go Fishing",
                                   image=self.go_fish_image,
                                   compound='top', 
                                   bg=self.root['bg'], # respect background color of tkinter window
                                   command=lambda: self.go_fishing(self.species_list, self.player)) # lambda means this function isn't called immediately.
        # Shop image and button
        self.shop_image = tk.PhotoImage(file = "images/shop.gif")
        self.shop_button = tk.Button(self.root, text="Shop", image=self.shop_image, compound="top", command=self.go_shopping)
        # Encyclopedia image and button
        self.encyclopedia_image = tk.PhotoImage(file = "images/encyclopedia.gif")
        self.encyclopedia_button = tk.Button(self.root, text="Encyclopedia", image=self.encyclopedia_image, compound="top", command=self.view_encyclopedia)
        # Location image and button
        self.location_image = tk.PhotoImage(file = "images/location.gif")
        self.locations_button = tk.Button(self.root, text="Locations", image=self.location_image, compound="top", command=self.view_locations)
        # Gear image and button
        self.gear_image = tk.PhotoImage(file = "images/gear.gif")
        self.gear_button = tk.Button(self.root, text="Gear", image=self.gear_image, compound="top", command=self.view_gear)
        # Achievements image and button
        self.achievements_image = tk.PhotoImage(file = "images/achievement.gif")
        self.achievements_button = tk.Button(self.root,text="Achievements", image=self.achievements_image, compound="top", command=self.view_achievements)
        # Help image and button
        self.help_image = tk.PhotoImage(file="images/help.gif")
        self.help_button = tk.Button(self.root, text="Help", image=self.help_image, compound="top", command=self.view_help)
        # Quit image and button
        self.quit_image = tk.PhotoImage(file = "images/quit2.gif")
        self.quit_button = tk.Button(self.root, text="Quit", image=self.quit_image, compound="top", command=self.quit_game)

        # Button to start the game (after entering the username)
        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.start_button.pack(side="top", pady=10)

        # Fishing page options
        self.catch_fish_button = tk.Button(self.root, 
                                   text="Catch Fish!", 
                                   command=lambda: self.fishing_minigame())
        self.back_to_main_button = tk.Button(self.root,text="Main Menu", command=self.show_main_menu)

        # Create a Text widget for logging actions
        self.textbox = tk.Text(self.root, height=5, width=120, wrap=tk.WORD, state=tk.DISABLED, font=("Arial", 10))

        # Shopping page buttons
        self.sell_1_fish_button = tk.Button(self.root, text="Sell One", command=self.sell_one)
        self.sell_all_fish_button = tk.Button(self.root, text="Sell All", command=self.sell_all)

        # Shopping page salesbox
        self.sales_image = tk.PhotoImage(file = "images/shop.gif")
        self.sales_label = tk.Label(self.root, text="Items for Sale", image=self.sales_image, compound="top", font=("Times New Roman", 14))
        self.sales_listbox = tk.Listbox(self.root, height=5, width=30, font=("Times New Roman", 10))
        self.buy_one_button = tk.Button(self.root, text="Buy Selected Item", command=self.buy_one)

        # Encyclopedia page buttons and options
        self.caught_species_button = tk.Button(self.root, text="View Caught Species", command=self.caught_species)
        self.caught_species_textbox = tk.Text(self.root, height=40, width=50, font=("Times New Roman",10))

        # Caught Species Page options
        self.back_to_encyclopedia_button = tk.Button(self.root, text="Back to Encyclopedia", command=self.view_encyclopedia)

        # Inventory image and buttons - initially hidden
        self.inventory_image = tk.PhotoImage(file = "images/inventory.gif")
        self.inventory_label = tk.Label(self.root, text="Inventory", image=self.inventory_image, compound="top", font=("Times New Roman", 14))
        self.inventory_listbox = tk.Listbox(self.root, height=16, width=40, font=("Times New Roman", 10))

        # Location placeholder
        self.current_location_label = False

        # Player Gold Image - initially hidden
        self.gold_image = tk.PhotoImage(file = "images/gold32x32.png")

        # Gear Page Display
        self.gear_label = tk.Label(self.root, text="Player Gear", image=self.gear_image, compound="top", font=("Times New Roman", 10))
        self.gear_listbox = tk.Listbox(self.root, height=5, width=50, font=("Times New Roman", 10))
        self.equip_item_button = tk.Button(self.root, text="Equip Selected Item", command=self.equip_item) 

        # Achievements Page Display
        self.achievements_label = tk.Label(self.root, text="Player Achievements", image=self.achievements_image, compound="top", font=("Times New Roman", 14)) 
        self.achievements_listbox = tk.Listbox(self.root, height=10, width=120, font=("Times New Roman", 10))

        # Help Page Display
        self.help_textbox = tk.Text(self.root, height=50, width=300, font=("Times New Roman",10))
        

    def start_game(self):

        # Get username data 
        username = self.username_entry.get()

        # Check if the username is not empty
        if username.strip() == "":
            # Display an error if username is empty
            messagebox.showerror("Input Error", "Please enter a valid username.")
            return

        # Create a new player instance with the username
        self.player = Player(username)
        messagebox.showinfo("Welcome", f"Welcome, {self.player.username}!")

        # initialize locations based on player
        self.locations_list = get_locations(self.player)
        self.current_location = self.locations_list[0] # start at Local Pond
        self.location_buttons = []

        # Hide username prompt and start button
        self.username_label.pack_forget()
        self.username_entry.pack_forget()
        self.start_button.pack_forget()
        self.welcome_label.pack_forget()

        # Show game buttons
        self.main_menu_label.pack(side="top", pady=10)
        self.go_fishing_button.pack(side="left", padx=10)
        self.shop_button.pack(side="left", padx=10)
        self.encyclopedia_button.pack(side="left", padx=10)
        self.locations_button.pack(side="left", padx=10)
        self.gear_button.pack(side="left", padx=10)
        self.achievements_button.pack(side="left", padx=10)
        self.help_button.pack(side="left", padx=10)
        self.quit_button.pack(side="left", padx=10)

        # Player gold display
        self.gold_label = tk.Label(self.root, text=f"{self.player.gold}", font=("Times New Roman", 10), image=self.gold_image, compound='top')
        self.gold_label.pack(side="right", padx=10)

        # Player Level display
        self.level_image = tk.PhotoImage(file = "images/level.gif")
        self.level_label = tk.Label(self.root, text = f"Level: {self.player.level}\nXP: {self.player.xp}\nXP to Next Level: {self.player.remaining_xp}", font=("Times New Roman", 10), image=self.level_image, compound='top')
        self.level_label.pack(side="right", padx=10)

        # Inventory widgets
        self.inventory_label.pack(side="top", pady=10)
        self.inventory_listbox.pack(side="top", pady=5)
        self.update_inventory()


    def show_main_menu(self):
        '''show main menu. Often used in the return to main menu buttons.'''

        # Backup player data whenever main menu is accessed.
        self.player.pickle_dump_data()

        # Unbind catch fish key; if applicable
        self.root.unbind("<f>")

        # Hide all buttons first
        self.catch_fish_button.pack_forget()
        self.back_to_main_button.pack_forget()
        self.inventory_label.pack_forget()
        self.inventory_listbox.pack_forget()
        self.textbox.pack_forget()
        self.sell_1_fish_button.pack_forget()
        self.sell_all_fish_button.pack_forget()
        self.caught_species_button.pack_forget()
        self.caught_species_textbox.pack_forget()
        if self.current_location_label:
            self.current_location_label.pack_forget()
        # including location unlocks
        if self.location_buttons != []:
            for location_button in self.location_buttons:
                location_button.pack_forget()
        self.achievements_label.pack_forget()
        self.achievements_listbox.pack_forget()
        self.help_textbox.pack_forget()

        # Show game buttons
        self.main_menu_label.pack(side="top", pady=10)
        self.go_fishing_button.pack(side="left", padx=10)
        self.shop_button.pack(side="left", padx=10)
        self.encyclopedia_button.pack(side="left", padx=10)
        self.locations_button.pack(side="left", padx=10)
        self.gear_button.pack(side="left", padx=10)
        self.achievements_button.pack(side="left", padx=10)
        self.help_button.pack(side="left", padx=10)
        self.quit_button.pack(side="left", padx=10)

        # Inventory widgets
        self.inventory_label.pack(side="top", pady=10)
        self.inventory_listbox.pack(side="top", pady=10)
        self.update_inventory()

        # Player gold display
        self.gold_label.pack(side="right", padx=10)

        # Player Level Display
        self.level_label.pack(side = "right", padx = 10)

        # Hide shop labels
        self.sales_label.pack_forget()
        self.sales_listbox.pack_forget()
        self.buy_one_button.pack_forget()

        # Hide gear labels
        self.gear_label.pack_forget()
        self.gear_listbox.pack_forget()
        self.equip_item_button.pack_forget()

    
    def go_fishing(self,species_list,player):
        '''fishing loop'''

        # Hide buttons I don't want on this page
        self.main_menu_label.pack_forget()
        self.go_fishing_button.pack_forget()
        self.shop_button.pack_forget()
        self.encyclopedia_button.pack_forget()
        self.locations_button.pack_forget()
        self.gear_button.pack_forget()
        self.achievements_button.pack_forget()
        self.help_button.pack_forget()
        self.quit_button.pack_forget()

        # Create and show current location button
        self.current_location_label = tk.Label(self.root, text=f"{self.current_location.name}\nSwitch Locations in Locations Tab", font=("Arial, 10"))
        self.current_location_label.pack(side="left", padx=10)

        # Show the fishing options on the page
        self.catch_fish_button.pack(side="left", padx=10)
        self.back_to_main_button.pack(side="left", padx=10)
        self.textbox.pack(side=tk.BOTTOM, fill=tk.X)

        # Bind f key to catch_fish_button
        self.root.bind("<f>", lambda event: self.fishing_minigame())


    def catch_fish(self,species_list,player):
        '''catch a fish, uses the button defined above'''
        weights = [species.rarity_weight for species in species_list]
        fish_species = random.choices(species_list, weights=weights, k=1)[0]
        if len(player.inventory) < 16:
            if self.minigame_result:
                fish = Fish(fish_species)
                self.update_textbox(f"You caught a {fish}.", color='black')
                player.caught_species[fish_species.name] = True
                player.caught_fish.append(fish)
                player.inventory.append(fish)
                self.update_inventory()
                # update player xp and check level
                prev_level = self.player.get_level(self.player.xp)
                self.player.xp += fish.xp
                self.player.level = self.player.get_level(self.player.xp)
                self.player.remaining_xp = self.player.get_xp_to_next_level(self.player.xp)
                self.level_label.config(text = f"Level: {self.player.level}\nXP: {self.player.xp}\nXP to Next Level: {self.player.remaining_xp}")
                if self.player.level > prev_level:
                    # check if a level up just happened and print a message
                    self.update_textbox(f"Congratulations, you leveled up to level {self.player.level}!", color="green")
                # check for fishing related achievements
                self.player.achievements[0].achieved = True # update for "Fisherman!" achievement
                if fish.species.rarity == 'diamond':
                    if self.player.achievements[1].achieved == False:
                        self.update_textbox(f"Congratulations, you unlocked the {self.player.achievements[1].name} achievement.", color="green")
                    self.player.achievements[1].achieved = True # update for "Diamond in the Rough" achievement
                if fish.grade == "⭐⭐⭐⭐⭐⭐":
                    if self.player.achievements[3].achieved == False:
                        self.update_textbox(f"Congratulations, you unlocked the {self.player.achievements[3].name} achievement.", color="green")
                    self.player.achievements[3].achieved = True # update for "Perfect Catch" achievement
            else:
                messagebox.showinfo("Failed Catch", "You failed to catch a fish this time. Try again!")

        else: 
            messagebox.showinfo("Inventory full", "Your inventory is full. Sell your fish!")

    def fishing_minigame(self):
        '''fishing minigame for catching fish, using a slider'''

        if len(self.player.inventory) >= 16:
            messagebox.showinfo("Inventory full", "Your inventory is full. Sell your fish!")
            return

        # remove for duration of minigame
        self.current_location_label.pack_forget()
        self.catch_fish_button.pack_forget()
        self.back_to_main_button.pack_forget()
        self.textbox.pack_forget()

        # new window for fishing minigame
        self.minigame_window = tk.Toplevel(self.root)
        self.minigame_window.title("Fishing!")
        self.minigame_window.iconbitmap("images/icon.ico") 

        # force focus and bind f key
        self.minigame_window.focus_set()
        self.minigame_window.bind("<f>", lambda event: self.attempt_catch())

        # set up slider
        self.canvas = tk.Canvas(self.minigame_window, width=300, height=50, bg='lightblue')
        self.slider = self.canvas.create_rectangle(20, 15, 30, 35, fill="dodger blue")
        self.target_zone = self.canvas.create_rectangle(140, 15, 160, 35, outline="green", width=3)

        # slider movement
        self.slider_pos = 20
        self.direction = 5
        self.running = True

        # catch button and label
        self.catch_button = tk.Button(self.minigame_window, text="Catch Fish!", font=("Times New Roman", 12), command=self.attempt_catch)
        self.catch_label = tk.Label(self.minigame_window, text="Press when the fish is in the green zone!\nTip: use the f-key to catch!", font=("Times New Roman", 12))
        self.catch_button.pack(pady=10)
        self.catch_label.pack(pady=10)
        # pack the canvas
        self.canvas.pack(pady=10) 

        def move_slider():
            '''continuously move the slider'''
            if not self.running:
                return # if minigame ended
            
            # set base speed. This is subject to change based on fishing rod equipped. Note that a higher number is "slower".
            base_speed = 15

            # find player's equipped rod
            for item in self.player.gear:
                if item.equipped == True:
                    rod_selection = item.name

            # use the equipped rod to slow the slider down
            if rod_selection == "Basic Fishing Rod":
                speed = base_speed
            elif rod_selection == "Bronze Fishing Rod":
                speed = int(base_speed * 1.2)
            elif rod_selection == "Silver Fishing Rod":
                speed = int(base_speed * 1.4)
            elif rod_selection == "Gold Fishing Rod":
                speed = int(base_speed * 2)

            
            self.slider_pos += self.direction
            if self.slider_pos >= 220 or self.slider_pos <= 20:
                self.direction *= -1 # reverse
            self.canvas.coords(self.slider, self.slider_pos, 15, self.slider_pos + 10, 35)
            self.root.after(speed, move_slider)

        # start moving the slider
        move_slider()


    def attempt_catch(self):
        '''attempt a catch'''

        self.running = False
        slider_center = self.slider_pos + 2.5
        distance_from_center = abs(slider_center - 150)
        self.minigame_result = False
        if distance_from_center <= 10:
            self.minigame_result = True
        self.catch_label.config(text="Success!\nNice catch!" if self.minigame_result else "Missed!\nThe one that got away...")
        self.minigame_window.after(1000, self.close_minigame_window)

    def close_minigame_window(self):
        '''closes the minigame window'''
        self.canvas.pack_forget()
        self.catch_button.pack_forget()
        self.catch_label.pack_forget()

        # Unbind
        self.minigame_window.unbind("<f>")
        
        # close minigame window
        self.minigame_window.destroy()

        # re-pack the catch fish button
        self.current_location_label.pack(side="left", padx=10)
        self.catch_fish_button.pack(side="left", padx=10)
        self.back_to_main_button.pack(side="left", padx=10)
        self.textbox.pack(side=tk.BOTTOM, fill=tk.X)

        if self.minigame_result == True:
            self.catch_fish(get_species_by_location(self.current_location), self.player)

    def go_shopping(self):
        '''shopping loop'''

        # Hide buttons I don't want on this page
        self.main_menu_label.pack_forget()
        self.go_fishing_button.pack_forget()
        self.shop_button.pack_forget()
        self.encyclopedia_button.pack_forget()
        self.locations_button.pack_forget()
        self.gear_button.pack_forget()
        self.achievements_button.pack_forget()
        self.help_button.pack_forget()
        self.quit_button.pack_forget()

        # Show shop items
        self.buy_one_button.pack(side="bottom", pady=10)
        self.sales_listbox.pack(side = "bottom", pady=10)
        self.create_sale_items()
        self.sales_label.pack(side = "bottom", pady=10)
        

        # Show shopping options on the page
        self.sell_1_fish_button.pack(side = "top", pady=10)
        self.sell_all_fish_button.pack(side = "top", pady=10)
        self.back_to_main_button.pack(side = "left", padx=10)
        

    def sell_one(self):
        '''sell one fish'''

        # Grab current selection
        selected_index = self.inventory_listbox.curselection()

        # Check if there's no selection
        if not selected_index:
            tk.messagebox.showinfo("No Selection", "Please select a fish to sell.")
            return
        
        # Get correct fish from the selected index
        selected_index = selected_index[0] # curselection uses a tuple, so this extracts from that tuple
        sold_fish = self.player.inventory.pop(selected_index)

        # add gold for selling the fish
        self.player.gold += sold_fish.sell_price
        # check for Moneybags achievement
        if self.player.gold >= 10000:
            self.player.achievements[4].achieved = True
        # update gold label
        self.gold_label.config(text=f"{self.player.gold}")

        # Update inventory display
        self.update_inventory()

        # Show message confirming sale
        tk.messagebox.showinfo("Fish Sold", f"You sold a {sold_fish.species.name} ({sold_fish.grade}) for {sold_fish.sell_price} gold.")

    def sell_all(self):
        '''sell all fish in inventory'''

        total_value = 0
        for fish in self.player.inventory[:]: # slice is needed so that we don't skip fish to sell. 
            total_value += fish.sell_price
            self.player.inventory.remove(fish)
        self.player.gold += total_value
        # check for Moneybags achievement
        if self.player.gold >= 10000:
            self.player.achievements[4].achieved = True

        # Show message confirming sale
        tk.messagebox.showinfo("Fish Sold", f"You have sold all of the fish in your inventory for {total_value} gold.")

        # update gold label
        self.gold_label.config(text=f"{self.player.gold}")

        # Update the inventory at the end            
        self.update_inventory()

    def create_sale_items(self):
        '''creates the items for sale in the shop'''

        self.sales_listbox.delete(0, tk.END)
        self.sale_items = get_items_for_sale()
        for sale_item in self.sale_items:
            self.sales_listbox.insert(tk.END, f"{sale_item.name}, Price: {sale_item.price}")

    def buy_one(self):
        '''buy selected sale item'''

        # Grab current selection
        selected_index = self.sales_listbox.curselection()

        # Check if there's no selection
        if not selected_index:
            tk.messagebox.showinfo("No Selection", "Please select an item to buy.")
            return
        
        # Get correct item from the selected index
        selected_index = selected_index[0] # curselection uses a tuple, so this extracts from that tuple
        bought_item = self.sale_items[selected_index]

        # add gold for selling the fish
        self.player.gold -= bought_item.price
        # update gold label
        self.gold_label.config(text=f"{self.player.gold}")

        # Update player gear
        self.player.gear.append(bought_item)

        # Show message confirming sale
        tk.messagebox.showinfo("Item Bought", f"You bought a {bought_item.name} for {bought_item.price} gold.")

    def view_encyclopedia(self):
        '''encyclopedia options'''

        # Hide buttons I don't want on this page
        self.main_menu_label.pack_forget()
        self.go_fishing_button.pack_forget()
        self.shop_button.pack_forget()
        self.encyclopedia_button.pack_forget()
        self.locations_button.pack_forget()
        self.gear_button.pack_forget()
        self.achievements_button.pack_forget()
        self.help_button.pack_forget()
        self.quit_button.pack_forget()
        self.inventory_label.pack_forget()
        self.inventory_listbox.pack_forget()
        self.back_to_encyclopedia_button.pack_forget()
        self.caught_species_textbox.pack_forget()
        self.gold_label.pack_forget()
        self.level_label.pack_forget()

        # Set up buttons on main encylopedia page
        self.caught_species_button.pack(side="left", padx=10)
        self.back_to_main_button.pack(side="left", padx=10)

    def caught_species(self):
        '''display the list of caught species'''

        # Hide the caught species button from the encyclopedia page
        self.caught_species_button.pack_forget()
        self.back_to_main_button.pack_forget()

        # Display the textbox
        self.caught_species_textbox.pack(side="right", padx=10)
        self.caught_species_textbox.delete(1.0,tk.END) # clear any previous content
        self.caught_species_textbox.tag_configure("uncaught", foreground="red")
        self.caught_species_textbox.tag_configure("caught", foreground="green")
        for species, value in self.player.caught_species.items():
            tag = "caught" if value == True else "uncaught"
            self.caught_species_textbox.insert(tk.END, f"{species}: {value}\n", tag)

        # Display back to encyclopedia button
        self.back_to_encyclopedia_button.pack(side="left", padx=10)

    def view_locations(self):
        '''location options'''

        # Hide buttons I don't want on this page
        self.main_menu_label.pack_forget()
        self.go_fishing_button.pack_forget()
        self.shop_button.pack_forget()
        self.encyclopedia_button.pack_forget()
        self.locations_button.pack_forget()
        self.gear_button.pack_forget()
        self.achievements_button.pack_forget()
        self.help_button.pack_forget()
        self.quit_button.pack_forget()
        self.inventory_label.pack_forget()
        self.inventory_listbox.pack_forget()
        self.back_to_encyclopedia_button.pack_forget()
        self.caught_species_textbox.pack_forget()

        # Set up buttons to show on this page
        self.back_to_main_button.pack(side="left", padx=10)

        # make sure location label is set up
        self.current_location_label = tk.Label(self.root, text=f"{self.current_location.name}\nSwitch Locations in Locations Tab", font=("Arial, 10"))

        # Location buttons
        self.location_buttons = []
        for location in self.locations_list:
            color = "green" if location.unlocked else "red"
            button_text = f"{location.name}\n{'Unlocked' if location.unlocked else f'Locked\n{location.unlock_price} gold'}"
            button = tk.Button(self.root, text=button_text, fg=color, font=("Arial", 10), command=lambda l=location: self.select_or_unlock(l))
            button.pack(pady=5)
            self.location_buttons.append(button)

    def select_or_unlock(self, location):
        '''handles location change or unlock'''

        if location.unlocked:
            self.current_location = location
            messagebox.showinfo("Location changed", f"You moved to {location.name}!")
            self.current_location_label.config(text=f"{self.current_location.name}\nSwitch Locations in Locations Tab")

        else: 
            # unlock location if enough gold
            if self.player.gold >= location.unlock_price:
                self.player.gold -= location.unlock_price
                location.unlocked = True
                # check for location achievement
                self.player.achievements[2].achieved = True # update for "Traveller" achievement
                self.player.unlocked_locations.add(location.name)
                messagebox.showinfo("Location unlocked!", f"You have unlocked {location.name}!")
                self.update_location_buttons()
                # update gold label
                self.gold_label.config(text=f"{self.player.gold}")
            else:
                # player doesn't have enough gold
                messagebox.showwarning("Not enough gold!", f"You do not have enough gold to unlock {location.name}!")
    
    def update_location_buttons(self):
        '''updates location buttons after unlock'''
        for index, location in enumerate(self.locations_list):
            color = "green" if location.unlocked else "red"
            button_text = f"{location.name}\n{'Unlocked' if location.unlocked else f'Locked\n{location.unlock_price} gold'}"
            self.location_buttons[index].config(text=button_text,fg=color)


    def view_gear(self):
        '''view player gear'''

        # Hide buttons I don't want on this page
        self.main_menu_label.pack_forget()
        self.go_fishing_button.pack_forget()
        self.shop_button.pack_forget()
        self.encyclopedia_button.pack_forget()
        self.locations_button.pack_forget()
        self.gear_button.pack_forget()
        self.achievements_button.pack_forget()
        self.help_button.pack_forget()
        self.quit_button.pack_forget()
        self.inventory_label.pack_forget()
        self.inventory_listbox.pack_forget()
        self.back_to_encyclopedia_button.pack_forget()
        self.caught_species_textbox.pack_forget()

        # Set up buttons to show on this page
        self.back_to_main_button.pack(side="left", padx=10)

        # Gear Page Display
        self.gear_label.pack(side="top", pady=10)
        self.gear_listbox.pack(side="top", pady=10)
        self.create_gear_listbox()
        self.equip_item_button.pack(side="top", pady=10)

    def create_gear_listbox(self):
        '''creates the player gear display'''

        self.gear_listbox.delete(0, tk.END)

        for item in self.player.gear:
            self.gear_listbox.insert(tk.END, f"{item.name}, Equipped: {item.equipped}")
            if item.equipped == True:
                self.gear_listbox.itemconfig(tk.END, {'fg': 'green'})

    def equip_item(self):
        '''equip the selected item'''
        # Grab current selection
        selected_index = self.gear_listbox.curselection()

        # Check if there's no selection
        if not selected_index:
            tk.messagebox.showinfo("No Selection", "Please select an item to equip.")
            return
        
        # Get correct fish from the selected index
        selected_index = selected_index[0] # curselection uses a tuple, so this extracts from that tuple
        # set all other equipped items to false
        for item in self.player.gear:
            item.equipped = False
        # equip the selected item
        self.player.gear[selected_index].equipped = True

        # update gear listbox
        self.create_gear_listbox()

        # Show message confirming sale
        tk.messagebox.showinfo("Item Equipped", f"You equipped {self.player.gear[selected_index].name}")

    def view_achievements(self):
        '''open the player achievements window'''
        # Hide buttons I don't want on this page
        self.main_menu_label.pack_forget()
        self.go_fishing_button.pack_forget()
        self.shop_button.pack_forget()
        self.encyclopedia_button.pack_forget()
        self.locations_button.pack_forget()
        self.gear_button.pack_forget()
        self.achievements_button.pack_forget()
        self.help_button.pack_forget()
        self.quit_button.pack_forget()
        self.inventory_label.pack_forget()
        self.inventory_listbox.pack_forget()
        self.back_to_encyclopedia_button.pack_forget()
        self.caught_species_textbox.pack_forget()

        # Show achievement information on page
        self.back_to_main_button.pack(side="left", padx=10)
        self.achievements_label.pack(side="top", pady=10)
        self.achievements_listbox.pack(side="top", pady=10)

        #update listbox with player achievement information
        self.fill_achievements_listbox()

    def fill_achievements_listbox(self):
        '''fill the achievements listbox with player information'''

        self.achievements_listbox.delete(0, tk.END)

        for achievement in self.player.achievements:
            self.achievements_listbox.insert(tk.END, f"Achievement: {achievement.name} ---------- Description: {achievement.description}")
            if achievement.achieved == True:
                self.achievements_listbox.itemconfig(tk.END, {'fg': 'green'})
            else:
                self.achievements_listbox.itemconfig(tk.END, {'fg': 'red'} )

    def view_help(self):
        '''view the help page which displays information about the game'''
        # Hide buttons I don't want on this page
        self.main_menu_label.pack_forget()
        self.go_fishing_button.pack_forget()
        self.shop_button.pack_forget()
        self.encyclopedia_button.pack_forget()
        self.locations_button.pack_forget()
        self.gear_button.pack_forget()
        self.achievements_button.pack_forget()
        self.help_button.pack_forget()
        self.quit_button.pack_forget()
        self.inventory_label.pack_forget()
        self.inventory_listbox.pack_forget()
        self.back_to_encyclopedia_button.pack_forget()
        self.caught_species_textbox.pack_forget()
        self.level_label.pack_forget()
        self.gold_label.pack_forget()

        # Show help information on page
        self.back_to_main_button.pack(side="left", padx=10)
        self.help_textbox.pack(side="top", pady=10)

        # load the help information
        with open('help.txt', 'r', encoding='utf-8') as file:
            help_text = file.read()

        # display the help information in textbox
        self.help_textbox.config(state=tk.NORMAL)
        self.help_textbox.delete("1.0", tk.END)
        self.help_textbox.insert(tk.END, help_text)
        self.help_textbox.config(state=tk.DISABLED)


    def quit_game(self):
        self.player.pickle_dump_data()
        self.root.quit()  # Close the window
    
    def on_close(self):
        self.player.pickle_dump_data()
        self.root.quit() # closes window
    
    def update_inventory(self):
        '''update inventory'''
        self.inventory_listbox.delete(0, tk.END)
        for fish in self.player.inventory:
            self.inventory_listbox.insert(tk.END, f"{fish.species.name} ({fish.grade})")
            if fish.species.rarity == "diamond":
                self.inventory_listbox.itemconfig(tk.END, {'fg': 'cyan'})
            elif fish.species.rarity == "platinum":
                self.inventory_listbox.itemconfig(tk.END, {'fg': 'green'})
            elif fish.species.rarity == "gold":
                self.inventory_listbox.itemconfig(tk.END, {'fg': 'gold'})
            elif fish.species.rarity == "silver":
                self.inventory_listbox.itemconfig(tk.END, {'fg': 'silver'})
            elif fish.species.rarity == "bronze":
                self.inventory_listbox.itemconfig(tk.END, {'fg': 'tan'})
            elif fish.species.rarity == "copper":
                self.inventory_listbox.itemconfig(tk.END, {'fg': 'seashell'})

    def update_textbox(self, message, color='black'):
        # Enable the Text widget, insert the message, and disable it again
        self.textbox.config(state=tk.NORMAL)  # Enable the Text widget for editing
        # get insert position for colored messages
        insert_position = self.textbox.index(tk.INSERT)
        self.textbox.insert(tk.END, message + "\n")  # Insert the new message at the end
        end_position = self.textbox.index(f"{insert_position} + {len(message) + 1}c")
        self.textbox.see(tk.END)  # Automatically scroll to the bottom
        # change color of inserted text
        self.textbox.tag_add("colored", insert_position, end_position)
        self.textbox.tag_config("colored", foreground=color)
        self.textbox.config(state=tk.DISABLED)  # Disable it again so the user cannot edit it

def main():
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()