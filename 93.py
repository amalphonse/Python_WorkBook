# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 11:36:51 2017

@author: Anju
"""
#Recursive File counter
import glob

file_list = glob.glob("subdirs/**/*.py",recursive=True)
print(len(file_list))