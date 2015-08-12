import tkinter as tk
from player_profile import Profile

# need a top level reference to images to prevent garbage collection
images = dict()


class PunchArenaArmory:
    def __init__(self, main_menu):
        tkRoot = self.tkRoot = main_menu.tkRoot
        self.main_menu = main_menu
        self.main_menu.menu_frame.grid_forget()

        self.armory_frame = tk.Frame(tkRoot, bg='pink', width=600, height=550, highlightthickness=0)
        self.armory_frame.grid(row=0, column=0)

        self.armory_canvas = tk.Canvas(self.armory_frame, bg='pink', width=600, height=550, highlightthickness=0)
        self.armory_canvas.grid(row=0, column=0)

        a = tk.Button(tkRoot, command=self.show_menu)
        a.configure(text=" < Menu")
        self.armory_canvas.create_window(0, 0, width=100, anchor='nw', window=a, height=50)

        b = tk.Button(tkRoot, command=self.show_shop)
        b.configure(text=" < Shop")
        self.armory_canvas.create_window(0, 50, width=100, anchor='nw', window=b, height=50)

    def show_menu(self):
        self.armory_frame.grid_forget()
        self.main_menu.menu_frame.grid(row=0, column=0)

    def show_shop(self):
        self.armory_frame.grid_forget()
        self.main_menu.shop()
