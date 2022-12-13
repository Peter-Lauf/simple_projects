import tkinter as tk
from tkinter import *
import  time

root = tk.Tk()
frame = tk.Frame(root, bd=5, relief=SUNKEN)
root.geometry("400x400")


def update_time():
    hours = time.strftime("%H")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_or_pm = time.strftime("%p")
    time_text = hours + ":" + minutes + ":" + seconds + " " + am_or_pm


canvas = tk.Canvas(frame, width=400, height=400, bg="goldenrod3")
canvas.pack(expand=True, fill="both")

bg = tk.PhotoImage(file="clock_face.png")
canvas.create_image(200, 200, image=bg)

update_time()
root.mainloop()