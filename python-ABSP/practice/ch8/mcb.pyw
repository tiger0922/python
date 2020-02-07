#! /usr/bin/env python3

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3: 
    keyword = sys.argv[2]
    if sys.argv[1].lower() == 'save':
        mcbShelf[keyword] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[keyword]
elif len(sys.argv) == 2:
    keyword = sys.argv[1]
    if keyword.lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif keyword.lower() == 'delete':
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[keyword])

mcbShelf.close()
