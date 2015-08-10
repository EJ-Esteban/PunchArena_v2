import tkinter as tk

# need a top level reference to cover to prevent garbage collection
cover= None

class PunchArenaMenu:
    def __init__(self,tkRoot):
        self.menu_canvas = tk.Canvas(tkRoot, bg='gray', width=600, height=550, highlightthickness=0)
        self.menu_canvas.grid(row = 0, column = 0)

        global cover
        cover = tk.PhotoImage(file="imgs/menucover.png")

        self.menu_canvas.create_image(0, 0, anchor="nw", image=cover)
        self.pop_buttons(tkRoot)

        self.active_profile = None



    def pop_buttons(self, tkRoot):
        """populates menu buttons"""

        #lower buttons--new, save, load
        low_options = {'bg': "gray", 'anchor': 'center', 'font' : "impact 25",
                   'width' : 10, 'activebackground' : "gray", 'relief' : 'sunken'}
        low_window = {"height" : 66, "width" : 195, "anchor": 'nw'}

        newgame_btn = tk.Button(tkRoot,low_options )
        newgame_btn.configure(text = "NEW GAME")
        self.bind_hover(newgame_btn)
        self.menu_canvas.create_window(4, 475,  low_window, window=newgame_btn)

        loadgame_btn = tk.Button(tkRoot,low_options )
        loadgame_btn.configure(text = "LOAD GAME")
        self.bind_hover(loadgame_btn)
        self.menu_canvas.create_window(202, 475,  low_window, window=loadgame_btn)

        savegame_btn = tk.Button(tkRoot,low_options)
        savegame_btn.configure(text = "SAVE GAME")
        self.bind_hover(savegame_btn)
        self.menu_canvas.create_window(400, 475,  low_window, window=savegame_btn)

    def bind_hover(self, button):
        button.bind("<Enter>", lambda event, h=button: h.configure(bg="light gray"))
        button.bind("<Leave>", lambda event, h=button: h.configure(bg="gray"))


