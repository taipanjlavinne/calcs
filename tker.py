#/usr/bin/python3

import math
from tkinter import *
from tkinter.ttk import *

trigFun = [
    {'name': 'sin',   'aT': 'asin',  'w': None, 'tvar': None, 'i': None},
    {'name': 'cos',   'aT': 'acos',  'w': None, 'tvar': None, 'i': None},
    {'name': 'tan',   'aT': 'atan',  'w': None, 'tvar': None, 'i': None},
    {'name': 'sec',   'aT': '',      'w': None, 'tvar': None, 'i': None},
    {'name': 'cot',   'aT': '',      'w': None, 'tvar': None, 'i': None},
    {'name': 'sinh',  'aT': 'asinh', 'w': None, 'tvar': None, 'i': None},
    {'name': 'cosh',  'aT': 'acosh', 'w': None, 'tvar': None, 'i': None},
    {'name': 'tanh',  'aT': 'atanh', 'w': None, 'tvar': None, 'i': None},
    {'name': 'coth',  'aT': '',      'w': None, 'tvar': None, 'i': None},
    {'name': 'sech',  'aT': '',      'w': None, 'tvar': None, 'i': None},
    {'name': 'shift', 'aT': '',      'w': None, 'tvar': None, 'i': None},
    {'name': '...',   'aT': '',      'w': None, 'tvar': None, 'i': None}
]

fun = [
    {'name': 'ln',    'aT': '',      'w': None, 'tvar': None, 'i': None},
    {'name': 'log10', 'aT': 'log2',  'w': None, 'tvar': None, 'i': None}
]


def buttonCallback(namn):
    print(namn)

root = Tk()

# Frames --------------------------------------------------------------
formulaFrame = Frame(root)
formulaFrame['width'] = 400
formulaFrame['height'] = 40
formulaFrame['relief'] = ''
formulaFrame['borderwidth'] = 1

functionFrame = Frame(root)

digitFrame = Frame(root)


formulaFrame.grid(columnspan = 2, row = 0, column = 0, sticky = (N, W, E, S))
functionFrame.grid(row = 1, column = 0, sticky = (S, W))
digitFrame.grid(row = 1, column = 1, sticky = (S, E))

root.rowconfigure(0, weight = 2)

# Buttons ---------------------------------------------------------------------
lenDiv2 = int(math.sqrt(len(trigFun)))
x = 0
y = 0
for d in trigFun:
    sv = StringVar()
    d['tvar'] = sv
    sv.set(d['name'])
    d['w'] = Button(
        functionFrame, 
        textvariable = sv,
        width = 5,
        command = lambda d=d: buttonCallback(d['name'])
    )
    if y == lenDiv2:
        y = 0
        x += 1
    d['w'].grid(row = x, column = y)
    y += 1

root.mainloop()
