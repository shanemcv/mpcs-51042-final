# Whiteboard pack - testing pack layout

import tkinter as tk
from tkinter import messagebox
from player import Player

player_data = {}

class GameApp:
    def __init__(self, root):

        # Root stuff
        self.root = root
        self.root.title("Fishtown")
        # self.root.geometry("1000x600")  # Set the window size - removed because the auto-sizing has been nicer so far. 

        # Label for Welcome Message
        self.welcome_label = tk.Label(self.root, text="Welcome to Fishtown!", font=("Arial", 24))
        self.welcome_label.pack(side="top", pady=10)

        # Label for username prompt
        self.username_label = tk.Label(self.root, text="Enter your username:")
        self.username_label.pack(side="top", pady=10)

        # Entry field for username
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(side="top", pady=10)

        # Button to start the game (after entering the username)
        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.start_button.pack(side="top", pady=10)

        # Game Options - initially hidden
        self.main_menu_label = tk.Label(self.root, text = "Welcome to Fishtown!", font=("Arial", 20))
        self.catch_fish_button = tk.Button(self.root, text="Go Fishing", command=self.go_fishing)
        self.shop_button = tk.Button(self.root, text="Shop", command=self.go_shopping)
        self.encyclopedia_button = tk.Button(self.root, text="Encyclopedia", command=self.view_encyclopedia)
        self.locations_button = tk.Button(self.root, text="Locations", command=self.view_locations)
        self.gear_button = tk.Button(self.root, text="Gear", command=self.view_gear)
        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit_game)

        # Inventory and Sell Fish buttons - initially hidden
        self.inventory_label = tk.Label(self.root, text="Fish Inventory")
        self.inventory_listbox = tk.Listbox(self.root, height=17, width=70)
        # self.sell_fish_button = tk.Button(self.root, text="Sell Fish", command=self.sell_fish)

        # Placeholder for player instance (initially None)
        self.player = None

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
        player_data[username] = self.player  # Save the new player data
        messagebox.showinfo("Welcome", f"Welcome, {self.player.username}!")

        # Hide username prompt and start button
        self.username_label.pack_forget()
        self.username_entry.pack_forget()
        self.start_button.pack_forget()
        self.welcome_label.pack_forget()

        # Show game options and inventory buttons
        self.main_menu_label.pack(side="top", pady=10)
        self.catch_fish_button.pack(side="left", padx=10)
        self.shop_button.pack(side="left", padx=10)
        self.encyclopedia_button.pack(side="left", padx=10)
        self.locations_button.pack(side="left", padx=10)
        self.gear_button.pack(side="left", padx=10)
        self.quit_button.pack(side="left", padx=10)

        # Inventory widgets
        self.inventory_label.pack(side="top", pady=10)
        self.inventory_listbox.pack(side="top", pady=10)
        # self.sell_fish_button.pack(side="top", pady=10)

    def go_fishing(self):
        print("You chose to go fishing!")

    def go_shopping(self):
        print("You chose to go shopping!")

    def view_encyclopedia(self):
        print("You chose to view the encyclopedia!")

    def view_locations(self):
        print("You chose to view locations!")

    def view_gear(self):
        print("You chose to view gear!")

    def quit_game(self):
        print("Quitting the game...")
        self.root.quit()  # Close the window


def main():
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
