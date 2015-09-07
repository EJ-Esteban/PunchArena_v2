import tkinter as tk
import moves
from player_profile import Profile

# need a top level reference to images to prevent garbage collection
images = dict()
armory_moves = dict()


class PunchArenaArmory:
    def __init__(self, main_menu):
        tkRoot = self.tkRoot = main_menu.tkRoot
        self.main_menu = main_menu
        self.main_menu.menu_frame.grid_forget()

        self.armory_frame = tk.Frame(tkRoot, bg='pink', width=600, height=550, highlightthickness=0)
        self.armory_frame.grid(row=0, column=0)

        self.make_drawing_area()
        self.pop_buttons_save()
        self.pop_info()
        self.pop_profile()
        self.pop_moves()
        self.repaint_moves()

    def make_drawing_area(self):
        global images
        self.c_canvas = [None] * 5
        self.c_canvas[0] = tk.Canvas(self.armory_frame, bg='red', width=600, height=6, highlightthickness=0)
        images['canvas0'] = tk.PhotoImage(file='imgs/menu/shopcover01.png')
        self.c_canvas[0].create_image(0, 0, image=images['canvas0'], anchor="nw")
        self.c_canvas[0].grid(row=0, column=0, columnspan=3)
        self.c_canvas[1] = tk.Canvas(self.armory_frame, bg='yellow', width=6, height=493, highlightthickness=0)
        images['canvas1'] = tk.PhotoImage(file='imgs/menu/shopcover02.png')
        self.c_canvas[1].create_image(0, 0, image=images['canvas1'], anchor="nw")
        self.c_canvas[1].grid(row=1, column=0, rowspan=3)
        self.c_canvas[2] = tk.Canvas(self.armory_frame, bg='blue', width=431, height=7, highlightthickness=0)
        images['canvas2'] = tk.PhotoImage(file='imgs/menu/shopcover03.png')
        self.c_canvas[2].create_image(0, 0, image=images['canvas2'], anchor="nw")
        self.c_canvas[2].grid(row=2, column=1)
        self.c_canvas[3] = tk.Canvas(self.armory_frame, bg='green', width=163, height=493, highlightthickness=0)
        images['canvas3'] = tk.PhotoImage(file='imgs/menu/shopcover04.png')
        self.c_canvas[3].create_image(0, 0, image=images['canvas3'], anchor="nw", tag="cover")
        self.c_canvas[3].grid(row=1, column=2, rowspan=3)
        self.c_canvas[4] = tk.Canvas(self.armory_frame, bg='orange', width=600, height=51, highlightthickness=0)
        images['canvas4'] = tk.PhotoImage(file='imgs/menu/shopcover05.png')
        self.c_canvas[4].create_image(0, 0, image=images['canvas4'], anchor="nw")
        self.c_canvas[4].grid(row=4, column=0, columnspan=3)
        self.moves_frame = tk.Frame(self.armory_frame, bg='light blue', width=431, height=337, highlightthickness=0)
        self.moves_frame.grid(row=1, column=1)
        self.info_canvas = tk.Canvas(self.armory_frame, bg='light green', width=431, height=149, highlightthickness=0)
        self.info_canvas.grid(row=3, column=1)

    def pop_buttons_save(self):
        """populates menu buttons"""

        tkRoot = self.tkRoot
        canvas = self.c_canvas[4]

        # lower buttons--new, save, load
        low_options = {'bg': "gray", 'anchor': 'center', 'font': "impact 22",
                       'width': 10, 'activebackground': "gray", 'relief': 'sunken'}
        low_window = {"height": 42, "width": 194, "anchor": 'nw'}

        newgame_btn = tk.Button(tkRoot, low_options, command=self.main_menu.new_game)
        newgame_btn.configure(text="New Game")
        self.bind_hover1(newgame_btn)
        canvas.create_window(3, 6, low_window, window=newgame_btn)

        loadgame_btn = tk.Button(tkRoot, low_options, command=self.main_menu.load_game)
        loadgame_btn.configure(text="Load Game")
        self.bind_hover1(loadgame_btn)
        canvas.create_window(202, 6, low_window, window=loadgame_btn)

        savegame_btn = tk.Button(tkRoot, low_options, command=self.main_menu.save_game)
        savegame_btn.configure(text="Save Game")
        self.bind_hover1(savegame_btn)
        canvas.create_window(401, 6, low_window, window=savegame_btn)

    def bind_hover1(self, button):
        button.bind("<Enter>", lambda event, h=button: h.configure(bg="light gray"))
        button.bind("<Leave>", lambda event, h=button: h.configure(bg="gray"))

    def unbind_hover1(self, button):
        button.configure(state="normal", bg="gray")
        button.unbind("<Enter>")
        button.unbind("<Leave>")
        button.configure(state="disabled")

    def pop_info(self):
        """populates info area"""
        tkRoot = self.tkRoot
        canvas = self.info_canvas

        btn_options = {'bg': "gray", 'anchor': 'center', 'font': "impact 12",
                       'width': 10, 'activebackground': "gray", 'relief': 'raised'}

        info_sign = tk.Button(tkRoot, btn_options, state='disabled', anchor="e")
        info_sign.configure(text="Info:  ", disabledforeground="black", font="impact 22")
        canvas.create_window(0, 0, width=100, anchor='nw', window=info_sign, height=50)

        menu_btn = tk.Button(tkRoot, btn_options, command=self.show_menu)
        menu_btn.configure(text="Menu")
        self.bind_hover1(menu_btn)
        canvas.create_window(0, 99, width=75, anchor='nw', window=menu_btn, height=50)

        shop_btn = tk.Button(tkRoot, btn_options, command=self.show_shop)
        shop_btn.configure(text="Shop")
        self.bind_hover1(shop_btn)
        canvas.create_window(75, 99, width=75, anchor='nw', window=shop_btn, height=50)

        self.buy_btn = tk.Button(tkRoot, btn_options)
        self.buy_btn.configure(text="Equip  ", font="impact 22", anchor="e", state="disabled")
        canvas.create_window(0, 50, width=150, anchor='nw', window=self.buy_btn, height=49)

        global images
        images['info_under'] = tk.PhotoImage(file="imgs/statbar/blankTile.png")
        images['info_over'] = tk.PhotoImage(file="imgs/statbar/IconCover.png")

        canvas.create_image(100, 0, image=images['info_under'], anchor='nw', tag='info_icon')
        canvas.create_image(100, 0, image=images['info_over'], anchor='nw')

        self.info = tk.Text(self.armory_frame, bg="dim gray", font="helvetica 10", wrap="word", foreground="white",
                            bd=2, padx=3, pady=3)
        canvas.create_window(150, 0, width=265, height=149, anchor='nw', window=self.info)

        scroll = tk.Scrollbar(self.armory_frame)
        self.info.configure(yscrollcommand=scroll.set, state="disabled")
        scroll.config(command=self.info.yview)
        scroll.grid(row=0, column=1, sticky="NSEW")
        canvas.create_window(414, 0, width=17, height=149, anchor='nw', window=scroll)

        self.info.tag_configure('title', font="helvetica 12 bold")
        self.info.tag_configure('tiny', font="helvetica 8 italic")
        self.info.tag_configure('small', font="helvetica 9 italic")

        self.info.tag_configure('red', foreground="red")
        self.info.tag_configure('blue', foreground="blue")
        self.info.tag_configure('green', foreground="lime green")
        self.info.tag_configure('yellow', foreground="yellow")

        self.info.tag_configure('tinyred', foreground="red", font="helvetica 8 italic")
        self.info.tag_configure('tinyblue', foreground="blue", font="helvetica 8 italic")
        self.info.tag_configure('tinygreen', foreground="lime green", font="helvetica 8 italic")
        self.info.tag_configure('tinyyellow', foreground="yellow", font="helvetica 8 italic")

    def pop_profile(self):
        canvas = self.c_canvas[3]
        canvas.create_rectangle(0, -6, 160, 172, fill="dark gray", width=2)
        canvas.create_rectangle(0, 166, 160, 267, fill="light gray", width=2)
        canvas.create_rectangle(0, 261, 160, 550, fill="dark gray", width=2)
        canvas.create_rectangle(0, -6, 160, 28, fill="white", width=2, tag='p_color')
        canvas.tag_raise("cover")

        canvas.create_text(81, 2, text="Player", font="helvetica 14 italic",
                           fill='black', disabledfill='gray', tag='p_name',
                           anchor="n", state="disabled", width=150)

        global images
        # player sprite background
        images['sprite_bg'] = tk.PhotoImage(file="imgs/map/tile_floor0.gif")
        canvas.create_image(81, 57, anchor="center", image=images['sprite_bg'])
        canvas.create_image(81, 57, anchor="center", image=images['sprite_bg'], tag="player_sprite")

        leftcol = {'font': "helvetica 10", 'anchor': 'e', 'fill': 'black'}
        canvas.create_text(93, 96, leftcol, text="Max HP:")
        canvas.create_text(93, 111, leftcol, text="Max MP:")
        canvas.create_text(93, 126, leftcol, text="Max Move:")
        canvas.create_text(93, 141, leftcol, text="Base Dmg:")
        canvas.create_text(93, 156, leftcol, text="Bloodlust:")

        canvas.create_text(93, 175, leftcol, text="Trait:")
        canvas.create_text(93, 190, leftcol, text="Trait:")
        canvas.create_text(93, 205, leftcol, text="Passives:")
        canvas.create_text(93, 220, leftcol, text="True Passives:")
        canvas.create_text(93, 235, leftcol, text="Actives:")
        canvas.create_text(93, 250, leftcol, text="Moves Owned:")

    def pop_moves(self):
        frame = tk.Frame(self.moves_frame)
        frame.grid(row=0, column=0)
        movelist = getattr(moves, "MOVELIST")

        moveheight = 50 * (int(len(movelist) / 5) + 1)
        yheight = max(moveheight, 337)

        self.moves_canvas = tk.Canvas(frame, bg="purple", height=337, width=414, scrollregion=(0, 0, 414, yheight),
                                      highlightthickness=0)
        self.moves_canvas.pack()

    def repaint_moves(self):
        canvas = self.moves_canvas

        canvas.delete(tk.ALL)

        scroll = tk.Scrollbar(self.moves_frame)
        self.moves_canvas.configure(yscrollcommand=scroll.set)
        scroll.config(command=self.moves_canvas.yview)
        scroll.grid(row=0, column=1, sticky='ns')

        global images
        images['armoryIcon'] = tk.PhotoImage(file="imgs/menu/armoryicon.png")
        images['armoryPassive'] = tk.PhotoImage(file="imgs/menu/armoryPassive.png")
        images['armoryTruePassive'] = tk.PhotoImage(file="imgs/menu/armoryTruePassive.png")
        profile = self.main_menu.active_profile

        k = 0
        self.move_buttons = dict()
        for move in moves.MOVELIST:
            if move == "none" or move not in profile.abilities.keys():
                pass
            else:
                a = ArmoryButton(self, k, move)
                self.move_buttons[move] = a
                lvl = profile.abilities[move]
                if lvl >= armory_moves[move].upgrade_max:
                    a.set_lvl_text("MAX")
                elif lvl > 10:
                    a.set_lvl_text(ArmoryButton.lvl[11])
                else:
                    a.set_lvl_text(ArmoryButton.lvl[lvl])

                k += 1

    def set_info(self, move):
        self.active_move = move

        profile = self.main_menu.active_profile
        global images
        self.info_canvas.itemconfig("info_icon", image=images[move])

        lvl = 0
        if move in profile.abilities.keys():
            lvl = profile.abilities[move]

        self.info.config(state="normal")
        obj = armory_moves[move]
        self.info.delete(1.0, tk.END)
        text = obj.description_long()
        self.info.insert(tk.END, text[0], "title")
        if len(text) > 2:
            self.info.insert(tk.END, "\n%s" % text[2], "small")

        self.info.insert(tk.END, "\nCurrent Level: %d" % lvl, "tiny")
        self.info.insert(tk.END, '\n' + text[1])
        self.info.config(state="disabled")

        if text[2] == "True Passive":
            self.buy_btn.configure(text="Equip  ", state="disabled")
            self.unbind_hover1(self.buy_btn)
        else:
            self.buy_btn.configure(text="Equip  ", state="normal")
            self.bind_hover1(self.buy_btn)


    def show_menu(self):
        self.armory_frame.grid_forget()
        self.main_menu.menu_frame.grid(row=0, column=0)

    def show_shop(self):
        self.armory_frame.grid_forget()
        self.main_menu.shop()


class ArmoryButton:
    lvl = ["--", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "X+"]

    def __init__(self, armory, count, move):
        self.y = int(count / 5)
        self.x = count % 5

        self.move = move
        self.armory = armory

        global armory_moves
        class_ = getattr(moves, move)
        armory_moves[move] = class_()

        canvas = armory.moves_canvas
        self.canvas = canvas
        global images

        images[move] = tk.PhotoImage(file="imgs/statbar/%s" % armory_moves[move].spriteName)
        canvas.create_image(self.x * 83 + 33, self.y * 50, anchor='nw', image=images[move],
                            tags=[self.move, self.move + "_sprite"])

        canvas.create_image(self.x * 83, self.y * 50, anchor='nw', image=images['armoryIcon'],
                            tags=[self.move, self.move + "_cover"])

        foo = armory_moves[move].description_long()[2]
        if foo == "True Passive":
            canvas.create_image(self.x * 83, self.y * 50, anchor='nw', image=images['armoryTruePassive'],
                                tags=[self.move, self.move + "_passive"])
        elif foo == "Equippable Passive":
            canvas.create_image(self.x * 83, self.y * 50, anchor='nw', image=images['armoryPassive'],
                                tags=[self.move, self.move + "_passive"])
        else:
            pass
        canvas.create_text(self.x * 83 + 16, self.y * 50 + 25, anchor='n', text="LVL",
                           tags=[self.move, self.move + "_lvl"])

        # bind all the move icons to the click method
        canvas.tag_bind(self.move, "<Button-1>", self.click)

    def set_lvl_text(self, text):
        self.canvas.itemconfig(self.move + "_lvl", text=text)

    def click(self, event):
        pass
        self.armory.set_info(self.move)
