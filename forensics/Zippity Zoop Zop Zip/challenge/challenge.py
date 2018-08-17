#!/usr/bin/env python

"""
This file generates a tree of zip folders.
Each "node" in the tree contains "file.txt" with a random fileContentFiller seen below.
Each "node" also contains "foldersPerLevel" zip files to go further down into the tree.
The flag is stored in one of the leaf nodes.
The size and width of the tree can be changed in main().

If you make a tree thats too big and have to kill the process you'll end up with so many zip files that "rm *.zip" will complain.
Use this instead "find . -name "*.zip" -print0 | xargs -0 rm"
"""

import os
import zipfile
import random
import shutil
import uuid

FLAG = "flag{i_b3t_y0u_pa1d_4_w1nr4r}"

class zipTree:

    fileContentFiller = ["Are you sure you're going the right way?",
                        "That other path looked promising ..",
                        "They wouldn't hide it that far down right?",
                        "Maybe you should automate this ..",
                        "Almost there! Probably.",
                        "What if this loops somehow ..",
                        "flag{h4ha_ju5t_k1dding_th15_i5nt_4_rea1_fl4g}",
                        "You might have missed it.",
                        "Try going back 1 and then down 3.",
                        "id: e3d8dce4-a1d7-11e8-9819-00163e626700",
                        "What do those uuid's mean?"
                        ]
    folderNames = ["Nothing_Over_Here",
                    "The_Flag_Is_Totally_This_Way",
                    "Inconspicuous_Folder",
                    "system32",
                    "xXx_haxorz420_xXx",
                    "Dont_Flag_Open_Inside",
                    "Useless_Folder",
                    "Free_Points_This_Way",
                    ""]
    fileName = "file.txt"

    def __init__(self, levels=3, foldersPerLevel=3):
        self.levels = levels
        self.foldersPerLevel = foldersPerLevel

    def generateTree(self):
        allBaseZips = self._generate_all_base_zips()
        while self.levels:
            allBaseZips = self._generate_tree_helper(allBaseZips)
            self.levels -= 1
    
    def _generate_all_base_zips(self):
        numberOfBaseZips = self.foldersPerLevel ** self.levels
        
        zipName = self._generate_base_zip(insertFlag = FLAG)
        allBaseZips = []
        allBaseZips.append(zipName)
        for _ in xrange(numberOfBaseZips-1):
            zipName = self._generate_base_zip()
            allBaseZips.append(zipName)
        return allBaseZips

    def _generate_base_zip(self, insertFlag=""):
        folderName = self._generate_random_folder()
        with open(folderName+"/"+self.fileName, 'w') as f:
            # Get random filler text and add it to file
            if insertFlag == "":
                fileFiller = self.fileContentFiller[random.randint(0,len(self.fileContentFiller)-1)]
            else:
                fileFiller = insertFlag
            f.write(fileFiller)

        self._zip_folder(folderName)
        return folderName+'.zip'

    def _generate_tree_helper(self, allZipsInDir):
        zipsForNextLevel = []
        zipsForThisLevel = []
        for i in xrange(len(allZipsInDir)):
            zipsForThisLevel.append(allZipsInDir[i])
            if (i+1)%self.foldersPerLevel == 0:
                zipsForNextLevel.append(self._add_files_to_zip(zipsForThisLevel))
                zipsForThisLevel = []
        return zipsForNextLevel

    def _zip_folder(self, folderName):
        zipf = zipfile.ZipFile(folderName+'.zip', 'w')
        for _, _, files in os.walk(folderName):
            for f in files:
                # print(f)
                zipf.write(folderName + '/' + f)
        zipf.close()
        shutil.rmtree(folderName) # Remove folder (keep the zip)
        return folderName+'.zip'

    def _generate_random_folder(self):
        folderName = self.folderNames[random.randint(0,len(self.folderNames)-1)] # Choose random folder name
        folderName = folderName + str(uuid.uuid1()) # Add an id to it just because
        os.makedirs(folderName) # Make the directory
        return folderName

    def _add_files_to_zip(self, filesToAdd):
        
        folderName = self._generate_random_folder()
        # Add file to folder
        with open(folderName+"/"+self.fileName, 'w') as f:
            # Get random filler text and add it to file
            fileFiller = self.fileContentFiller[random.randint(0,len(self.fileContentFiller)-1)]
            f.write(fileFiller)
        for f in filesToAdd:
            shutil.move(f, folderName+'/'+f)
        zipName = self._zip_folder(folderName)

        return zipName
        

def main():
    myTree = zipTree(levels=10, foldersPerLevel=3)
    myTree.generateTree()

if __name__ == '__main__':
    main()