# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 18:34:15 2017

@author: Anju
"""

def acceleration(v1,v2,t1,t2):
    a = (v2-v1)/(t2-t1)
    return a

print(acceleration(0,10,0,20))
    