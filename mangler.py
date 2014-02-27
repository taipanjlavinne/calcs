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
# TODO: when adding functions remember to put first 
# longer name which have same substring in them

_single_param_functions = [
    {'fT': 'angular', 'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.atanh',
     'ka': ['atanh']},
    {'fT': 'angular', 'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.asinh',
     'ka': ['asinh']},
    {'fT': 'angular', 'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.acosh',
     'ka': ['acosh']},
    {'fT': 'angular', 'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.tanh',
     'ka': ['tanh']},
    {'fT': 'angular', 'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.sinh',
     'ka': ['sinh']},
    {'fT': 'angular', 'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.cosh',
     'ka': ['cosh']},
    {'fT': 'angular', 'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.sech',
     'ka': ['secanth', 'sech']},
    {'fT': 'angular', 'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.coth',
     'ka': ['coth', 'ctnh', 'cotanh']},
    {'fT': 'angular', 'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.atan',
     'ka': ['arctan', 'atan']},
    {'fT': 'angular', 'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.asin',
     'ka': ['arcsin', 'asin']},
    {'fT': 'angular', 'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.acos',
     'ka': ['arccos', 'acos']},
    {'fT': 'angular', 'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.tan',
     'ka': ['tangent', 'tan']},
    {'fT': 'angular', 'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.sin',
     'ka': ['sine', 'sin']},
    {'fT': 'angular', 'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.cos',
     'ka': ['cosine', 'cos']},
    {'fT': 'angular', 'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.cot',
     'ka': ['cotangent', 'cot', 'cotan', 'ctn']},
    {'fT': 'angular', 'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.sec',
     'ka': ['secant', 'sec']},
    {'fT': 'angular', 'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.csc',
     'ka': ['cosecant', 'csc']},
    {'fT': ''       , 'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.log2',
     'ka': ['log2']},
    {'fT': ''       , 'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.log10',
     'ka': ['log10']},
    {'fT': ''       , 'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.log',
     'ka': ['log']},
    {'fT': ''       , 'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.sqrt',
     'ka': ['sqrt']},
    {'fT': ''       , 'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.square',
     'ka': ['square', 'sqr']},
    {'fT': ''       , 'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.exp10',
     'ka': ['exp10']},
    {'fT': ''       , 'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.exp2',
     'ka': ['exp2']},
    {'fT': ''       , 'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.exp',
     'ka': ['exp']}
]

# basic math functions which with certain aliases can
# corrupt the rest
_basic_functions = [
    {'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.add',   'ka': ['+', 'add']},
    {'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.sub',   'ka': ['-', 'sub']},
    {'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.mul',   'ka': ['*', 'mul']},
    {'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.div',   'ka': ['/', 'div']},
    {'pT': 'gmpy2.mpfr', 'cN': 'gmpy2.pow',   'ka': ['^', 'pow']}
]

# added these since decimal module is better with them
# than gmpy2
_basic_D_functions = [
    {'pT': 'decimal.Decimal', 'cN': 'decimal.getcontext().add',
     'ka': ['+', 'add']},
    {'pT': 'decimal.Decimal', 'cN': 'decimal.getcontext().subtract',
     'ka': ['-', 'sub']},
    {'pT': 'decimal.Decimal', 'cN': 'decimal.getcontext().multiply',
     'ka': ['*', 'mul']},
    {'pT': 'decimal.Decimal', 'cN': 'decimal.getcontext().divide',
     'ka': ['/', 'div']},
    {'pT': 'decimal.Decimal', 'cN': 'decimal.getcontext().power',
     'ka': ['^', 'pow']}
]


# math constants
_constants = [
    {'cN': 'gmpy2.const_pi',      'ka': ['const_pi', 'pi']},
    {'cN': 'gmpy2.const_euler',   'ka': ['const_euler', 'euler']},
    {'cN': 'gmpy2.const_log2',    'ka': ['const_log2', 'log2']},
    {'cN': 'gmpy2.const_catalan', 'ka': ['const_catalan']}
]

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
            outs =  'str(%s(%s(%s("%s"))))' % ('gmpy2.degrees',
                                              n,
                                              s,
                                              mangled_text[y:].strip())
        else:
            outs =  'str(%s(%s(%s("%s"))))' % (n,
                                              'gmpy2.radians',
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
    retval = ''
    mo = re.search(r'(?<=\d)(\s*[\+\-\/\*\^])', mangled_text)
    dmo = re.search(r'[bx]', mangled_text)
    if dmo:  # if contains b or x, decimal module cant cope 
        fd = _fundict(mo.group().strip(), diclist = _basic_functions)
    else:
        fd = _fundict(mo.group().strip(), diclist = _basic_D_functions)
    x, y = mo.span()
    retval = 'str(%s(%s("%s"), %s("%s")))' %( fd['cN'],fd['pT'],
                                              mangled_text[:x],
                                              fd['pT'],
                                              mangled_text[y:]
                                              )
    return retval



def mo_ptext(mangled_text):
    return re.search(r'\([^\(\)]+\)', mangled_text)


def mo_calc(mangled_text):
    x = re.search(r'(\-?\d+\.?\d*)[\^](\-?\d+\.?\d*)', mangled_text)
    if not x:
        x = re.search(r'(\-?\d+\.?\d*)[\*\/](\-?\d+\.?\d*)', mangled_text)
        if not x:
            x = re.search(r'(\-?\d+\.?\d*)[\-\+](\-?\d+\.?\d*)', mangled_text)
    return x
