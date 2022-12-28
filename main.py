import tkinter as tk
from tkinter import messagebox
import time
import datetime


class Clicker:
    counter = 0
    start_time = None
    cps = 0

    @classmethod
    def click(cls, event=None):
        if cls.counter == 0:
            cls.start_time = time.time()
        cls.counter += 1
        clicks_counter["text"] = f"clicks: {cls.counter}"
        time_diff = time.time()-cls.start_time
        displayed_time = time.gmtime(time_diff)
        displayed_time = time.strftime("%M:%S", displayed_time)
        timer_label["text"] = "time:", displayed_time
        cls.cps = round(cls.counter / time_diff, 1)
        if cls.counter == 1:
            cls.cps = 1
        cps_counter.config(text=f"cps: {cls.cps}")

    @classmethod
    def finish(cls):
        messagebox.showinfo(
            title="Result", message=f"You clicked {cls.counter} times with an average speed of {cls.cps} cps")
        cls.counter = 0
        cls.cps = 0
        cps_counter.config(text=f"cps: {cls.cps}")
        timer_label["text"] = "time: 00:00"
        clicks_counter["text"] = f"clicks: {cls.counter}"
        answer = messagebox.askquestion(
            title="Quit?", message="Do you want to exit?")
        if answer == "yes":
            window.destroy()


clicker = Clicker()

window = tk.Tk()
window.title("CPS tester")
window.resizable(0, 0)
window.geometry("500x200")

click_label = tk.Label(text="click here", bg="azure3",
                       width=24, height=7, font=("sans", 24, "bold"))
click_label.bind("<Button-1>", clicker.click)
click_label.place(width=340, height=200)

cps_counter = tk.Label(text="cps: 0",
                       bg="paleturquoise1", font=("sans", 20, "bold"))
cps_counter.place(x=340, y=0, width=160, height=70)

finish_button = tk.Button(text="finish", bg="plum1",
                          command=clicker.finish, font=("sans", 14), borderwidth=3)
finish_button.place(x=340, y=150, width=160, height=50)

timer_label = tk.Label(window, text="time: 00:00",
                       bg="paleturquoise2", font=("sans", 14), width=22)
timer_label.place(x=340, y=70, width=160, height=40)

clicks_counter = tk.Label(window, text="clicks: 0",
                          bg="paleturquoise3", font=("sans", 14), width=22)
clicks_counter.place(x=340, y=110, width=160, height=40)

window.mainloop()
