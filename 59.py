# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 12:49:32 2017

@author: alphy
"""

"""
Question: Please complete the code so that it prints out the expected output.

a = [1, 2, 3] 

Expected output: 

Item 1 has index 0
Item 2 has index 1
Item 3 has index 2
"""

a = [1, 2, 3] 

for index,item in enumerate(a):
    print("Item %s had index %s"%(item,index))