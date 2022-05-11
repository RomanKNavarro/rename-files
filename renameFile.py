#! python3
# fileRename.py - After disk clean up, used to give files original names

import os
culprits = []
fixed = []
for (folder, folders, filenames) in os.walk("C:\Coding Shit\myPrograms"):
    for filename in filenames:
        if filename.endswith('UTC).py'):
            culprits.append(filename)

print(culprits)
for i in culprits:
    fixed.append(i.replace(' (2020_05_16 22_06_50 UTC)', ''))

print(fixed)

###############################
# REAL PROGRAM
# I FUCKED UP AND MADE EVERY SINGLE PY FILE INTO TEXT

'''for (folder, folders, filenames) in os.walk("C:\Coding Shit\myPrograms"):
    for filename in filenames:
        if filename.endswith('(2'):
            os.rename(os.path.join(folder, filename), os.path.join(folder, filename[:-27]))'''

#############################
# PHASE 2
# TURN TO PY AGAIN

from pathlib import Path

'''p = Path("C:\Coding Shit\myPrograms\ATBS Chapter 3 (2)\sameName2 (2")
p.rename(p.with_suffix('.py'))'''


for (folder, folders, filenames) in os.walk("C:\Coding Shit\myPrograms"):
    for filename in filenames:
        if filename.endswith('(2'):
            p = Path(os.path.join(folder, filename))
            #p.rename(p.with_suffix('.py'))
            
#########################
# PHASE 3
# REMOVE LAST STRAGGLERS, IT WORKED

for (folder, folders, filenames) in os.walk("C:\Coding Shit\myPrograms"):
    for filename in filenames:
        if filename.endswith('(2.py'):
            os.rename(os.path.join(folder, filename), os.path.join(folder, filename.replace(' (2', '')))



            
                             
