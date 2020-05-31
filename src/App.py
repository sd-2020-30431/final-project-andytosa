import tkinter as tk
from DialogWindows import *
from TestGenerator import *
from TestItems import *

class MainWindow(tk.Frame):
    def __init__(self, parent, generator):
        tk.Frame.__init__(self, parent)
        
        self.generator = generator

        button_rv = tk.Button(self, text="Add r_var", command=lambda: self.open_dialog(RVariableDialog))
        button_ra = tk.Button(self, text="Add r_arr", command=lambda: self.open_dialog(RArrayDialog))
        self.label = tk.Label(self, width=80)

        self.label.pack(side="top", fill="x")
        button_rv.pack()
        button_ra.pack()

    def open_dialog(self, dialog):
        result = dialog(self).returnTestItem()
        self.label.configure(text="your result: %s" % result)

if __name__ == "__main__":
    root = tk.Tk()
    generator = TestGenerator()
    MainWindow(root, generator).pack(fill="both", expand=True)
    root.mainloop()
