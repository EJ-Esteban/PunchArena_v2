import tkinter as tk
import os

from Punch_mainmenu import PunchArenaMenu

tkRoot = None

if __name__ == "__main__":
    tkRoot = tk.Tk()
    tkRoot.resizable(0, 0)
    tkRoot.wm_title("Punch Arena v. 0.2.1")
    cwd = os.getcwd()
    tkRoot.iconbitmap(cwd+'/imgs/punch.ico')

    menu = PunchArenaMenu(tkRoot)

    tkRoot.mainloop()
