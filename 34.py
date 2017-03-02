# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 12:28:25 2017

@author: alphy
"""
def foo():
    global c
    c = 1 
    return c 
foo() 
print(c)