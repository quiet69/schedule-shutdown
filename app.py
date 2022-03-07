import tkinter
from tkinter import *
from tkinter import messagebox
import subprocess
from webbrowser import get


def swlweep():
    try:
        h = hrs.get() or 0
        m = min.get() or 0
        s = sec.get() or 0
        timeInsec = int(h)*3600 + int(m)*60 + int(s)
        # print(timeInsec)
        # print(f'hours = {hrs.get()}\nminutes = {min.get()}\nseconds = {sec.get()}\n')
        subprocess.call(f'shutdown -s -t {timeInsec}')
    except: 
        messagebox.showerror("no worky!?", "owo input error???")


def noSlweep():
    subprocess.call('shutdown -a')

def queet():
    gui.destroy()

    
gui = Tk()
gui.title("quiet slweep")
gui.geometry('250x250')
gui.configure(background = "pink");




hours = Label(gui ,text = "hours").grid(row = 0,column = 0)
minutes = Label(gui ,text = "minutes").grid(row = 1,column = 0)
seconds= Label(gui ,text = "seconds").grid(row = 2,column = 0)


hrs = Entry(gui)
hrs.grid(row=0, column=1)

min = Entry(gui)
min.grid(row=1, column=1)

sec = Entry(gui)
sec.grid(row=2, column=1)



b1 = Button(gui)
b1.config(text = 'pleez slweep owo!', command = swlweep)
b1.grid(row=8, column=1)

b2 = Button(gui)
b2.config(text = 'no slweepy!!', command = noSlweep)
b2.grid(row=9, column=1)

b3 = Button(gui)
b3.config(text = 'clwose', command = queet)
b3.grid(row=10, column=1)

gui.mainloop()