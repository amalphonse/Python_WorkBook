# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 06:58:55 2017

@author: anju
"""

"""
Question: Print out the text of this file 
http://www.pythonhow.com/data/universe.txt. 
Please don't manually download the file. 
Let Python do all the work.
"""
import requests

r = requests.get("http://www.pythonhow.com/data/universe.txt")
print(r.text)