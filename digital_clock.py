import tkinter as tk
from tkinter import *
import time

root = tk.Tk()
frame = Frame(root, bd=15, relief=SUNKEN, bg="RoyalBlue2")


def update_time():
    hours = time.strftime("%H")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_or_pm = time.strftime("%p")
    time_text = hours + ":" + minutes + ":" + seconds + " " + am_or_pm
    display_label.config(text=time_text)
    display_label.after(1000, update_time)


display_label = tk.Label(
    frame, font=("arial", 118, "bold"), text="00:00:00", bg="cornflowerblue"
)

display_label.pack()

frame.pack()
update_time()
root.mainloop()
