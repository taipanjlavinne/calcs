#!/usr/bin/env python3
from mangler import *
from gmpy2 import *        # importing all which we'll have change TODO
                           # but with some automation

_context = get_context()   # unhiding context context


def crunch(mtext, Degrees=False):
    ''' Does all calculations which are "well formatted"

        mtext = string with da formula
        return = string with da answer
    '''
    mo_c = None
    mtext = signmangle(mtext)
    mo_p = mo_ptext(mtext)
    if mo_p:         # inner parenthesis found ?
        x, y = mo_p.span()
        mo_c = mo_calc(mtext[x + 1: y])
        if mo_c:     # calculations found inside parenthesis ?
            tmp = mo_c.group()
            tmp = crunch(tmp)
            mtext = '%s%s%s' % (mtext[:x + 1], tmp, mtext[y - 1:])
        # remove dummy parenthesis
        mtext = '%s%s%s' % (mtext[:x], mtext[x + 1:y - 1], mtext[y:])
    mo_c = mo_fun(mtext)
    if mo_c:         # found matches to functions ?
        tmp = eval(mangle_fun_to_exec(mo_c.group(), Degrees))
        x, y = mo_c.span()
        mtext = '%s%s%s' % (mtext[:x], tmp, mtext[y:])
        return crunch(mtext)
    mo_c = mo_con(mtext)
    if mo_c:     # found known constants eq. pi.. ?
        tmp = eval(mangle_const_to_exec(mo_c.group()))
        i, j = mo_c.span()
        mtext = '%s%s%s' % (mtext[:i], tmp, mtext[j:])
        return crunch(mtext)
# if we got this far down, there should be only basic calculations left!!!
    mo_c = mo_calc(mtext)
    if mo_c:         # found something to crunch on ?
        tmp = eval(mangle_calc_to_exec(mo_c.group()))
        x, y = mo_c.span()
        mtext = '%s%s%s' % (mtext[:x], tmp, mtext[y:])
        return crunch(mtext)
    # finally we are done, did we get an A+ ?
    return mtext


if __name__ is '__main__':
    print('please use appropriate program entry')
