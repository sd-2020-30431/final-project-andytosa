import tkinter as tk


class TIDialog(object):
    def __init__(self, parent):
        self.toplevel = tk.Toplevel(parent)

    def returnTestItem(self):
        pass

    
class RVariableDialog(TIDialog):
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


