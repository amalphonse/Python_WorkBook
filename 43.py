# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 18:26:58 2017

@author: anju

"""
import string

with open("letters.txt","w") as f:
    for letter1,letter2 in zip(string.ascii_lowercase[0::2],string.ascii_letters[1::2]):
        f.write(letter1+letter2 + "\n")
