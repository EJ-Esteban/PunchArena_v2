import tkinter as tk
from player_profile import Profile

# need a top level reference to images to prevent garbage collection
images = dict()


class PunchArenaStore:
    def __init__(self, main_menu):
        tkRoot = self.tkRoot = main_menu.tkRoot
        self.main_menu = main_menu

        self.armory_canvas = tk.Canvas(tkRoot, bg='gray', width=600, height=550, highlightthickness=0)
        self.armory_canvas.grid(row=0, column=0)

        self.active_profile = main_menu.active_profile

        global images
        images['cover'] = tk.PhotoImage(file="imgs/menu/menucover.png")
        self.armory_canvas.create_image(0, 0, anchor="nw", image=images['cover'])

        self.armory_canvas.lift(self.main_menu.menu_canvas)

        self.frame1 = tk.Frame(tkRoot)
        self.armory_canvas.create_window(10, 10, anchor="nw", height=200, width=300, window=self.frame1)

        self.moves_canvas = tk.Canvas(self.frame1, bg="red", height=200, width=300)
