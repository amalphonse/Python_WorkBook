# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 19:46:17 2017

@author: Anju
"""

"""
Create a script that iterates through text files and c
hecks if strings p, y, t, h, o, or n are found in the 
content of the text file. If any of those strings is found, 
append that string to a list.
"""

import glob

letters= []
check_letters = "python"

file_list = glob.iglob("letters/*.txt")

for file_name in file_list:
    with open(file_name,"r") as f:
        letter = f.read().strip("\n")
        if letter in check_letters:
            letters.append(letter)
 
print(letters)

