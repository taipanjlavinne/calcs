#!/usr/bin/env python3
import re

'''Various functions and structures to mangle mathematical formulas

   Using "mtext" to notate [ready to calculate] text with inner format
'''

#pre-mangling to ease future function resolve
def premangle(mtext):
    mtext = re.sub(r'\+\-', r'\-', mtext)
    mtext = re.sub(r'\-\-', r'\+', mtext) 
    mtext = re.sub(r'\+\+', r'\+', mtext)
    return mtext

    
# math functions which take single parameter
_single_param_funs = [
    {'pT': 'mpfr', 'cN': 'atan',   'ka': ['arctan', 'atan']},
    {'pT': 'mpfr', 'cN': 'asin',   'ka': ['arcsin', 'asin']},
    {'pT': 'mpfr', 'cN': 'acos',   'ka': ['arccos', 'acos']},
    {'pT': 'mpfr', 'cN': 'tan',    'ka': ['tangent', 'tan']},
    {'pT': 'mpfr', 'cN': 'sin',    'ka': ['sine', 'sin']},
    {'pT': 'mpfr', 'cN': 'cos',    'ka': ['cosine', 'cos']},
    {'pT': 'mpfr', 'cN': 'atanh',  'ka': ['atanh']},
    {'pT': 'mpfr', 'cN': 'asinh',  'ka': ['asinh']},
    {'pT': 'mpfr', 'cN': 'acosh',  'ka': ['acosh']},
    {'pT': 'mpfr', 'cN': 'tanh',   'ka': ['tanh']},
    {'pT': 'mpfr', 'cN': 'sinh',   'ka': ['sinh']},
    {'pT': 'mpfr', 'cN': 'cosh',   'ka': ['cosh']},
    {'pT': 'mpfr', 'cN': 'cot',    'ka': ['cotangent', 'cot']},
    {'pT': 'mpfr', 'cN': 'coth',   'ka': ['coth']},
    {'pT': 'mpfr', 'cN': 'log',    'ka': ['log']},
    {'pT': 'mpfr', 'cN': 'log10',  'ka': ['log10']},
    {'pT': 'mpfr', 'cN': 'log2',   'ka': ['log2']},
    {'pT': 'mpfr', 'cN': 'square', 'ka': ['square', 'sqr']},
    {'pT': 'mpfr', 'cN': 'sqrt',   'ka': ['sqrt']},
    {'pT': 'mpfr', 'cN': 'exp',    'ka': ['exp']},
    {'pT': 'mpfr', 'cN': 'exp2',   'ka': ['exp2']},
    {'pT': 'mpfr', 'cN': 'exp10',  'ka': ['exp10']}
]

# basic math functions which with certain aliases can
# corrupt the rest
_basic_funs = [
    {'pT': 'mpfr', 'cN': 'add',   'ka': ['+', 'add']},
    {'pT': 'mpfr', 'cN': 'sub',   'ka': ['-', 'sub']},
    {'pT': 'mpfr', 'cN': 'mul',   'ka': ['*', 'mul']},
    {'pT': 'mpfr', 'cN': 'div',   'ka': ['/', 'div']}    
]
# math constants
_mathconstants = [
    {'cN': 'const_pi',      'ka': ['const_pi', 'pi']},
    {'cN': 'const_euler',   'ka': ['const_euler', 'euler']},
    {'cN': 'const_log2',    'ka': ['const_log2', 'log2']},
    {'cN': 'const_catalan', 'ka': ['const_catalan']}
]


def _fundict(name, diclist = _single_param_funs):
    for f in diclist:
        if name in f['ka']:
            return f
    return None


def _condict(name, diclist = _mathconstants):
    for f in diclist:
        if name in f['ka']:
            return f
    return None


def mofun(text):
    '''Formula -> str

       Return match object
       Search text for a function which input format is
       "function_name()" with parens, used for actual
       calculation. Translations done elsewhere
    '''
    l = []
    for f in _single_param_funs:
        l.extend(f['ka'])
    pattern = r'(' + '|'.join(l) + r')\([^\(]+\)'
    return re.search(pattern, text)


def mocon(text):
    '''Formula -> str

       Return match object
       Search text for a constant which input format is
       "constant_name"
    '''
    l = []
    for f in _mathconstants:
        l.extend(f['ka'])
    pattern = r'(' + '|'.join(l) + r')'
    return re.search(pattern, text)


def mangle_fun_to_exec(mtext):
    i = mtext.find('(')
    e = mtext.find(')')
    s = _fundict(mtext[:i])['pT']
    return 'str(%s%s("%s")))' % (mtext[:i + 1], s,  mtext[i + 1:e])


def mangle_const_to_exec(mtext):
    mo = _condict(mtext)
    return r'str(%s())' % mo['cN']


def mangle_calc_to_exec(mtext):
    '''mangles evaluatable function str from  basic math operation

       e.q '1 - 1' => str(sub(mpfr("1"), mpfr("1")))
    '''
    # added look`a`head to avoid confusion with negative numbers
    mo = re.search('(?<=\d)(\s*[\+\-\/\*])', mtext)
    fd = _fundict(mo.group().strip(), diclist = _basic_funs)
    x, y = mo.span()
    return 'str(%s(%s("%s"), %s("%s")))' % (
        fd['cN'],
        fd['pT'],
        mtext[:x],
        fd['pT'],
        mtext[y:]
        )


def moptext(mtext):
    return re.search(r'\([^\(\)]\)', mtext)


def mocalc(mtext):
    x = r'(\-?\d+\.?\d*)[\-\+\=\*\/](\-?\d+\.?\d*)'
    return re.search(x, mtext)
