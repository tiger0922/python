#! /usr/bin/env python3

import webbrowser, sys, pyperclip, urllib.parse
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + urllib.parse.quote(address))
