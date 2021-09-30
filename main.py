#! bin/env python3
# importing required modules

"""This programme is created by Munseer."""

from tkinter import *
from tkinter.ttk  import *

from time import strftime

# setting up clock
root =Tk()
root.title("clock")

def time():
	string =strftime('%h:%H:%M:%S %p')
	label.config(text=string)
	label.after(1000, time)
	
label = Label(root, font=("ds-digital", 25), background = "black", foreground = "cyan")
label.pack(anchor='center')
time()

# finishing clock
mainloop()
