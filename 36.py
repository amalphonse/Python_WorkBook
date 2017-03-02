# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 12:30:50 2017

@author: Anju
"""

def count_words(filepath):
    with open(filepath,'r') as f:
        strng = f.read()
        strng_lst = strng.split(" ")
        return len(strng_lst)
    
    
print(count_words('words.txt'))
