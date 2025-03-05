# Welcome to Fishtown :)
# main.py - core gameplay loop

import random
from fish import Species, Fish
from player import Player
import tkinter as tk
from tkinter import messagebox
from locations import Location

def get_species():
    '''create the species list'''

    species_list = [
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
    
class GameApp:
    def __init__(self, root):

        # Game info
        self.species_list = get_species()
        

        # Root tkinter stuff
        self.root = root
        self.root.title("Fishtown")
        # self.root.geometry("1000x600")  # Set the window size - removed because the auto-sizing has been nicer so far.

        # game icon
        root.iconbitmap("images/icon.ico") 

        # Bind the window close (X button) to a custom method
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Placeholder for player instance (initially None)
        self.player = None

        # Label for Welcome Message
        self.welcome_label = tk.Label(self.root, text="Welcome to Fishtown!", font=("Arial", 24))
        self.welcome_label.pack(side="top", pady=10)

        # Label for username prompt
        self.username_label = tk.Label(self.root, text="Enter your username:")
        self.username_label.pack(side="top", pady=10)

        # Entry field for username
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(side="top", pady=10)

        # Game Options - initially hidden
        self.main_menu_label = tk.Label(self.root, text = "Welcome to Fishtown!", font=("Arial", 20))
        self.go_fishing_button = tk.Button(self.root, 
                                   text="Go Fishing", 
                                   command=lambda: self.go_fishing(self.species_list, self.player)) # lambda means this function isn't called immediately.
        self.shop_button = tk.Button(self.root, text="Shop", command=self.go_shopping)
        self.encyclopedia_button = tk.Button(self.root, text="Encyclopedia", command=self.view_encyclopedia)
        self.locations_button = tk.Button(self.root, text="Locations", command=self.view_locations)
        self.gear_button = tk.Button(self.root, text="Gear", command=self.view_gear)
        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit_game)

        # Button to start the game (after entering the username)
        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.start_button.pack(side="top", pady=10)

        # Fishing page options
        self.catch_fish_button = tk.Button(self.root, 
                                   text="Catch Fish!", 
                                   command=lambda: self.catch_fish(self.species_list,self.player)) # lambda means this function isn't called immediately.
        self.back_to_main_button = tk.Button(self.root,text="Main Menu", command=self.show_main_menu)

        # Create a Text widget for logging actions
        self.textbox = tk.Text(self.root, height=5, width=120, wrap=tk.WORD, state=tk.DISABLED, font=("Arial", 10))

        # Shopping page buttons
        self.sell_1_fish_button = tk.Button(self.root, text="Sell One", command=self.sell_one)
        self.sell_all_fish_button = tk.Button(self.root, text="Sell All", command=self.sell_all)

        # Encyclopedia page buttons and options
        self.caught_species_button = tk.Button(self.root, text="View Caught Species", command=self.caught_species)
        self.caught_species_textbox = tk.Text(self.root, height=10, width=50, font=("Arial",10))

        # Caught Species Page options
        self.back_to_encyclopedia_button = tk.Button(self.root, text="Back to Encyclopedia", command=self.view_encyclopedia)

        # Location Page Options


        # Inventory buttons - initially hidden
        self.inventory_label = tk.Label(self.root, text="Inventory", font=("Arial", 14))
        self.inventory_listbox = tk.Listbox(self.root, height=16, width=30, font=("Arial", 10))

        # Player Gold Image - initially hidden
        self.gold_image = tk.PhotoImage(file = "images/gold32x32.png")
        

    def start_game(self):

        # Get username data 
        username = self.username_entry.get()

        # Check if the username is not empty
        if username.strip() == "":
            # Display an error if username is empty
            messagebox.showerror("Input Error", "Please enter a valid username.")
            return
        
        '''# Check if the username already exists
        if username in player_data:
            # Load existing player data
            self.player = player_data[username]
            messagebox.showinfo("Welcome Back", f"Welcome back, {self.player.username}!")
        else:'''
        # Create a new player instance with the username
        self.player = Player(username)
        # player_data = {}
        # player_data[username] = self.player  # Save the new player data
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
        self.quit_button.pack(side="left", padx=10)

        # Inventory widgets
        self.inventory_label.pack(side="top", pady=10)
        self.inventory_listbox.pack(side="top", pady=10)
        self.update_inventory()

        # Player gold display
        self.gold_label = tk.Label(self.root, text=f"{self.player.gold}", font=("Arial", 10), image=self.gold_image, compound='top')
        self.gold_label.pack(side="right", padx=10)

    def show_main_menu(self):
        '''show main menu. Often used in the return to main menu buttons.'''

        # Backup player data whenever main menu is accessed.
        self.player.pickle_dump_data()

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
        # including location unlocks
        if self.location_buttons != []:
            for location_button in self.location_buttons:
                location_button.pack_forget()

        # Show game buttons
        self.main_menu_label.pack(side="top", pady=10)
        self.go_fishing_button.pack(side="left", padx=10)
        self.shop_button.pack(side="left", padx=10)
        self.encyclopedia_button.pack(side="left", padx=10)
        self.locations_button.pack(side="left", padx=10)
        self.gear_button.pack(side="left", padx=10)
        self.quit_button.pack(side="left", padx=10)

        # Inventory widgets
        self.inventory_label.pack(side="top", pady=10)
        self.inventory_listbox.pack(side="top", pady=10)
        self.update_inventory()

        # Player gold display
        self.gold_label.pack(side="right", padx=10)
    
    def go_fishing(self,species_list,player):
        '''fishing loop'''

        # Hide buttons I don't want on this page
        self.main_menu_label.pack_forget()
        self.go_fishing_button.pack_forget()
        self.shop_button.pack_forget()
        self.encyclopedia_button.pack_forget()
        self.locations_button.pack_forget()
        self.gear_button.pack_forget()
        self.quit_button.pack_forget()

        # Show the fishing options on the page
        self.catch_fish_button.pack(side="left", padx=10)
        self.back_to_main_button.pack(side="left", padx=10)
        self.textbox.pack(side=tk.BOTTOM, fill=tk.X)

        '''# Create a scrollbar widget
        scrollbar = tk.Scrollbar(self.root, command=self.textbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Link the scrollbar to the text widget
        self.textbox.config(yscrollcommand=scrollbar.set)'''

    def catch_fish(self,species_list,player):
        '''catch a fish, uses the button defined above'''
        weights = [species.rarity_weight for species in species_list]
        fish_species = random.choices(species_list, weights=weights, k=1)[0]
        if len(player.inventory) < 16:
            fish = Fish(fish_species)
            self.update_textbox(f"You have caught a {fish}.")
            player.caught_species[fish_species.name] = True
            player.caught_fish.append(fish)
            player.inventory.append(fish)
            self.update_inventory()
        else: 
            messagebox.showinfo("Inventory full", "Your inventory is full. Sell your fish!")

    def go_shopping(self):
        '''shopping loop'''

        # Hide buttons I don't want on this page
        self.main_menu_label.pack_forget()
        self.go_fishing_button.pack_forget()
        self.shop_button.pack_forget()
        self.encyclopedia_button.pack_forget()
        self.locations_button.pack_forget()
        self.gear_button.pack_forget()
        self.quit_button.pack_forget()

        # Show shopping options on the page
        self.sell_1_fish_button.pack(side = "left", padx=10)
        self.sell_all_fish_button.pack(side = "left", padx=10)
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
        # update gold label
        self.gold_label.config(text=f"{self.player.gold}")

        # Update inventory display
        self.update_inventory()

        # Show message confirming sale
        tk.messagebox.showinfo("Fish Sold", f"You sold a {sold_fish.grade} {sold_fish.species.name} for {sold_fish.sell_price} gold.")

    def sell_all(self):
        '''sell all fish in inventory'''

        total_value = 0
        for fish in self.player.inventory[:]: # slice is needed so that we don't skip fish to sell. 
            total_value += fish.sell_price
            self.player.inventory.remove(fish)
        self.player.gold += total_value

        # Show message confirming sale
        tk.messagebox.showinfo("Fish Sold", f"You have sold all of the fish in your inventory for {total_value} gold.")

        # update gold label
        self.gold_label.config(text=f"{self.player.gold}")

        # Update the inventory at the end            
        self.update_inventory()

    def view_encyclopedia(self):
        '''encyclopedia options'''

        # Hide buttons I don't want on this page
        self.main_menu_label.pack_forget()
        self.go_fishing_button.pack_forget()
        self.shop_button.pack_forget()
        self.encyclopedia_button.pack_forget()
        self.locations_button.pack_forget()
        self.gear_button.pack_forget()
        self.quit_button.pack_forget()
        self.inventory_label.pack_forget()
        self.inventory_listbox.pack_forget()
        self.back_to_encyclopedia_button.pack_forget()
        self.caught_species_textbox.pack_forget()
        self.gold_label.pack_forget()

        # Set up buttons on main encylopedia page
        self.caught_species_button.pack(side="left", padx=10)
        self.back_to_main_button.pack(side="left", padx=10)

    def caught_species(self):
        '''display the list of caught species'''

        # Hide the caught species button from the encyclopedia page
        self.caught_species_button.pack_forget()
        self.back_to_main_button.pack_forget()

        # Display the textbox
        self.caught_species_textbox.pack()
        self.caught_species_textbox.delete(1.0,tk.END) # clear any previous content
        for species, value in self.player.caught_species.items():
            self.caught_species_textbox.insert(tk.END, f"{species}: {value}\n")

        # Display back to encyclopedia button
        self.back_to_encyclopedia_button.pack()

    def view_locations(self):
        '''location options'''

        # Hide buttons I don't want on this page
        self.main_menu_label.pack_forget()
        self.go_fishing_button.pack_forget()
        self.shop_button.pack_forget()
        self.encyclopedia_button.pack_forget()
        self.locations_button.pack_forget()
        self.gear_button.pack_forget()
        self.quit_button.pack_forget()
        self.inventory_label.pack_forget()
        self.inventory_listbox.pack_forget()
        self.back_to_encyclopedia_button.pack_forget()
        self.caught_species_textbox.pack_forget()

        # Set up buttons to show on this page
        self.back_to_main_button.pack(side="left", padx=10)

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

        else: 
            # unlock location if enough gold
            if self.player.gold >= location.unlock_price:
                self.player.gold -= location.unlock_price
                location.unlocked = True
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
        print("You chose to view gear!")

    def quit_game(self):
        print("Quitting the game...")
        self.player.pickle_dump_data()
        self.root.quit()  # Close the window
    
    def on_close(self):
        self.player.pickle_dump_data()
        self.root.quit() # closes window
    
    def update_inventory(self):
        '''update inventory'''
        self.inventory_listbox.delete(0, tk.END)
        for fish in self.player.inventory:
            self.inventory_listbox.insert(tk.END, f"{fish.grade} {fish.species.name}")  # Make sure Fish class has __str__ defined
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

    def update_textbox(self, message):
        # Enable the Text widget, insert the message, and disable it again
        self.textbox.config(state=tk.NORMAL)  # Enable the Text widget for editing
        self.textbox.insert(tk.END, message + "\n")  # Insert the new message at the end
        self.textbox.see(tk.END)  # Automatically scroll to the bottom
        self.textbox.config(state=tk.DISABLED)  # Disable it again so the user cannot edit it

def main():
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()