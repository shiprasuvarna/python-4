#31) Write a Python GUI program to create a window and disable to resize the window using tkinter
#module.
import tkinter as tk
parent = tk.Tk()
parent.title("-Welcome to Python tkinter Basic exercises-")
# Disable resizing the GUI
parent.resizable(0,0)
parent.mainloop()
