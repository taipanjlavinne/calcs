#/usr/bin/python3

from tkinter import Frame, Button, Tk, N, W, E, S, StringVar, Label
from tkinter.font import Font
from tkinter import Menu
#from tkinter.ttk import Frame, Button

degs = False

try:
    degs = args.degrees
except:
    import sys
    sys.exit('not cool')

# n for function name which used in mangler
# a for alternate -||-
# w for widget
# t for StringVar in widget
# ar for alternate representation string
# r  for           -||-
trigFun = [
        {'n': 'sin',   'a': 'asin',  'w': None, 't': None, 'ar':'sin\u207B\u00B9', 'r': 'sin' },
        {'n': 'cos',   'a': 'acos',  'w': None, 't': None, 'ar':'cos\u207B\u00B9', 'r': 'cos' },
        {'n': 'tan',   'a': 'atan',  'w': None, 't': None, 'ar':'tan\u207B\u00B9', 'r': 'tan' },
        {'n': 'sec',   'a': '',      'w': None, 't': None, 'ar':'',  'r': 'sec' },
        {'n': 'csc',   'a': '',      'w': None, 't': None, 'ar':'',  'r': 'csc' },
        {'n': 'cot',   'a': '',      'w': None, 't': None, 'ar':'',  'r': 'cot' },
        {'n': 'sinh',  'a': 'asinh', 'w': None, 't': None, 'ar':'sinh\u207B\u00B9','r': 'sinh'},
        {'n': 'cosh',  'a': 'acosh', 'w': None, 't': None, 'ar':'cosh\u207B\u00B9','r': 'cosh'},
        {'n': 'tanh',  'a': 'atanh', 'w': None, 't': None, 'ar':'tanh\u207B\u00B9','r': 'tanh'},
        {'n': 'sech',  'a': '',      'w': None, 't': None, 'ar':'',  'r': 'sech'},
        {'n': 'csch',  'a': '',      'w': None, 't': None, 'ar':'',  'r': 'csch'},
        {'n': 'coth',  'a': '',      'w': None, 't': None, 'ar':'',  'r': 'coth'}
        ]                                                   
                                                            
fun = [                                                     
        {'n': 'ln',    'a': '',      'w': None, 't': None, 'ar':'',  'r': None},
        {'n': 'log10', 'a': 'log2',  'w': None, 't': None, 'ar':'',  'r': None}
        ]                                                 
                                                          
basicFun =  [                                             
        {'n': '+', 'w': None, 't': None},
        {'n': '-', 'w': None, 't': None},
        {'n': '*', 'w': None, 't': None},
        {'n': '/', 'w': None, 't': None}
        ]                                                   
                                                            
numFun = [                                                  
        {'n': '1', 'w': None, 't': None},
        {'n': '2', 'w': None, 't': None},
        {'n': '3', 'w': None, 't': None},
        {'n': '4', 'w': None, 't': None},
        {'n': '5', 'w': None, 't': None},
        {'n': '6', 'w': None, 't': None},
        {'n': '7', 'w': None, 't': None},
        {'n': '8', 'w': None, 't': None},
        {'n': '9', 'w': None, 't': None},
        {'n': '-', 'w': None, 't': None},
        {'n': '0', 'w': None, 't': None},
        {'n': '.', 'w': None, 't': None}
        ]


root = Tk()
root.resizable( height=True, width = False)
root.rowconfigure(0, weight = 1, minsize = 20)

def buttonCallback(namn):
    print(namn)

def menuCallback(namn):
    print(namn)

# Fonts ----------------------------------------------------------------------
bFont = Font(family = 'Arial', size = 10)
aFont = Font(family = 'Arial', size = 8)

# Mainmenu ------------------------------------------------------------------
menuBar = Menu(root)
fileMenu = Menu(menuBar, tearoff = 0)
fileMenu.add_command(label = 'Quit', command = lambda: menuCallback('quit'))
menuBar.add_cascade(label = 'File', menu = fileMenu)
root.configure(menu = menuBar)


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
    asv.set(d['ar'])
    if d['ar'] != '':
        l = Label( 
                trigFrame,
                font = aFont,
                textvariable = asv,
                width = 5
                )
    d['t'] = sv
    sv.set(d['r'])
    d['w'] = Button(
            trigFrame, 
            font = bFont,
            padx = 0,
            pady = 0,
            textvariable = sv,
            width = 5,
            command = lambda d=d: buttonCallback(d['n'])
            )
    if y == triFrameColumns:
        y = 0
        x2 += 2
        x += 2

    if d['ar'] != '':
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
    sv.set(d['n'])
    d['w'] = Button(
            numFrame, 
            textvariable = sv,
            width = 2,
            pady = 3,
            padx = 2,
            command = lambda d=d: buttonCallback(d['n'])
            )
    if y == numFrameColumns:
        y = 0
        x += 1
    d['w'].grid(row = x, column = y)
    y += 1

root.mainloop()
