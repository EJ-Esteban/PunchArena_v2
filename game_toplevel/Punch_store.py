import tkinter as tk
import math

import moves

# need a top level reference to images to prevent garbage collection
images = dict()

# storing these constants up here for convenience
d_offset = [47, 300]
d_segment = 18
d_center = 37

d_red = [0, 0, 1, -1, 0, -2, -1, -1]
d_blue = [0, 0, 1, -1, 2, 0, 1, 1]
d_green = [0, 0, 1, 1, 0, 2, -1, 1]
d_yellow = [0, 0, -1, 1, -2, 0, -1, -1]


class PunchArenaStore:
    def __init__(self, main_menu):
        tkRoot = self.tkRoot = main_menu.tkRoot
        self.main_menu = main_menu
        self.main_menu.menu_frame.grid_forget()

        self.shop_frame = tk.Frame(tkRoot, bg='pink', width=600, height=550, highlightthickness=0)
        self.shop_frame.grid(row=0, column=0)

        # self.shop_frame.tkraise()

        self.make_drawing_area()
        self.pop_buttons_save()
        self.pop_info()
        self.pop_profile()
        self.pop_moves()
        self.update_profile()

    def make_drawing_area(self):
        global images
        self.c_canvas = [None] * 5
        self.c_canvas[0] = tk.Canvas(self.shop_frame, bg='red', width=600, height=6, highlightthickness=0)
        images['canvas0'] = tk.PhotoImage(file='imgs/menu/shopcover01.png')
        self.c_canvas[0].create_image(0, 0, image=images['canvas0'], anchor="nw")
        self.c_canvas[0].grid(row=0, column=0, columnspan=3)
        self.c_canvas[1] = tk.Canvas(self.shop_frame, bg='yellow', width=6, height=493, highlightthickness=0)
        images['canvas1'] = tk.PhotoImage(file='imgs/menu/shopcover02.png')
        self.c_canvas[1].create_image(0, 0, image=images['canvas1'], anchor="nw")
        self.c_canvas[1].grid(row=1, column=0, rowspan=3)
        self.c_canvas[2] = tk.Canvas(self.shop_frame, bg='blue', width=431, height=7, highlightthickness=0)
        images['canvas2'] = tk.PhotoImage(file='imgs/menu/shopcover03.png')
        self.c_canvas[2].create_image(0, 0, image=images['canvas2'], anchor="nw")
        self.c_canvas[2].grid(row=2, column=1)
        self.c_canvas[3] = tk.Canvas(self.shop_frame, bg='green', width=163, height=493, highlightthickness=0)
        images['canvas3'] = tk.PhotoImage(file='imgs/menu/shopcover04.png')
        self.c_canvas[3].create_image(0, 0, image=images['canvas3'], anchor="nw", tag="cover")
        self.c_canvas[3].grid(row=1, column=2, rowspan=3)
        self.c_canvas[4] = tk.Canvas(self.shop_frame, bg='orange', width=600, height=51, highlightthickness=0)
        images['canvas4'] = tk.PhotoImage(file='imgs/menu/shopcover05.png')
        self.c_canvas[4].create_image(0, 0, image=images['canvas4'], anchor="nw")
        self.c_canvas[4].grid(row=4, column=0, columnspan=3)
        self.moves_frame = tk.Frame(self.shop_frame, bg='light blue', width=431, height=337, highlightthickness=0)
        self.moves_frame.grid(row=1, column=1)
        self.info_canvas = tk.Canvas(self.shop_frame, bg='light green', width=431, height=149, highlightthickness=0)
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

        armory_btn = tk.Button(tkRoot, btn_options, command=self.show_armory)
        armory_btn.configure(text="Armory")
        self.bind_hover1(armory_btn)
        canvas.create_window(75, 99, width=75, anchor='nw', window=armory_btn, height=50)

        buy_btn = tk.Button(tkRoot, btn_options)
        buy_btn.configure(text="Buy   ", font="impact 22", anchor="e")
        self.bind_hover1(buy_btn)
        canvas.create_window(0, 50, width=150, anchor='nw', window=buy_btn, height=49)

        global images
        images['info_under'] = tk.PhotoImage(file="imgs/statbar/errorblock.gif")
        images['info_over'] = tk.PhotoImage(file="imgs/statbar/buttoncover.gif")

        canvas.create_image(100, 0, image=images['info_under'], anchor='nw')
        canvas.create_image(100, 0, image=images['info_over'], anchor='nw', tag='info_icon')

        self.info = tk.Text(self.shop_frame, bg="dim gray", font="helvetica 10", wrap="word", foreground="white",
                            bd=2)
        canvas.create_window(150, 0, width=265, height=149, anchor='nw', window=self.info)

        scroll = tk.Scrollbar(self.shop_frame)
        self.info.configure(yscrollcommand=scroll.set, state="disabled")
        scroll.config(command=self.info.yview)
        scroll.grid(row=0, column=1, sticky="NSEW")
        canvas.create_window(414, 0, width=17, height=149, anchor='nw', window=scroll)

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
        canvas.create_text(93, 96, leftcol, text="Punch Dollars:")
        canvas.create_text(93, 111, leftcol, text="Net Worth:")
        canvas.create_text(93, 126, leftcol, text="Eff. Net Worth:")
        canvas.create_text(93, 141, leftcol, text="Moves owned:")
        canvas.create_text(93, 156, leftcol, text="Upgrades:")

        canvas.create_text(93, 175, leftcol, text="Primary Trait:")
        canvas.create_text(93, 190, leftcol, text="CC Total:")
        canvas.create_text(93, 205, leftcol, text="Red CC:")
        canvas.create_text(93, 220, leftcol, text="Blue CC:")
        canvas.create_text(93, 235, leftcol, text="Green CC:")
        canvas.create_text(93, 250, leftcol, text="Yellow CC:")

        rightcol = {'font': "helvetica 10", 'anchor': 'w', 'disabledfill': 'gray', 'state': 'disabled', 'text': '--'}

        canvas.create_text(96, 96, rightcol, fill='black', tag='p_pdollars')
        canvas.create_text(96, 111, rightcol, fill='black', tag='p_networth')
        canvas.create_text(96, 126, rightcol, fill='black', tag='p_enetworth')
        canvas.create_text(96, 141, rightcol, fill='black', tag='p_moves')
        canvas.create_text(96, 156, rightcol, fill='black', tag='p_upgrades')

        canvas.create_text(96, 175, rightcol, fill='black', tag='p_trait')
        canvas.create_text(96, 190, rightcol, fill='black', tag='p_cc')
        canvas.create_text(96, 205, rightcol, fill='red', tag='p_red')
        canvas.create_text(96, 220, rightcol, fill='blue', tag='p_blue')
        canvas.create_text(96, 235, rightcol, fill='green', tag='p_green')
        canvas.create_text(96, 250, rightcol, fill='goldenrod', tag='p_yellow')

        red_diamond = self.fill_diamond(d_red, 1)
        blue_diamond = self.fill_diamond(d_blue, 1)
        green_diamond = self.fill_diamond(d_green, 1)
        yellow_diamond = self.fill_diamond(d_yellow, 1)

        canvas.create_polygon(self.diamond_coords(red_diamond), fill="pink")
        canvas.create_polygon(self.diamond_coords(blue_diamond), fill="light blue")
        canvas.create_polygon(self.diamond_coords(green_diamond), fill="light green")
        canvas.create_polygon(self.diamond_coords(yellow_diamond), fill="light yellow")

        canvas.create_polygon(self.diamond_coords(red_diamond), fill="red", tag="d_red")
        canvas.create_polygon(self.diamond_coords(blue_diamond), fill="blue", tag="d_blue")
        canvas.create_polygon(self.diamond_coords(green_diamond), fill="green", tag="d_green")
        canvas.create_polygon(self.diamond_coords(yellow_diamond), fill="yellow", tag="d_yellow")

        images['diamond'] = tk.PhotoImage(file="imgs/diamondEmpty.png")
        canvas.create_image(d_offset, image=images['diamond'], anchor='nw', tag="diamond")

    def diamond_coords(self, list):
        diamond = [list[0] + d_offset[0], list[1] + +d_offset[1],
                   list[2] + +d_offset[0], list[3] + +d_offset[1],
                   list[4] + +d_offset[0], list[5] + +d_offset[1],
                   list[6] + +d_offset[0], list[7] + +d_offset[1]]
        return diamond

    def fill_diamond(self, list, scale):
        coords = [0] * 8
        for k in range(8):
            coords[k] = list[k] * scale * d_segment + 37
        return coords

    def redraw_player(self):
        """redraw on reload"""
        self.update_profile()

    def update_profile(self):
        canvas = self.c_canvas[3]
        profile = self.main_menu.active_profile

        # change name
        canvas.itemconfig('p_name', state="normal")
        canvas.itemconfig('p_name', text=profile.name)
        global images
        i = tk.PhotoImage(file="imgs/sprites/%sS.gif" % profile.sprite)
        images['sprite_fg'] = i
        canvas.itemconfig("player_sprite", image=i)

        canvas.itemconfig("p_pdollars", state='normal', text=str(profile.punch_dollars))
        canvas.itemconfig("p_networth", state='normal', text=str(profile.net_worth))
        canvas.itemconfig("p_enetworth", state='normal', text=str(profile.effective_net_worth))

        moves = len(profile.abilities.keys()) - 1  # sub 1 because there's a blank "none" move
        upgrades = 0
        for x in profile.abilities.keys():
            if profile.abilities[x] > 1:
                upgrades += profile.abilities[x] - 1
        canvas.itemconfig("p_moves", state='normal', text=str(moves))
        canvas.itemconfig("p_upgrades", state='normal', text=str(upgrades))

        cc = profile.color_credits
        rscl = bscl = gscl = yscl = 1
        col = "white"
        if cc[0] == cc[1] == cc[2] == cc[3]:
            canvas.itemconfig("p_trait", state='normal', text="neutral", fill="black")
            if cc[0] == 0:
                rscl = bscl = gscl = yscl = 0
        else:
            j = cc.index(max(cc))
            if j is 0:
                canvas.itemconfig("p_trait", state='normal', text="Sturdy", fill="red")
                col = "red"
                bscl = float(cc[1] / cc[0])
                gscl = float(cc[2] / cc[0])
                yscl = float(cc[3] / cc[0])
            elif j is 1:
                canvas.itemconfig("p_trait", state='normal', text="Tactical", fill="blue")
                col = "blue"
                rscl = float(cc[0] / cc[1])
                gscl = float(cc[2] / cc[1])
                yscl = float(cc[3] / cc[1])
            elif j is 2:
                canvas.itemconfig("p_trait", state='normal', text="Fast", fill="green")
                col = "green"
                rscl = float(cc[0] / cc[2])
                bscl = float(cc[1] / cc[2])
                yscl = float(cc[3] / cc[2])
            elif j is 3:
                canvas.itemconfig("p_trait", state='normal', text="Agressive", fill="goldenrod")
                col = "goldenrod"
                rscl = float(cc[0] / cc[3])
                bscl = float(cc[1] / cc[3])
                gscl = float(cc[2] / cc[3])
        canvas.itemconfig('p_color', fill=col)

        total = sum(cc)
        canvas.itemconfig("p_cc", state='normal', text=str(total))
        canvas.itemconfig("p_red", state='normal', text=str(cc[0]))
        canvas.itemconfig("p_blue", state='normal', text=str(cc[1]))
        canvas.itemconfig("p_green", state='normal', text=str(cc[2]))
        canvas.itemconfig("p_yellow", state='normal', text=str(cc[3]))

        red_diamond = self.fill_diamond(d_red, math.sqrt(rscl))
        canvas.delete("d_red")
        canvas.create_polygon(self.diamond_coords(red_diamond), fill="red", tag="d_red")

        blue_diamond = self.fill_diamond(d_blue, math.sqrt(bscl))
        canvas.delete("d_blue")
        canvas.create_polygon(self.diamond_coords(blue_diamond), fill="blue", tag="d_blue")

        green_diamond = self.fill_diamond(d_green, math.sqrt(gscl))
        canvas.delete("d_green")
        canvas.create_polygon(self.diamond_coords(green_diamond), fill="green", tag="d_green")

        yellow_diamond = self.fill_diamond(d_yellow, math.sqrt(yscl))
        canvas.delete("d_yellow")
        canvas.create_polygon(self.diamond_coords(yellow_diamond), fill="yellow", tag="d_yellow")

        canvas.tag_raise("diamond")

    def pop_moves(self):
        frame = tk.Frame(self.moves_frame)
        frame.grid(row=0, column=0)

        self.moves_canvas = tk.Canvas(frame, bg="purple", height=337, width=414, scrollregion=(0, 0, 414, 500),
                                      highlightthickness=0)
        self.moves_canvas.pack()

        canvas = self.moves_canvas

        scroll = tk.Scrollbar(self.moves_frame)
        self.moves_canvas.configure(yscrollcommand=scroll.set, state="disabled")
        scroll.config(command=self.moves_canvas.yview)
        scroll.grid(row=0, column=1, sticky='ns')

        global images
        images['shopicon'] = tk.PhotoImage(file="imgs/menu/shopicon.png")

        movelist = getattr(moves, "MOVELIST")
        k = 0
        self.move_buttons = []
        for move in movelist:
            if move == "none":
                pass
            else:
                self.move_buttons.append(ShopButton(self, k, move))
                k += 1



    def show_menu(self):
        self.shop_frame.grid_forget()
        self.main_menu.menu_frame.grid(row=0, column=0)

    def show_armory(self):
        self.shop_frame.grid_forget()
        self.main_menu.armory()


class ShopButton:
    def __init__(self, shop, count, move):
        self.y = int(count / 5)
        self.x = count % 5

        self.move = move

        canvas = shop.moves_canvas
        global images
        canvas.create_image(self.x * 83, self.y * 50, anchor='nw', image=images['shopicon'], tag=self.move)
