# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 09:32:14 2017

@author: Anju
"""

#Question: Filter the dictionary by removing all items with a value of greater than 1.

d = {"a": 1, "b": 2, "c": 3}


dct = dict((key,value) for key,value in d.items() if value<=1)
print(dct)