#!/usr/bin/env python3
from mangler import *
from gmpy2 import *

_context = get_context() # unhiding context context


def crunch(mtext):
    moc = None
    mtext = premangle(mtext)
    mop = moptext(mtext)
    if mop is not None:     # inner () found ?
        x, y = mop.span()
        moc = mocalc(mtext[x + 1: y])
        if moc is not None:     # calculations found ?
            tmp = moc.group()
            tmp = crunch(tmp)
            mtext = '%s%s%s' % (mtext[:x+1], tmp, mtext[y-1:])
        moc = mofun(mtext)
        if moc is not None:
            tmp = eval(mangle_fun_to_exec(moc.group()))
            x, y = moc.span()
            mtext = '%s%s%s' % (mtext[:x], tmp, mtext[y:])
            return crunch(mtext)
        moc = mocon(mtext)
        if moc is not None:
            tmp = eval(mangle_const_to_exec(moc.group()))
            i, j = moc.span()
            mtext = '%s%s%s' % (mtext[:i], tmp, mtext[j:])
            return crunch(mtext)
         # remove dummy parenthesis
        mtext = '%s%s%s' % (mtext[:x], mtext[x+1:y-1], mtext[y:])
    moc = mocalc(mtext)
    if moc is not None:
        tmp = eval(mangle_calc_to_exec(moc.group()))
        x, y = moc.span()
        mtext = '%s%s%s' % (mtext[:x], tmp, mtext[y:])
        return crunch(mtext)
    return mtext

if __name__ is '__main__':
    print('please use appropriate program entry')
