# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 18:42:13 2017

@author: anju
"""

"""
Question: Create a program that once executed the program prints Hello  instantly first, then it prints it after 1 second, then after 2, 3, 4, and so on the interval 
increases between prints.

"""
import time

i=0

while True:
    i=i+1
    print("Hello")
    time.sleep(i)