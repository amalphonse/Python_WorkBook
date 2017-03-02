# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 12:28:28 2017

@author: alphy
"""

#String Splitter

def string_splitter(strng):
    strng = strng.split(" ")
    strng_len = len(strng)
    return strng_len

print(string_splitter("Hello World"))