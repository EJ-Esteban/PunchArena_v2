import tkinter as tk
from player_profile import Profile

# need a top level reference to images to prevent garbage collection
images = dict()


class PunchArenaStore:
    def __init__(self, main_menu):
        tkRoot = self.tkRoot = main_menu.tkRoot
        self.main_menu = main_menu
        self.main_menu.menu_frame.grid_forget()

        self.shop_frame = tk.Frame(tkRoot, bg='pink', width=600, height=550, highlightthickness=0)
        self.shop_frame.grid(row=0, column=0)

        self.active_profile = main_menu.active_profile

        # self.shop_frame.tkraise()

        self.make_drawing_area()
        self.pop_buttons_save()
        self.pop_info()

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
        self.c_canvas[2] = tk.Canvas(self.shop_frame, bg='blue', width=430, height=7, highlightthickness=0)
        images['canvas2'] = tk.PhotoImage(file='imgs/menu/shopcover03.png')
        self.c_canvas[2].create_image(0, 0, image=images['canvas2'], anchor="nw")
        self.c_canvas[2].grid(row=2, column=1)
        self.c_canvas[3] = tk.Canvas(self.shop_frame, bg='green', width=164, height=493, highlightthickness=0)
        images['canvas3'] = tk.PhotoImage(file='imgs/menu/shopcover04.png')
        self.c_canvas[3].create_image(0, 0, image=images['canvas3'], anchor="nw")
        self.c_canvas[3].grid(row=1, column=2, rowspan=3)
        self.c_canvas[4] = tk.Canvas(self.shop_frame, bg='orange', width=600, height=51, highlightthickness=0)
        images['canvas4'] = tk.PhotoImage(file='imgs/menu/shopcover05.png')
        self.c_canvas[4].create_image(0, 0, image=images['canvas4'], anchor="nw")
        self.c_canvas[4].grid(row=4, column=0, columnspan=3)
        self.moves_frame = tk.Frame(self.shop_frame, bg='light blue', width=430, height=337, highlightthickness=0)
        self.moves_frame.grid(row=1, column=1)
        self.info_canvas = tk.Canvas(self.shop_frame, bg='light green', width=430, height=149, highlightthickness=0)
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

        self.info = tk.Text(self.shop_frame, bg="gray", font="helvetica 10", wrap="word", foreground="white",
                            bd=1)
        canvas.create_window(150, 0, width=263, height=149, anchor='nw', window=self.info)

        scroll = tk.Scrollbar(self.shop_frame)
        self.info.configure(yscrollcommand=scroll.set, state="disabled")
        scroll.config(command=self.info.yview)
        scroll.grid(row=0, column=1, sticky="NSEW")

        canvas.create_window(412, 0, width=18, height=149, anchor='nw', window=scroll)

    def show_menu(self):
        self.shop_frame.grid_forget()
        self.main_menu.menu_frame.grid(row=0, column=0)

    def show_armory(self):
        self.shop_frame.grid_forget()
        self.main_menu.armory()
