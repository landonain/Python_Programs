#! python3
# pw.py - An insecure password locker program

import sys
import pyperclip

cookbook = {'chick': """Chicken Thighs, Red Cabbage,
                Green Lettuce, Cheese, Carrots,
                Mutligrain wraps, Total Cost 37.50
                or 3.16 per wrap (possibly lower)""",
             'notemail': 'duhher'}


if len(sys.argv) < 2:
    print('Usage: python pw.py [recipe] - copy recipe and cost')
    sys.exit()

recipe = sys.argv[1] #first command line arg is the account name

if recipe in cookbook:
    pyperclip.copy(cookbook[recipe])
    print('Recipe for ' + recipe + ' copied to clipboard.')
else:
    print('There is no account named ' + recipe)

