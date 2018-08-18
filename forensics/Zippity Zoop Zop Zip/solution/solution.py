#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zipfile
import os
import sys
import glob


def unzip_recursive(filename, delete_zip=True, force_folder=False):
    """
    Extract all files from a zip file recursively
    
    args:
      filename    : path to a zip file
      delete_zip  : if true, delete the zip file after extraction
      force_folder: if true, extract files in a folder with same name as zip file
      
    return:
      Nothing
    """
    
    if not zipfile.is_zipfile(filename):
        print("not zip file:", filename)
        return
    
    with zipfile.ZipFile(filename, "r") as zf:
        file_list = zf.namelist()
        path = os.path.dirname(filename)
        if force_folder:
            path = os.path.splitext(filename)[0]   
            k = 1
            tmp = path
            while os.path.isdir(path):
                k += 1
                path = tmp + "_" + str(k)        
        
        zf.extractall(path=path)
        file_list = [os.path.join(path, f) for f in file_list]
        
    if delete_zip:
        os.remove(filename)
        
    for fn in filter(zipfile.is_zipfile, file_list):
        unzip_recursive(fn, delete_zip, force_folder)

        

def main():
    a = sys.argv[1:]
    if len(a) < 1:
        print("no input")
        return   
    for path in a:        
        if os.path.isfile(path):
            unzip_recursive(path, True, False)
        else:
            print("invalid path:", path)
        
if __name__ == "__main__":
    main()