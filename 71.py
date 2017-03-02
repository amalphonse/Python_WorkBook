# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 07:02:56 2017

@author: anju
"""
"""
Question: Count the number of "a" characters in this text file: 
    http://www.pythonhow.com/data/universe.txt
"""
import requests

r= requests.get("http://www.pythonhow.com/data/universe.txt")
text = r.text
count_a = text.count("a")
print(count_a)