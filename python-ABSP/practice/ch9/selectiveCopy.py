#! /usr/bin/env python3

import shutil, os

os.mkdir('./JPG')
destination = './JPG'
def selectiveCopy(folder):
    folder = os.path.abspath(folder)
    
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename[-4:] == '.jpg':
                shutil.copy(os.path.join(foldername, filename), destination)
                
selectiveCopy('/Users/tsaiminhan/Public/Picture')
