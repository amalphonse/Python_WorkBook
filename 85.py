# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 18:33:59 2017

@author: anju
"""

"""
Exercise 85 - Data Cleaner
"""

with open("countries-raw.txt","r") as f:
    content = f.readlines()
    
content = [i.strip("\n") for i in content if "\n" in i]
content = [i for i in content if i !=""]
content = [i for i in content if i != "Top of Page"]
content = [i for i in content if len(i)!=1]

print(content)

with open("countries_clean.txt","w") as f:
    for c in content:
        f.write(c+"\n")