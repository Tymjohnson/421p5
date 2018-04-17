# GUI.py
# Tyler Johnson & Michael Mulzer
# April 9 2018
# Sample GUI to implement into dnsSpoof project
from Tkinter import *
import sys
import os


def start(event=None):
    output['text'] = "started!"
    os.system('python Spoof.py')


def stop(event=None):
    output['text'] = "Please clear your DNS cache"


def clear(event=None):
    output['text'] = ""


master = Tk()


output = Label(master, text="")
output.grid(column=0, row=0, columnspan=3)


b = Button(master, text="Start")
b.grid(column=2, row=5)
b.value = 0
b.bind('<Button>', start)


# Include the operator buttons
add = Button(master, text="Stop")
add.grid(column=3, row=5, rowspan=4)
add.value = '+'
add.bind("<Button>", stop)


cl = Button(master, text="Reset")
cl.grid(column=4, row=5, columnspan=3)
cl.bind("<Button>", clear)

mainloop()
