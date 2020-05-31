import tkinter as tk
from DialogWindows import *
from TestGenerator import *
from TestItems import *

class MainWindow(tk.Frame):
    def __init__(self, parent, generator):
        tk.Frame.__init__(self, parent)
        
        self.generator = generator
        
        # File name 
        self.tname_entry = tk.Entry(self, width=30)
        button_te = tk.Button(self, text = "Change name", command=self.change_name)
        
        self.tname_entry.pack(side="top")
        button_te.pack()


        # Add TestItems buttons
        button_rv = tk.Button(self, text="Add r_var", command=lambda: self.open_dialog(RVariableDialog))
        button_ra = tk.Button(self, text="Add r_arr", command=lambda: self.open_dialog(RArrayDialog))
        self.test_label = tk.Label(self, width=80)

        self.test_label.pack(side="top", fill="x")
        button_rv.pack()
        button_ra.pack()

    def open_dialog(self, dialog):
        result = dialog(self).returnTestItem()
        self.generator.addItem(result)
        self.test_label.config(text=self.generator.test_obj.__str__())

    def change_name(self):
        name = self.tname_entry.get()
        self.generator.setName(name)

if __name__ == "__main__":
    root = tk.Tk()
    generator = TestGenerator()
    MainWindow(root, generator).pack(fill="both", expand=True)
    root.mainloop()
