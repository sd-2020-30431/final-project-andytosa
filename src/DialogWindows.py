import tkinter as tk
from TestItems import *

class TIDialog(object):
    def __init__(self, parent, test_obj):
        self.toplevel = tk.Toplevel(parent)
        self.test_obj = test_obj

    def returnTestItem(self):
        pass

    
class RVariableDialog(TIDialog):
    def __init__(self, parent, test_obj):
        super().__init__(parent, test_obj)

        label = tk.Label(self.toplevel, text="name, min, max")
        self.name_entry = tk.Entry(self.toplevel, width=15)
        self.min_entry = tk.Entry(self.toplevel, width=15)
        self.max_entry = tk.Entry(self.toplevel, width=15)
        button = tk.Button(self.toplevel, text="OK", command=self.destroyWindow)

        label.pack(side="top", fill="x")
        self.name_entry.pack()
        self.min_entry.pack()
        self.max_entry.pack()
        button.pack()

    def destroyWindow(self):
        name = self.name_entry.get()
        mini = self.min_entry.get()
        maxi = self.max_entry.get()

        self.testItem = RandomVariable(name, (int(mini), int(maxi)))

        self.toplevel.destroy()
        

    def returnTestItem(self):
        self.toplevel.deiconify()
        self.toplevel.wait_window()

        return self.testItem


class RArrayDialog(TIDialog):
    def __init__(self, parent, test_obj):
        super().__init__(parent, test_obj)
        
        self.var_list = test_obj.variables

        var_names = [var.getName() for var in self.var_list]

        label = tk.Label(self.toplevel, text="var, min, max")
        self.var = tk.StringVar()
        self.opt_menu = tk.OptionMenu(self.toplevel, self.var, *var_names)
        self.min_entry = tk.Entry(self.toplevel, width=15)
        self.max_entry = tk.Entry(self.toplevel, width=15)
        button = tk.Button(self.toplevel, text="OK", command=self.destroyWindow)

        label.pack(side="top", fill="x")
        self.opt_menu.pack()
        self.min_entry.pack()
        self.max_entry.pack()
        button.pack()

    def destroyWindow(self):
        var_name = self.var.get()
        mini = self.min_entry.get()
        maxi = self.max_entry.get()
        
        var = [x for x in self.var_list if x.getName() == var_name][0]

        self.testItem = RandomArray(var, (int(mini), int(maxi)))

        self.toplevel.destroy()
        

    def returnTestItem(self):
        self.toplevel.deiconify()
        self.toplevel.wait_window()

        return self.testItem


class RContainerDialog(TIDialog):
    def __init__(self, parent, test_obj):
        super().__init__(parent, test_obj)
        
        self.var_list = test_obj.variables

        var_names = [var.getName() for var in self.var_list]

        label = tk.Label(self.toplevel, text="name, var")
        self.name_entry = tk.Entry(self.toplevel, width=15)
        self.var = tk.StringVar()
        self.opt_menu = tk.OptionMenu(self.toplevel, self.var, *var_names)
        button = tk.Button(self.toplevel, text="OK", command=self.destroyWindow)

        label.pack(side="top", fill="x")
        self.name_entry.pack()
        self.opt_menu.pack()
        button.pack()

    def destroyWindow(self):
        name = self.name_entry.get()
        var_name = self.var.get()
        
        var = [x for x in self.var_list if x.getName() == var_name][0]

        self.testItem = RepeatContainer(name, var)

        self.toplevel.destroy()
        

    def returnTestItem(self):
        self.toplevel.deiconify()
        self.toplevel.wait_window()

        return self.testItem


