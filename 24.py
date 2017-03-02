# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 21:35:41 2017

@author: Anju
"""

d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

for key, value in d.items():
    print(key, "has value", value)