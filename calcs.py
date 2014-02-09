#/usr/bin/python3

from cruncher import crunch
import argparse
from gmpy2 import round2 as rnd, mpfr as R
import gmpy2 as gmp



arpa = argparse.ArgumentParser(description='Calculates given math from cmdline')
arpa.add_argument('-p', '--precision', help='set calculation precision', type=int)
arpa.add_argument('-f', '--format', help='result format', type=int)
arpa.add_argument('-c', '--calculate', nargs='+', help='formula to calculate')
arpa.add_argument('-d', '--degrees', action='store_true',
                  help='Use degrees instead of radians')
arpa.add_argument('-g', '--graphical', action='store_true',
                  help='Show Tk calculator')
args = arpa.parse_args()

_context = gmp.get_context()

_context.precision = args.precision if args.precision else 512
_context.round = gmp.RoundToNearest
_context.subnormalize = True

if not args.graphical and args.calculate:
    result = crunch( ' '.join(args.calculate), 
                   args.degrees if args.degrees else False)
    if result.endswith('.0'):
        print (result[:-2])
    else: print (result)

