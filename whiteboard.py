import tkinter as tk
from tkinter import messagebox

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fishtown")
        # self.root.geometry("1000x600")  # Set the window size

        # Configure grid to allow resizing
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=3)
        self.root.grid_columnconfigure(0, weight=2)
        self.root.grid_columnconfigure(1, weight=1)

        # Label for Welcome Message
        self.welcome_label = tk.Label(self.root, text="Welcome to Fishtown!", font=("Arial", 24))
        self.welcome_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Label for username prompt
        self.username_label = tk.Label(self.root, text="Enter your username:")
        self.username_label.grid(row=1, column=0, padx=10, pady=10)

        # Entry field for username
        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)

        # Button to start the game (after entering the username)
        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.start_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Game Options - initially hidden
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

    def start_game(self):
        # Hide username prompt and start button
        self.username_label.grid_forget()
        self.username_entry.grid_forget()
        self.start_button.grid_forget()
        self.welcome_label.grid_forget()

        # Show game options and inventory buttons
        self.catch_fish_button.grid(row=0, column=0, padx=10, pady=10)
        self.shop_button.grid(row=1, column=0, padx=10, pady=10)
        self.encyclopedia_button.grid(row=2, column=0, padx=10, pady=10)
        self.locations_button.grid(row=3, column=0, padx=10, pady=10)
        self.gear_button.grid(row=4, column=0, padx=10, pady=10)
        self.quit_button.grid(row=5, column=0, padx=10, pady=10)

        # Inventory widgets
        self.inventory_label.grid(row=0, column=1, padx=10, pady=10)
        self.inventory_listbox.grid(row=1, column=1, padx=10, pady=10)
        # self.sell_fish_button.grid(row=2, column=1, padx=10, pady=10)

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

root = tk.Tk()
app = GameApp(root)
root.mainloop()
