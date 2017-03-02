# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 16:39:38 2017

@author: ANju
"""

#Create a function that takes a text file as input and returns the number of words 
#contained in the text file. Please take into consideration that some words can 
#be separated by a comma with no space. For example "Hi,it's me." would need 
#to be counted as three words. For your convenience, you can use the text 
#file in the attachment.

import re

def count_words(filepath):
    with open(filepath,'r') as f:
        strng = f.read()
        strng = re.split(",| ",strng)
        return len(strng)
    
print(count_words('words2.txt'))