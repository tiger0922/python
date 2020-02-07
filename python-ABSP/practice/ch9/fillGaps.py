#! /usr/bin/env python3

import os, shutil, re

def getFilesWithPrefix(folder, prefix):
    fileRegex = re.compile(prefix+'(\d{1,})(.\w+)')
    fileList = []
    for file in os.listdir(folder):
        if fileRegex.match(file):
            fileList.append(file)
    fileList.sort()
    return fileList

def fillGaps(folder, prefix):
    fileList = getFilesWithPrefix(folder, prefix)
    fileRegex = re.compile(prefix+'(\d{1,})(.\w+)')

    start = int(fileRegex.search(fileList[0]).group(1))
    count = start
    max_length = len(fileRegex.search(fileList[-1]).group(1))

    for file in fileList:
        mo = fileRegex.search(file)
        fileNum = int(mo.group(1))

        if fileNum != count:
            newFileName = prefix + '0'*(max_length-len(str(fileNum))) + str(count) + mo.group(2)
            shutil.move(os.path.abspath(file), os.path.abspath(newFileName))

        count += 1


fillGaps('.', 'spam')

    
    
    

