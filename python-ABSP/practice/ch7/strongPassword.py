#! python3
# Strong Password Detection

import re

lengthRegex = re.compile(r'.{8,}')
digitRegex = re.compile(r'.*\d+.*')
upperRegex = re.compile(r'.*[A-Z].*')
lowerRegex = re.compile(r'.*[a-z].*')

def testStrength(string):
    if lengthRegex.search(string) == None:
        return False
    if digitRegex.search(string) == None:
        return False
    if upperRegex.search(string) == None:
        return False
    if lowerRegex.search(string) == None:
        return False
    return True

while True:
    password = input()
    print(testStrength(password))
