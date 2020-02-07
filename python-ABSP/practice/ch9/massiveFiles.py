#! /usr/bin/env python3

import os

def listBigFiles(folder):
    folder = os.path.abspath(folder)
    
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            try:
                if os.path.getsize(os.path.join(foldername, filename)) > 100000000:
                    print(os.path.join(foldername, filename))
            except:
                continue

listBigFiles('/Users/tsaiminhan/')
