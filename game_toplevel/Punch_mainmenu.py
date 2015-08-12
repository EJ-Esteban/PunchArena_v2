import tkinter as tk
from tkinter import messagebox
import os
from Punch_store import PunchArenaStore
from Punch_armory import PunchArenaArmory
from player_profile import Profile
from graphics_common import MyDialog

# need a top level reference to images to prevent garbage collection
images = dict()


class PunchArenaMenu:
    def __init__(self, tkRoot):
        self.tkRoot = tkRoot

        self.menu_frame = tk.Frame(tkRoot)
        self.menu_frame.grid(row=0, column=0)

        self.menu_canvas = tk.Canvas(self.menu_frame, bg='gray', width=600, height=550, highlightthickness=0)
        self.menu_canvas.grid(row=0, column=0)

        self.player_profile()

        global images
        cover = tk.PhotoImage(file="imgs/menu/menucover.png")
        images['cover'] = cover

        self.menu_canvas.create_image(0, 0, anchor="nw", image=cover)
        self.pop_buttons_save()
        self.active_profile = None

        self.tk_shop = None
        self.tk_armory = None
        self.tk_arena = None

        self.pop_buttons_play()

    def pop_buttons_save(self):
        """populates menu buttons"""

        tkRoot = self.tkRoot

        # lower buttons--new, save, load
        low_options = {'bg': "gray", 'anchor': 'center', 'font': "impact 22",
                       'width': 10, 'activebackground': "gray", 'relief': 'sunken'}
        low_window = {"height": 42, "width": 194, "anchor": 'nw'}

        newgame_btn = tk.Button(tkRoot, low_options, command=self.new_game)
        newgame_btn.configure(text="New Game")
        self.bind_hover1(newgame_btn)
        self.menu_canvas.create_window(3, 505, low_window, window=newgame_btn)

        loadgame_btn = tk.Button(tkRoot, low_options, command=self.load_game)
        loadgame_btn.configure(text="Load Game")
        self.bind_hover1(loadgame_btn)
        self.menu_canvas.create_window(202, 505, low_window, window=loadgame_btn)

        savegame_btn = tk.Button(tkRoot, low_options, command=self.save_game)
        savegame_btn.configure(text="Save Game")
        self.bind_hover1(savegame_btn)
        self.menu_canvas.create_window(401, 505, low_window, window=savegame_btn)

    def bind_hover1(self, button):
        button.bind("<Enter>", lambda event, h=button: h.configure(bg="light gray"))
        button.bind("<Leave>", lambda event, h=button: h.configure(bg="gray"))

    def bind_hover2(self, button):
        button.bind("<Enter>", lambda event, h=button: h.configure(bg="white"))
        button.bind("<Leave>", lambda event, h=button: h.configure(bg="light slate gray"))

    def player_profile(self):
        """loads right bar, showign current player"""

        canvas = self.menu_canvas
        canvas.create_rectangle(0, 0, 440, 550, fill="slate gray", width=2)

        canvas.create_rectangle(440, 0, 600, 172, fill="dark gray", width=2)
        canvas.create_rectangle(440, 172, 600, 267, fill="light gray", width=2)
        canvas.create_rectangle(440, 267, 600, 550, fill="dark gray", width=2)
        canvas.create_rectangle(440, 0, 600, 34, fill="white", width=2, tag='p_color')
        # player name
        canvas.create_text(518, 8, text="Player", font="helvetica 14 italic",
                           fill='black', disabledfill='gray', tag='p_name',
                           anchor="n", state="disabled", width=150)
        global images
        # player sprite background
        images['sprite_bg'] = tk.PhotoImage(file="imgs/map/tile_floor0.gif")
        canvas.create_image(518, 63, anchor="center", image=images['sprite_bg'])
        canvas.create_image(518, 63, anchor="center", image=images['sprite_bg'], tag="player_sprite")

        # player stats:

        leftcol = {'font': "helvetica 10", 'anchor': 'e', 'fill': 'black'}
        canvas.create_text(530, 102, leftcol, text="Max HP:")
        canvas.create_text(530, 117, leftcol, text="Max MP:")
        canvas.create_text(530, 132, leftcol, text="Max Move:")
        canvas.create_text(530, 147, leftcol, text="Base Dmg:")
        canvas.create_text(530, 162, leftcol, text="Bloodlust:")

        rightcol = {'font': "helvetica 10", 'anchor': 'w', 'disabledfill': 'gray', 'state': 'disabled', 'text': '--'}
        canvas.create_text(533, 102, rightcol, fill='red', tag='p_hp')
        canvas.create_text(533, 117, rightcol, fill='blue', tag='p_mp')
        canvas.create_text(533, 133, rightcol, fill='green', tag='p_move')
        canvas.create_text(533, 147, rightcol, fill='goldenrod', tag='p_dmg')
        canvas.create_text(533, 162, rightcol, fill='dark red', tag='p_bl')

        # player net worth stats
        canvas.create_text(530, 181, leftcol, text="Punch Dollars:")
        canvas.create_text(530, 196, leftcol, text="Eff. Net Worth:")
        canvas.create_text(530, 211, leftcol, text="Red CC:")
        canvas.create_text(530, 226, leftcol, text="Blue CC:")
        canvas.create_text(530, 241, leftcol, text="Green CC:")
        canvas.create_text(530, 256, leftcol, text="Yellow CC:")

        canvas.create_text(533, 181, rightcol, fill='black', tag='p_pdollars')
        canvas.create_text(533, 196, rightcol, fill='black', tag='p_networth')
        canvas.create_text(533, 211, rightcol, fill='red', tag='p_red')
        canvas.create_text(533, 226, rightcol, fill='blue', tag='p_blue')
        canvas.create_text(533, 241, rightcol, fill='green', tag='p_green')
        canvas.create_text(533, 256, rightcol, fill='goldenrod', tag='p_yellow')

        # moves equipped
        canvas.create_text(447, 277, {'font': "helvetica 12", 'anchor': 'w', 'fill': 'black', 'text': "Equipped:"})

        images['button cover'] = tk.PhotoImage(file="imgs/statbar/buttoncover.gif")
        images['error'] = tk.PhotoImage(file="imgs/statbar/errorblock.gif")

        for x in [0, 1, 2, 3]:
            canvas.create_image(460, 287 + x * 53, anchor="nw", image=images['error'], tag="p_" + str(x * 2))
            canvas.create_image(460, 287 + x * 53, anchor="nw", image=images['button cover'])

        for x in [0, 1, 2, 3]:
            canvas.create_image(528, 287 + x * 53, anchor="nw", image=images['error'], tag="p_" + str(x * 2 + 1))
            canvas.create_image(528, 287 + x * 53, anchor="nw", image=images['button cover'])

    def update_profile(self):
        profile = self.active_profile
        canvas = self.menu_canvas

        # change name
        canvas.itemconfig('p_name', state="normal")
        canvas.itemconfig('p_name', text=profile.name)
        # tally color credits and attempt to color the player the most appropriate color
        cc = profile.color_credits
        col = "white"
        if cc[0] == cc[1] == cc[2] == cc[3]:
            pass
        else:
            j = cc.index(max(cc))
            if j is 0:
                col = "red"
            elif j is 1:
                col = "blue"
            elif j is 2:
                col = "green"
            elif j is 3:
                col = "goldenrod"
        canvas.itemconfig('p_color', fill=col)

        # tiny avatar thing
        global images
        i = tk.PhotoImage(file="imgs/sprites/%sS.gif" % self.active_profile.sprite)
        images['sprite_fg'] = i
        canvas.itemconfig("player_sprite", image=i)

        canvas.itemconfig("p_hp", state='normal', text=str(profile.max_hp))
        canvas.itemconfig("p_mp", state='normal', text=str(profile.max_mp))
        canvas.itemconfig("p_move", state='normal', text=str(profile.max_move))
        canvas.itemconfig("p_dmg", state='normal', text=str(profile.base_damage))
        canvas.itemconfig("p_bl", state='normal', text=str(profile.blood_in) + "/" + str(profile.blood_out))

        canvas.itemconfig("p_pdollars", state='normal', text=str(profile.punch_dollars))
        canvas.itemconfig("p_networth", state='normal', text=str(profile.effective_net_worth))
        canvas.itemconfig("p_red", state='normal', text=str(cc[0]))
        canvas.itemconfig("p_blue", state='normal', text=str(cc[1]))
        canvas.itemconfig("p_green", state='normal', text=str(cc[2]))
        canvas.itemconfig("p_yellow", state='normal', text=str(cc[3]))

        for x in range(8):
            move = profile.equipped_abilties[x]
            if move == 'none':
                canvas.itemconfig("p_%d" % x, image=images['error'])
            else:
                images['icon_%d' % x] = tk.PhotoImage(file="imgs/statbar/%sbutton.gif" % move)
                canvas.itemconfig("p_%d" % x, image=images['icon_%d' % x])

    def pop_buttons_play(self):
        tkRoot = self.tkRoot
        canvas = self.menu_canvas

        global images
        images['diamond'] = tk.PhotoImage(file="imgs/diamondfilled.png")

        canvas.create_image(20, 30, anchor='nw', image=images['diamond'])

        canvas.create_text(100, 30, anchor='nw', text="PUNCH ARENA", font='impact 40')
        play_options = {'bg': "light slate gray", 'anchor': 'center', 'font': "Helvetica 30",
                        'width': 10, 'activebackground': "gray", 'relief': 'raised'}
        play_window = {"height": 70, "width": 418, "anchor": 'nw'}

        arena_btn = tk.Button(tkRoot, play_options, command=self.arena_fight)
        arena_btn.configure(text="Arena")
        self.bind_hover2(arena_btn)
        self.menu_canvas.create_window(12, 125, play_window, window=arena_btn)

        armory_btn = tk.Button(tkRoot, play_options, command=self.armory)
        armory_btn.configure(text="Armory")
        self.bind_hover2(armory_btn)
        self.menu_canvas.create_window(12, 200, play_window, window=armory_btn)

        shop_btn = tk.Button(tkRoot, play_options, command=self.shop)
        shop_btn.configure(text="Shop")
        self.bind_hover2(shop_btn)
        self.menu_canvas.create_window(12, 275, play_window, window=shop_btn)

        options_btn = tk.Button(tkRoot, play_options, command=self.options)
        options_btn.configure(text="Options")
        self.bind_hover2(options_btn)
        self.menu_canvas.create_window(12, 350, play_window, window=options_btn)

    def new_game(self):
        if self.active_profile is not None:
            a = messagebox.askyesnocancel(
                "Game is loaded",
                "Do you wish to save your current game?",
            )
            if a is None:
                return
            elif a is True:
                self.save_game()
        MyDialog(self.tkRoot, "What if your fighter's name?", self, "create_player")

    def create_player(self, name):
        if name == "":
            name = "Aria"
        self.active_profile = Profile(name)
        self.update_profile()
        if self.tk_shop is not None:
            self.tk_shop.redraw_player()

    def save_game(self):
        if self.active_profile is None:
            messagebox.showwarning(
                "No player loaded",
                "Nothing to save!."
            )
            return
        name = self.active_profile.name
        name = name.replace(' ', '_')
        if os.path.isfile("save/%s.txt" % name):
            a = messagebox.askyesno(
                "File already exists",
                "Overwrite file?",
            )
            if a is False:
                return
        self.active_profile.save_player()

    def load_game(self):
        if self.active_profile is not None:
            a = messagebox.askyesnocancel(
                "Game is loaded",
                "Do you wish to save your current game?",
            )
            if a is None:
                return
            elif a is True:
                self.save_game()
        MyDialog(self.tkRoot, "What if your fighter's name?", self, "recreate_player")

    def recreate_player(self, name):
        if name == "":
            name = "aria"
        name = name.replace(' ', '_')
        if not os.path.isfile("save/%s.txt" % name):
            messagebox.showwarning(
                "Invalid name",
                "Couldn't find that player's save."
            )
            return

        self.active_profile = Profile()
        self.active_profile.load_player(name)
        self.update_profile()

        if self.tk_shop is not None:
            self.tk_shop.redraw_player()



    def armory(self):
        if self.active_profile is None:
            messagebox.showwarning(
                "No player loaded",
                "Load a player or start a new\ngame to use the armory."
            )
        if self.tk_armory is None:
            self.tk_armory = PunchArenaArmory(self)
        else:
            self.menu_frame.grid_forget()
            self.tk_armory.armory_frame.grid(row=0, column=0)

    def arena_fight(self):
        if self.active_profile is None:
            messagebox.showwarning(
                "No player loaded",
                "Load a player or start a new\ngame to fight in the arena."
            )
            return

    def shop(self):
        if self.active_profile is None:
            messagebox.showwarning(
                "No player loaded",
                "Load a player or start a new\ngame to use the shop."
            )
            return
        if self.tk_shop is None:
            self.tk_shop = PunchArenaStore(self)
        else:
            self.menu_frame.grid_forget()
            self.tk_shop.shop_frame.grid(row=0, column=0)
            self.tk_shop.update_profile()

    def options(self):
        pass
