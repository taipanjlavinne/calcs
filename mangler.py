#!/usr/bin/env python3
import re

'''Various functions and structures to mangle mathematical formulas

   Using "mangled_text" to notate [ready to calculate] text with inner format
'''


# Mangling signs to ease resolve
def signmangle(mangled_text):
    mangled_text = re.sub(r'\+\-', r'\-', mangled_text)
    mangled_text = re.sub(r'\-\-', r'\+', mangled_text)
    mangled_text = re.sub(r'\+\+', r'\+', mangled_text)
    mangled_text = re.sub(r'\-\+', r'\-', mangled_text)
    return mangled_text

# math functions which take single parameter
# TODO: when adding functions remember to put first longer
# which have same string in them
_single_param_functions = [
    {'fT': 'angular', 'pT': 'mpfr', 'cN': 'atanh',  'ka': ['atanh']},
    {'fT': 'angular', 'pT': 'mpfr', 'cN': 'asinh',  'ka': ['asinh']},
    {'fT': 'angular', 'pT': 'mpfr', 'cN': 'acosh',  'ka': ['acosh']},
    {'fT': 'angular', 'pT': 'mpfr', 'cN': 'tanh',   'ka': ['tanh']},
    {'fT': 'angular', 'pT': 'mpfr', 'cN': 'sinh',   'ka': ['sinh']},
    {'fT': 'angular', 'pT': 'mpfr', 'cN': 'cosh',   'ka': ['cosh']},
    {'fT': 'angular', 'pT': 'mpfr', 'cN': 'coth',   'ka': ['coth']},
    {'fT': 'angular', 'pT': 'mpfr', 'cN': 'atan',   'ka': ['arctan', 'atan']},
    {'fT': 'angular', 'pT': 'mpfr', 'cN': 'asin',   'ka': ['arcsin', 'asin']},
    {'fT': 'angular', 'pT': 'mpfr', 'cN': 'acos',   'ka': ['arccos', 'acos']},
    {'fT': 'angular', 'pT': 'mpfr', 'cN': 'tan',    'ka': ['tangent', 'tan']},
    {'fT': 'angular', 'pT': 'mpfr', 'cN': 'sin',    'ka': ['sine', 'sin']},
    {'fT': 'angular', 'pT': 'mpfr', 'cN': 'cos',    'ka': ['cosine', 'cos']},
    {'fT': 'angular', 'pT': 'mpfr', 'cN': 'cot',    'ka': ['cotangent', 'cot']},
    {'fT': ''       , 'pT': 'mpfr', 'cN': 'log2',   'ka': ['log2']},
    {'fT': ''       , 'pT': 'mpfr', 'cN': 'log10',  'ka': ['log10']},
    {'fT': ''       , 'pT': 'mpfr', 'cN': 'log',    'ka': ['log']},
    {'fT': ''       , 'pT': 'mpfr', 'cN': 'sqrt',   'ka': ['sqrt']},
    {'fT': ''       , 'pT': 'mpfr', 'cN': 'square', 'ka': ['square', 'sqr']},
    {'fT': ''       , 'pT': 'mpfr', 'cN': 'exp10',  'ka': ['exp10']},
    {'fT': ''       , 'pT': 'mpfr', 'cN': 'exp2',   'ka': ['exp2']},
    {'fT': ''       , 'pT': 'mpfr', 'cN': 'exp',    'ka': ['exp']}
]

# basic math functions which with certain aliases can
# corrupt the rest
_basic_functions = [
    {'pT': 'mpfr', 'cN': 'add',   'ka': ['+', 'add']},
    {'pT': 'mpfr', 'cN': 'sub',   'ka': ['-', 'sub']},
    {'pT': 'mpfr', 'cN': 'mul',   'ka': ['*', 'mul']},
    {'pT': 'mpfr', 'cN': 'div',   'ka': ['/', 'div']},
    {'pT': 'mpfr', 'cN': 'pow',   'ka': ['^', 'pow']}
]

# math constants
_constants = [
    {'cN': 'const_pi',      'ka': ['const_pi', 'pi']},
    {'cN': 'const_euler',   'ka': ['const_euler', 'euler']},
    {'cN': 'const_log2',    'ka': ['const_log2', 'log2']},
    {'cN': 'const_catalan', 'ka': ['const_catalan']}
]

def _do_imports():
    pass

def _fundict(name, diclist = _single_param_functions):
    for f in diclist:
        if name in f['ka']:
            return f
    return None


def _condict(name, diclist = _constants):
    for f in diclist:
        if name in f['ka']:
            return f
    return None


def mo_fun(mangled_text):
    '''Formula -> str

       Return match object
       Search text for a function which input format is
       "function_name data" without parens, used for actual
       calculation.
    '''
    l = []
    for f in _single_param_functions:
        l.extend(f['ka'])
    pattern = r'(' + '|'.join(l) + r')[ \d\,\.]+'
    return re.search(pattern, mangled_text)


def mo_con(mangled_text):
    '''Formula -> str

       Return match object
       Search text for a constant which input format is
       "constant_name"
    '''
    l = []
    for f in _constants:
        l.extend(f['ka'])
    pattern = r'(' + '|'.join(l) + r')'
    return re.search(pattern, mangled_text)


def mangle_fun_to_exec(mangled_text, Degrees=False):
    outs = ''
    a = re.search(r'\s*[a-zA-Z]+(2|(10))?\s*', mangled_text)
    x, y = a.span()
    dic = _fundict(a.group().strip())
    s = dic['pT']
    n = dic['cN']
    if (dic['fT'] is 'angular') and Degrees:
        if n.startswith('a'):  # function is arcus something ?...
            outs =  'str(%s(%s(%s("%s"))))' % ('degrees',
                                              n,
                                              s,
                                              mangled_text[y:].strip())
        else:
            outs =  'str(%s(%s(%s("%s"))))' % (n,
                                              'radians',
                                              s,
                                              mangled_text[y:].strip())
    else:
        outs =  'str(%s(%s("%s")))' % (n,
                                      s,
                                      mangled_text[y:].strip())
    return outs


def mangle_const_to_exec(mangled_text):
    mo_ = _condict(mangled_text)
    return r'str(%s())' % mo_['cN']


def mangle_calc_to_exec(mangled_text):
    '''mangles evaluatable function str from  basic math operation

       e.q '1 - 1' => str(sub(mpfr("1"), mpfr("1")))
    '''
    # added look`behind to avoid confusion with negative numbers
    mo = re.search('(?<=\d)(\s*[\+\-\/\*\^])', mangled_text)
    fd = _fundict(mo.group().strip(), diclist = _basic_functions)
    x, y = mo.span()
    return 'str(%s(%s("%s"), %s("%s")))' %( fd['cN'],fd['pT'],
                                            mangled_text[:x],
                                            fd['pT'],
                                            mangled_text[y:]
                                            )


def mo_ptext(mangled_text):
    return re.search(r'\([^\(\)]+\)', mangled_text)


def mo_calc(mangled_text):
    x = re.search(r'(\-?\d+\.?\d*)[\^](\-?\d+\.?\d*)', mangled_text)
    if not x:
        x = re.search(r'(\-?\d+\.?\d*)[\*\/](\-?\d+\.?\d*)', mangled_text)
        if not x:
            x = re.search(r'(\-?\d+\.?\d*)[\-\+](\-?\d+\.?\d*)', mangled_text)
    return x
