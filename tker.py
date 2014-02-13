#/usr/bin/python3

from tkinter import *
from tkinter.ttk import *

trigFun = [
    {'name': 'sin',   'a': 'asin',  'w': None, 't': None, 'i': None},
    {'name': 'cos',   'a': 'acos',  'w': None, 't': None, 'i': None},
    {'name': 'tan',   'a': 'atan',  'w': None, 't': None, 'i': None},
    {'name': 'sec',   'a': '',      'w': None, 't': None, 'i': None},
    {'name': 'cot',   'a': '',      'w': None, 't': None, 'i': None},
    {'name': 'sinh',  'a': 'asinh', 'w': None, 't': None, 'i': None},
    {'name': 'cosh',  'a': 'acosh', 'w': None, 't': None, 'i': None},
    {'name': 'tanh',  'a': 'atanh', 'w': None, 't': None, 'i': None},
    {'name': 'coth',  'a': '',      'w': None, 't': None, 'i': None},
    {'name': 'sech',  'a': '',      'w': None, 't': None, 'i': None},
    {'name': 'shift', 'a': '',      'w': None, 't': None, 'i': None},
    {'name': 'rad',   'a': '',      'w': None, 't': None, 'i': None}
]

fun = [
    {'name': 'ln',    'a': '',      'w': None, 't': None, 'i': None},
    {'name': 'log10', 'a': 'log2',  'w': None, 't': None, 'i': None}
]

basicFun =  [
    {'name': '+',     'a': '',      'w': None, 't': None, 'i': None},
    {'name': '-',     'a': '',      'w': None, 't': None, 'i': None},
    {'name': '*',     'a': '',      'w': None, 't': None, 'i': None},
    {'name': '/',     'a': '',      'w': None, 't': None, 'i': None}
]

numFun = [
    {'name': '1',     'a': '',      'w': None, 't': None, 'i': None},
    {'name': '2',     'a': '',      'w': None, 't': None, 'i': None},
    {'name': '3',     'a': '',      'w': None, 't': None, 'i': None},
    {'name': '4',     'a': '',      'w': None, 't': None, 'i': None},
    {'name': '5',     'a': '',      'w': None, 't': None, 'i': None},
    {'name': '6',     'a': '',      'w': None, 't': None, 'i': None},
    {'name': '7',     'a': '',      'w': None, 't': None, 'i': None},
    {'name': '8',     'a': '',      'w': None, 't': None, 'i': None},
    {'name': '9',     'a': '',      'w': None, 't': None, 'i': None},
    {'name': '-',     'a': '',      'w': None, 't': None, 'i': None},
    {'name': '0',     'a': '',      'w': None, 't': None, 'i': None},
    {'name': '.',     'a': '',      'w': None, 't': None, 'i': None}
]

def buttonCallback(namn):
    print(namn)

root = Tk()
root.resizable( height=True, width = False)
root.rowconfigure(0, weight = 1, minsize = 20)

# Frames --------------------------------------------------------------
formulaFrame = Frame(root)
formulaFrame['width'] = 400
formulaFrame['height'] = 40
formulaFrame['relief'] = 'solid'
formulaFrame['borderwidth'] = 1
functionFrame = Frame(root)
trigFrame = Frame(functionFrame)

numFrame = Frame(root)


formulaFrame.grid(columnspan = 2, row = 0, column = 0, sticky = (N, W, E, S))
functionFrame.grid(row = 1, column = 0, sticky = (S, W))
numFrame.grid(row = 1, column = 1, sticky = (S, E))
trigFrame.grid(row = 0, column = 0, sticky = (S, W, N))


# Buttons ---------------------------------------------------------------------

triFrameColumns = 3

x = 0
y = 0

for d in trigFun:
    sv = StringVar()
    d['t'] = sv
    sv.set(d['name'])
    d['w'] = Button(
        trigFrame, 
        textvariable = sv,
        width = 5,
        command = lambda d=d: buttonCallback(d['name'])
    )
    if y == triFrameColumns:
        y = 0
        x += 1
    d['w'].grid(row = x, column = y)
    y += 1

x = 0
y = 0

numFrameColumns = 3

for d in numFun:
    sv = StringVar()
    d['t'] = sv
    sv.set(d['name'])
    d['w'] = Button(
       numFrame, 
        textvariable = sv,
        width = 3,
        command = lambda d=d: buttonCallback(d['name'])
    )
    if y == numFrameColumns:
        y = 0
        x += 1
    d['w'].grid(row = x, column = y)
    y += 1

root.mainloop()
