# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 11:42:55 2017

@author: Anju
"""
#URL CLeaner

with open("urls.txt","r") as f:
    lines = f.readlines()
    
with open("urls_connected.txt","w") as f:
    for line in lines:
        line = line.replace("s","",1)
        line=line[:6] + "/"+line[6:]
        f.write(line)