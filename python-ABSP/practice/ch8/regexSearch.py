#! /usr/bin/env python3

import os, sys, re

regex = ''
if len(sys.argv) == 2:
    regex = re.compile(sys.argv[1])
else:
    exit()

for filename in os.listdir():
    if filename[-4:] == '.txt':
        f = open(filename)
        for line in f.readlines():
            if regex.search(line):
                print(line)

