# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 19:48:40 2017

@author: Anju
"""
from math import pi
r =10

def liquid_volume(h):
    l_v = ((4 * pi * (r**3))/3)-((pi * h**2 *(3*r - h))/3)
    return l_v

print(liquid_volume(2))