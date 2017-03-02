# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:07:07 2017

@author: anju
"""

import string

with open("letters_1.txt","w") as f:
    for letter1,letter2,letter3 in zip(string.ascii_lowercase[0::3],string.ascii_lowercase[1::3],string.ascii_lowercase[2::3]):
        f.write(letter1+letter2 +letter3+ "\n")
