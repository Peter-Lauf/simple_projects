import tkinter as ui
from tkinter import *
import time
import math


window = ui.Tk()
window.geometry("600x600")


def update_time():
    hours = int(time.strftime("%H"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))

    seconds_x = seconds_hand_len * math.sin(math.radians(seconds * 6)) + center_x
    seconds_y = -1 * seconds_hand_len * math.cos(math.radians(seconds * 6)) + center_y
    canvas.coords(seconds_hand, center_x, center_y, seconds_x, seconds_y)

    minutes_x = minutes_hand_len * math.sin(math.radians(minutes * 6)) + center_x
    minutes_y = -1 * minutes_hand_len * math.cos(math.radians(minutes * 6)) + center_y
    canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)

    hours_x = hours_hand_len * math.sin(math.radians(hours * 30)) + center_x
    hours_y = -1 * hours_hand_len * math.cos(math.radians(hours * 30)) + center_y
    canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)

    window.after(1000, update_time)

canvas = ui.Canvas(window, width=600, height=600, bg="plum3")
canvas.pack(expand=True, fill='both')

bg = ui.PhotoImage(file='new.png')
canvas.create_image(300, 300, image=bg)

center_x = 300
center_y = 300
seconds_hand_len = 240
minutes_hand_len = 190
hours_hand_len = 150

seconds_hand = canvas.create_line(300, 300,
                                  300 + seconds_hand_len, 300 + seconds_hand_len,
                                  width=2, fill="red")

minutes_hand = canvas.create_line(300, 300,
                                  300 + minutes_hand_len, 300 + minutes_hand_len,
                                  width=3, fill="black")

hours_hand = canvas.create_line(300, 300,
                                  300 + hours_hand_len, 300 + hours_hand_len,
                                  width=6, fill="black")
update_time()

window.mainloop()
