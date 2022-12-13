import tkinter as tk
from tkinter import *
import time


root = tk.Tk()
frame = tk.Frame(root, bd=20, relief=RAISED, padx=10, pady=10, bg="RoyalBlue1" )


def update_time():

    hours = time.strftime("%H")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_or_pm = time.strftime("%p")
    time_text = hours + ":" + minutes + ":" + seconds + " " + am_or_pm
    display_time_label.config(text=time_text)
    display_time_label.after(1000, update_time)


display_time_label = tk.Label(frame, font=("arial", 118, "bold"),text="00:00:00", bg="greenyellow")
display_time_label.pack(padx=10, pady=10)

frame.pack()
update_time()
root.mainloop()
