# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 18:05:28 2017

@author: anju
"""

"""
Question: The code produces an error. Please understand the error and try to fix it

age = input("What's your age? ")
age_last_year = age - 1
print("Last year you were %s." % age_last_year)
"""

age = input("What's your age? ")
age_last_year = int(age) - 1
print("Last year you were %s." % age_last_year)