import tkinter as tk
import os

class MyDialog:
    """
    creates a popup box that will ask for a text input. On enter/okay,
    box is destroyed and method is executed based on input

    based on some effbot tutorials
    """

    def __init__(self, tkRoot, query="", targetObj=None, targetMethod=None):
        top = self.top = tk.Toplevel(tkRoot)
        top.wm_title("Query")
        top.iconbitmap(os.getcwd() + '/imgs/punch.ico')

        tk.Label(top, text=query).grid(row=0, column=0, columnspan=2)
        self.entry = tk.Entry(top)
        self.entry.grid(row=1, column=0, padx=5, pady=5)
        self.entry.bind("<Return>", lambda event: self.ok())
        self.entry.focus_force()

        button = tk.Button(top, text="OK", command=self.ok)
        button.grid(row=1, column=1, pady=5, padx=5)

        self.targetObj = targetObj
        self.targetMethod = targetMethod

    def ok(self):
        getattr(self.targetObj, self.targetMethod, None)(self.entry.get())
        self.top.destroy()
