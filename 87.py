# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 18:56:17 2017

@author: anju
"""

#Data Missing

checklist = ["Portugal","Germany","Spain"]
checklist = [i+"\n" for i in checklist]

with open("countries-missing.txt","r") as f:
    content = f.readlines()
    
updated = sorted(checklist+content)

with open("countries_missing_fixed.txt","w") as f:
    for i in updated:
        f.write(i)

