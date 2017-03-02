# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 18:12:47 2017

@author: Anju
"""

#write a script that extracts letters from the 26 text files 
#and put the letters in a list

import glob

l = []
file_list = glob.glob("letters/*.txt")

for file_name in file_list:
    with open(file_name,"r") as f:
        l.append(f.read().strip("\n"))
        
print(l)