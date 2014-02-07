#/usr/bin/env python3

from cruncher import crunch, _context
import argparse
from decimal import Decimal

arpa = argparse.ArgumentParser(description='Calculates given math from cmdline')
arpa.add_argument('-p', '--precision', help='set calculation precision', type=int)
arpa.add_argument('-f', '--format', help='result format', type=int)
arpa.add_argument('formula', nargs='+', help='formula to calculate')
arpa.add_argument('-d', '--degrees', action='store_true',
                  help='Use degrees instead of radians')
args = arpa.parse_args()

_context.precision = args.precision if args.precision else 200

print (Decimal(crunch( ''.join(args.formula), args.degrees if args.degrees else False)))
