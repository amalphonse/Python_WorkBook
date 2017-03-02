# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 18:50:58 2017

@author: anju
"""

"""
Data checker
"""

checklist = ["Portugal", "Germany", "Munster", "Spain"]

with open("countries_clean.txt","r") as f:
    content = f.readlines()

content = [i.strip("\n") for i in content]

checked_list = [i for i in content if i in checklist]
print(checked_list)