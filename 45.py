# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 21:15:25 2017

@author: anju
"""

import string

for letter in string.ascii_lowercase:
    with open(letter+'.txt','w') as f:
        f.write(letter)