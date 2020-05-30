from tkinter import *
from tkinter.ttk import *

root = Tk()
#root.geometry('500x500')

notebook = Notebook(root)
notebook.grid(sticky='NESW')

page1 = Frame(notebook, width=500, height=500)
notebook.add(page1, text='Tab1')


page2 = Frame(notebook, width=500, height=500)
notebook.add(page2, text='Tab1')


root.mainloop()
