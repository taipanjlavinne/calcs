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
            tmp = calc(moc.group())  # recursion
            x, y = moc.span()
            mtext = '%s%s%s' % (mtext[:x], tmp, mtext[y:])
            return crunch(mtext)
        moc = mofun(mtext)
        if moc is not None:
            tmp = eval(mangle_fun_to_exec(moc.group()))
            x, y = moc.span()
            mtext = '%s%s%s' % (mtext[:x], tmp, mtext[y:])
            return crunch(mtext)
        moc = mocon(mtext)
        if moc is not None:
            print (moc.group())
            tmp = eval(mangle_const_to_exec(moc.group()))
            x, y = moc.span()
            mtext = '%s%s%s' % (mtext[:x], tmp, mtext[y:])
            return crunch(mtext)
    moc = mocalc(mtext)
    if moc is not None:
        print (moc.group())
        tmp = eval(mangle_calc_to_exec(moc.group()))
        x, y = moc.span()
        mtext = '%s%s%s' % (mtext[:x], tmp, mtext[y:])
        return crunch(mtext)
    return mtext

if __name__ is '__main__':
    print('please use appropriate program entry')
