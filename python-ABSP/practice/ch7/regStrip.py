#! python3
# Regex version of strip()

import re, sys

def Strip(string, stripS):
    if stripS == '':
        stripS = ' '
    begin = re.compile(r'^[' + stripS + r']+')
    end = re.compile(r'[' + stripS + r']+$')
    string = begin.sub('', string)
    string = end.sub('', string)
    return string

stripS = ''
if len(sys.argv) == 2:
    stripS = sys.argv[1]

while True:
    string = input()
    print(Strip(string, stripS))

