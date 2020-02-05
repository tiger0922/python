#! python3
# Add star sign at the beginning of each line

import pyperclip

text = pyperclip.paste()
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
    print(lines[i])

clip = '\n'.join(lines)
pyperclip.copy(clip)
