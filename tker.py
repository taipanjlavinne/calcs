#/usr/bin/python3

from tkinter import Frame, Button, Tk, N, W, E, S, StringVar, Label
from tkinter.font import Font
#from tkinter.ttk import Frame, Button

degs = False

try:
    degs = args.degrees
except:
    import sys
    sys.exit('not cool')

trigFun = [
        {'name': 'sin',   'a': 'asin',  'w': None, 't': None, 'i': None},
        {'name': 'cos',   'a': 'acos',  'w': None, 't': None, 'i': None},
        {'name': 'tan',   'a': 'atan',  'w': None, 't': None, 'i': None},
        {'name': 'sec',   'a': '',      'w': None, 't': None, 'i': None},
        {'name': 'csc',   'a': '',      'w': None, 't': None, 'i': None},
        {'name': 'cot',   'a': '',      'w': None, 't': None, 'i': None},
        {'name': 'sinh',  'a': 'asinh', 'w': None, 't': None, 'i': None},
        {'name': 'cosh',  'a': 'acosh', 'w': None, 't': None, 'i': None},
        {'name': 'tanh',  'a': 'atanh', 'w': None, 't': None, 'i': None},
        {'name': 'sech',  'a': '',      'w': None, 't': None, 'i': None},
        {'name': 'csch',  'a': '',      'w': None, 't': None, 'i': None},
        {'name': 'coth',  'a': '',      'w': None, 't': None, 'i': None}
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


root = Tk()
root.resizable( height=True, width = False)
root.rowconfigure(0, weight = 1, minsize = 20)

def buttonCallback(namn):
    print(namn)

# Fonts ----------------------------------------------------------------------
bFont = Font(family = 'Arial', size = 10)
aFont = Font(family = 'Arial', size = 6, weight = "bold")

# FormulaFrame -------------------------------------------------------------

formulaFrame = Frame(root)

formulaFrame['width'] = 400
formulaFrame['height'] = 40
formulaFrame['relief'] = 'solid'
formulaFrame['borderwidth'] = 1
formulaFrame.grid(columnspan = 3, row = 0, column = 0, sticky = (N, W, E, S))


# Utility Frame -------------------------------------------------------------
utilFrame = Frame(root)
utilFrame.grid(columnspan = 3, row = 1, column = 0, sticky = (N, W, E, S))


# Trigonometry Frame --------------------------------------------------------
trigFrame = Frame(root)
trigFrame.grid(row = 2, column = 0, sticky = (S, W, N))

triFrameColumns = 3
x = 0
x2 = 1
y = 0

for d in trigFun:
    sv = StringVar()
    asv = StringVar()
    asv.set(d['a'])
    if d['a'] != '':
        l = Label( 
                trigFrame,
                font = aFont,
                textvariable = asv,
                width = 5
                )
    d['t'] = sv
    sv.set(d['name'])
    d['w'] = Button(
            trigFrame, 
            font = bFont,
            padx = 0,
            pady = 0,
            textvariable = sv,
            width = 5,
            command = lambda d=d: buttonCallback(d['name'])
            )
    if y == triFrameColumns:
        y = 0
        x2 += 2
        x += 2

    if d['a'] != '':
        l.grid(row = x, column = y)
    d['w'].grid(row = x2, column = y)
    y += 1

# Misc. Function Frame ------------------------------------------------

functionFrame = Frame(root)
functionFrame.grid(row = 2, column = 1, sticky = (S, W))


#Number Frame ----------------------------------------------------------------

x = 0
y = 0

numFrame = Frame(root)
numFrame.grid(row = 2, column = 2, sticky = (S, E))
numFrameColumns = 3

for d in numFun:
    sv = StringVar()
    d['t'] = sv
    sv.set(d['name'])
    d['w'] = Button(
            numFrame, 
            textvariable = sv,
            width = 2,
            pady = 3,
            padx = 2,
            command = lambda d=d: buttonCallback(d['name'])
            )
    if y == numFrameColumns:
        y = 0
        x += 1
    d['w'].grid(row = x, column = y)
    y += 1

root.mainloop()
