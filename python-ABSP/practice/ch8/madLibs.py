#! /usr/bin/env python3

import sys

textfile = open('madlib.txt', 'r')
newText = [] 

for line in textfile.readlines():
    for word in line.split():
        if word[:9] == 'ADJECTIVE':
            print('Enter an adjective:')
            adj = input()
            word = adj + word[9:]
        elif word[:4] == 'NOUN':
            print('Enter a noun:')
            n = input()
            word = n + word[4:]
        elif word[:4] == 'VERB':
            print('Enter a verb:')
            v = input()
            word = v + word[4:]
        newText.append(word)

newTextFile = open('newmadlib.txt', 'w')
print(' '.join(newText))
newTextFile.write(" ".join(newText))

