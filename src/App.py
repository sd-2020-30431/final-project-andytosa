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
        
        self.tname_entry.pack()
        button_te.pack()

        # Generate Tests
        self.nr_entry = tk.Entry(self, width=30)
        button_gen = tk.Button(self, text = "Generate", command=self.generate)
        
        self.nr_entry.pack()
        button_gen.pack()

        
        # Container Select
        self.repeaters = [self.generator.test_obj] + self.generator.test_obj.repeaters
        r_names = [x.getName() for x in self.repeaters]
        self.r_var = tk.StringVar()
        self.r_menu = tk.OptionMenu(self, self.var, *r_names)

        # Add TestItems buttons
        button_rv = tk.Button(self, text="Add r_var", command=lambda: self.open_dialog(RVariableDialog))
        button_ra = tk.Button(self, text="Add r_arr", command=lambda: self.open_dialog(RArrayDialog))
        button_rc = tk.Button(self, text="Add r_cnt", command=lambda: self.open_dialog(RContainerDialog))
        self.test_label = tk.Label(self, width=80)

        button_rv.pack()
        button_ra.pack()
        button_rc.pack()
        self.test_label.pack(side="top", fill="x")


    def generate(self):
        nr = self.nr_entry.get()
        self.generator.generate(int(nr))


    def open_dialog(self, dialog):
        result = dialog(self, self.generator.test_obj).returnTestItem()
        
        if isinstance(result, TestItem):
            self.generator.addItem(result)
            self.test_label.config(text=self.generator.test_obj.__str__())

            if isinstance(result, RepeatContainer):
                self.repeaters = [self.generator.test_obj] + self.generator.test_obj.repeaters
                r_names = [x.getName() for x in self.repeaters]
                self.r_menu.config(value=*r_names)
        else:
            pass


    def change_name(self):
        name = self.tname_entry.get()
        self.generator.setName(name)

if __name__ == "__main__":
    root = tk.Tk()
    generator = TestGenerator()
    MainWindow(root, generator).pack(fill="both", expand=True)
    root.mainloop()
