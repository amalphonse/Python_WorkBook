# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 11:51:15 2017

@author: Anju
"""


#Question:  Here's another similar exercise. What will the following script output? Try to do this mentally if you can.

c = 1
def foo():
    c = 2
    return c
c = 3
print(foo())


#The Answer will be 2