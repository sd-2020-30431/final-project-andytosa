import tkinter as tk
from TestItems import *

class TIDialog(object):
    def __init__(self, parent):
        self.toplevel = tk.Toplevel(parent)

    def returnTestItem(self):
        pass

    
class RVariableDialog(TIDialog):
    def __init__(self, parent):
        self.toplevel = tk.Toplevel(parent)
        
        label = tk.Label(self.toplevel, text="name, min, max")
        self.name_var = tk.StringVar()
        self.name_entry = tk.Entry(self.toplevel, textvariable=self.name_var, width=15)
        self.min_entry = tk.Entry(self.toplevel, width=15)
        self.max_entry = tk.Entry(self.toplevel, width=15)
        button = tk.Button(self.toplevel, text="OK", command=self.destroyWindow)

        label.pack(side="top", fill="x")
        self.name_entry.pack()
        self.min_entry.pack()
        self.max_entry.pack()
        button.pack()

    def destroyWindow(self):
        name = self.name_var.get()
        mini = self.min_entry.get()
        maxi = self.max_entry.get()

        self.testItem = RandomVariable(name, (int(mini), int(maxi)))

        self.toplevel.destroy()
        

    def returnTestItem(self):
        self.toplevel.deiconify()
        self.toplevel.wait_window()

        return self.testItem


class RArrayDialog(TIDialog):
    def __init__(self, parent):
        self.toplevel = tk.Toplevel(parent)
        self.var = tk.StringVar()

        label = tk.Label(self.toplevel, text="Pick something:")
        om = tk.OptionMenu(self.toplevel, self.var, "one", "two","three")
        button = tk.Button(self.toplevel, text="OK", command=self.toplevel.destroy)

        label.pack(side="top", fill="x")
        om.pack(side="top", fill="x")
        button.pack()

    def returnTestItem(self):
        self.toplevel.deiconify()
        self.toplevel.wait_window()
        value = self.var.get()
        return value


