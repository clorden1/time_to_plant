#import dependecies
import tkinter as tk
from tkinter import ttk

#define window 
root = tk.Tk()
root.geometry("700x400")
#Title window
root.title('Time to Plant')

#Style widget window
# style = ttk.Style()
# style

#Labels and buttons for region and date
region_label = ttk.Label(text = 'Region').grid(column = 0, row = 0)
region_button = ttk.Button().grid(column = 1, row = 0)

date_label = ttk.Label(text = 'Date').grid(column = 0, row = 3)
date_button = ttk.Button().grid(column = 1, row = 3)

#initalize window
root.mainloop()