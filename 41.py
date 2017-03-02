# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 21:00:58 2017

@author: anju
"""

"""Question: Create a script that generates a text file with all letters of English alphabet inside it, one letter per line."""


import string

def letters_file():
    with open('letters.txt','w') as f:
        for letter in string.ascii_lowercase:
            f.write(letter + "\n")
            
            
letters_file()